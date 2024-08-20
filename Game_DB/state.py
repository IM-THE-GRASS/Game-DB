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
    def get_img(self, game_id):
        return "https:" + self.get_from_api("artworks", "f *; where game = 18158; l 50;")[0]["url"].replace("thumb", "screenshot_big")
        
    def get_search_results(self):
        self.search_results = self.get_from_api("games", f'f name, involved_companies; search "{self.search_value}"; where version_parent = null;')
        print(self.get_img(1))
    
    def submit_search(self):
        if self.search_focus:
            return rx.redirect(f"/search")
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        self.search_value = new
    def print(self):
        print("AAA")