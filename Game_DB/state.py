import reflex as rx
import dotenv
import os
import requests
import time
import threading
dotenv.load_dotenv()
# API configuration
client_id = os.environ.get("client_id")
access_token = os.environ.get("token")
base_url = 'https://api.igdb.com/v4'
class State(rx.State):
    search_value:str = ""
    search_focus:bool = False
    search_results:list[dict[str, str]] = []
    loading:bool
    stop_thread:bool
    @rx.var()
    def search_resultss(self) -> str:
        return str(self.search_results)
    def get_from_api(self, endpoint, payload):
        response = requests.post(
            f'https://api.igdb.com/v4/{endpoint}',
            **{
                'headers': {'Client-ID': f'{client_id}', 'Authorization': f'Bearer {access_token}'},
                'data': payload
            }
        )
        return response.json()
        
    def get_search_results(self):
        def mains():
            self.loading = True
            response = self.get_from_api("games", f'f name, platforms, screenshots, cover   ; search "{self.search_value}"; where version_parent = null; l 100;')
            self.search_results = []
            for result in response:
                if self.stop_thread:
                    return
                try:
                    cover_response = self.get_from_api("covers", f"f *; where id = {result['cover']};")
                    url = "https:" + cover_response[0]["url"]
                    url = url.replace("thumb", "cover_big")
                    if url == "":
                        raise Exception()
                except:
                    try:
                        cover_response = self.get_from_api("covers", f"f *; where id = {result['cover']};")
                        url = "https:" + cover_response[0]["url"]
                        print(result["name"], " IS SECOND AT")
                    except:
                        try:
                            cover_response = self.get_from_api("screenshots", f"f *; where id = {result['screenshots'][0]};")
                            url = "https:" + cover_response[0]["url"]
                            print(result["name"], "GOT TO THIRD")
                        except:
                            print(result["name"], "FAILED")
                            pass
                try:platforms = self.get_from_api("platforms", f"f *; where id = {result['platforms'][0]};")
                except:pass
                try:
                    
                    result["platform"] = platforms[0]["abbreviation"]
                except:pass
                try:
                    result["img"] = url
                    url = ""
                except:pass
                self.search_results.append(result)
            self.loading = False
            print(response)
        self.stop_thread = True
        time.sleep(1)
        self.stop_thread = False
        thread = threading.Thread(target=mains)
        thread.start()
    
    def submit_search(self):
        if self.search_focus:
            return rx.redirect("/search")
    def submit_search2(self):
        if self.search_focus:
            self.get_search_results()
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        self.search_value = new
    def print(self,_):
        self.search_results = self.search_results