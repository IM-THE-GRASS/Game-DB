import reflex as rx
import dotenv
import os
import requests
import json

dotenv.load_dotenv()

# API configuration
client_id = os.environ.get("client_id")
access_token = os.environ.get("token")
base_url = 'https://api.igdb.com/v4'
class State(rx.State):
    search_value:str = ""
    search_focus:bool = False
    search_results:list[dict[str, str]]
    
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
        response = self.get_from_api("games", f'f *; search "{self.search_value}"; where version_parent = null;')
        for result in response:
            print(result)
            try:
                cover_response = self.get_from_api("covers", f"f *; where id = {result['cover']};")
                url = "https:" + cover_response[0]["url"]
                url = url.replace("thumb", "cover_big")
            except:pass
            platforms = self.get_from_api("platforms", f"f *; where id = {result['platforms'][0]};")
            result["platform"] = platforms[0]["abbreviation"]
            print(platforms)
            result["img"] = url
        self.search_results = response
    
    def submit_search(self):
        if self.search_focus:
            return rx.redirect(f"/search?{self.search_value}")
    def submit_search2(self):
        if self.search_focus:
            self.get_search_results()
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        self.search_value = new
    def print(self):
        print("AAA")