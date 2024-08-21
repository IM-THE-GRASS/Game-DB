import reflex as rx
import dotenv
import os
import requests
import time
import threading
from datetime import datetime
dotenv.load_dotenv()
# API configuration
client_id = os.environ.get("client_id")
access_token = os.environ.get("token")
base_url = 'https://api.igdb.com/v4'
class State(rx.State):
    search_value:str = ""
    search_focus:bool = False
    search_results:list[dict[str, str]] = []
    search_sort:str
    search_sort_order:str
    loading:bool
    stop_thread:bool
    @rx.var()
    def search_disabled(self) -> bool:
        return self.search_sort or self.search_sort_order
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
        
    def get_search_results(self, search_sort:str = "", search_sort_order:str = ""):
        def mains():
            self.loading = True
            if search_sort and search_sort_order:
                response = self.get_from_api("games", f'f name, platforms, screenshots, cover, first_release_date   ; where version_parent = null; l 100; sort {search_sort} {search_sort_order};')
            else:
                response = self.get_from_api("games", f'f name, platforms, screenshots, cover, first_release_date   ; search "{self.search_value}"; where version_parent = null; l 100;')
            self.search_results = []
            for result in response:
                print(result)
                if self.stop_thread:
                    return
                try:
                    year = datetime.utcfromtimestamp(result["first_release_date"]).strftime('%Y')
                    result["year"] = year
                except:pass
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
        if self.search_sort and self.search_sort_order:
            self.get_search_results(self.search_sort, self.search_sort_order)
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        if not self.search_disabled:
            self.search_value = new
    def print(self,_):
        self.search_results = self.search_results
    def test(self, _):
        print(_)
    def set_sort_order(self, new):
        try:
            self.search_sort_order = new["value"]
        except:
            pass
    def set_sort(self, new):
        try:
            self.search_sort = new["value"]
        except:
            pass
        