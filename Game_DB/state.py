import reflex as rx
import dotenv
import os
import requests
import time
import threading
import json
from datetime import datetime

# todo:
# gmae mode 


dotenv.load_dotenv()
# API configuration
client_id = os.environ.get("client_id")
access_token = os.environ.get("token")
base_url = 'https://api.igdb.com/v4'
class State(rx.State):
    loading:bool = False
    
    search_value:str = ""
    search_focus:bool = False
    search_results:list[dict[str, str]] = []
    search_results_loading:bool = False
    
    @rx.var()
    def search_disabled(self) -> bool:
        return self.search_sort or self.search_sort_for
    def get_from_api(self, endpoint, payload):
        response = requests.post(
            f'https://api.igdb.com/v4/{endpoint}',
            **{
                'headers': {'Client-ID': f'{client_id}', 'Authorization': f'Bearer {access_token}'},
                'data': payload
            }
        )
        return response.json()
    def get_from_api2(endpoint:str, payload:str):
        response = requests.post(
            f'https://api.igdb.com/v4/{endpoint}',
            **{
                'headers': {'Client-ID': f'{client_id}', 'Authorization': f'Bearer {access_token}'},
                'data': payload
            }
        )
        print(response)
        return response.json()
    
    
    #importantloading stuff i think
    
    def on_load(self):
        return self.get_search_results()
    def on_update(self,_):
        self.search_results = self.search_results
        if self.sort_for_disabled:
            self.search_sort_for = ""
        if self.search_results == [] and self.loading:
            self.search_results_loading = True
        else:
            self.search_results_loading =  False
    
    
        
        
        
    # sort
    search_sort:str
    search_sort_for:str
    sort_for_disabled:bool = True
    sort_fors:dict = {
        "Release date":[
            {
                "value":"asc",
                "label":"Ascending"
            },
            {
                "value":"desc",
                "label":"Decending",
            }
        ],
        "Alphabetical":[
            {
                "value":"asc",
                "label":"Ascending"
            },
            {
                "value":"desc",
                "label":"Decending",
            }
        ],
        "Average Rating":[
            {
                "value":"asc",
                "label":"Ascending"
            },
            {
                "value":"desc",
                "label":"Decending",
            }
        ],
        "Popularity":[
            {
                "value":"asc",
                "label":"Ascending"
            },
            {
                "value":"desc",
                "label":"Decending",
            }
        ],
    }
    
    def fix_thing(to_fix):
        for thing in to_fix:
            thing["value"] = thing["id"]
            thing.pop("id")
            thing["label"] = thing["name"]
            thing.pop("name")    
        return to_fix
    sort_fors["Genre"] = get_from_api2(endpoint="genres", payload="f name, id; l 500;")
    sort_fors["Genre"] = fix_thing(sort_fors["Genre"])
    sort_fors["Game Engine"] = get_from_api2(endpoint="game_engines", payload="f name, id; l 500;")
    sort_fors["Game Engine"] = fix_thing(sort_fors["Game Engine"])
    sort_fors["Platform"] = get_from_api2(endpoint="platforms", payload="f name, id; l 500;")
    sort_fors["Platform"] = fix_thing(sort_fors["Platform"])
    sort_fors["Player Perspective"] = get_from_api2(endpoint="player_perspectives", payload="f name, id; l 500;")
    sort_fors["Player Perspective"] = fix_thing(sort_fors["Player Perspective"])
    sort_fors["Theme"] = get_from_api2(endpoint="themes", payload="f name, id; l 500;")
    sort_fors["Theme"] = fix_thing(sort_fors["Theme"])
    sort_fors["Franchise"] = get_from_api2(endpoint="franchises", payload="f name, id; l 500;")
    sort_fors["Franchise"] = fix_thing(sort_fors["Franchise"])
    sort_fors["Game mode"] = get_from_api2(endpoint="game_modes", payload="f name, id; l 500;")
    sort_fors["Game mode"] = fix_thing(sort_fors["Game mode"])
    print(sort_fors["Game Engine"])
    sort_for_options:list[dict[str, str]] = []
    sort_options = [
        {
            "value":"first_release_date",
            "label":"Release date",
            "sort":True
        },
        {
            "value":"franchises",
            "label":"Franchise",
            "sort":False    
        },
        {
            "value":"game_engines",
            "label":"Game Engine",
            "sort":False
        },
        {
            "value":"player_perspectives",
            "label":"Player Perspective",
            "sort":False
        },
        {
            "value":"themes",
            "label":"Theme",
            "sort":False
        },
        {
            "value":"rating",
            "label":"Average Rating",
            "sort":True
        },
        {
            "value":"rating_count",
            "label":"Popularity",
            "sort":True
        },
        {
            "value":"platforms",
            "label":"Platform",
            "sort":False
        },
        {
            "value":"gmae_modes",
            "label":"Game mode",
            "sort":False
        },
        {
            "value":"genres",
            "label":"Genre",
            "sort":False
        },
        {
            "value":"name",
            "label":"Alphabetical",
            "sort":True
        },
    ]
    sort_info:dict
    def set_sort_for(self, new):
        try:
            self.search_sort_for = new["value"]
            self.submit_search2()
        except:
            self.search_sort_for = ""
        
    def set_sort(self, new):
        self.sort_info = new
        try:
            self.search_sort = new["value"]
            self.sort_for_disabled = False
            self.sort_for_options = self.sort_fors[new["label"]]
        except:
            self.sort_for_disabled = True
            self.search_sort = ""
            time.sleep(1)
            
            
            
            
            
            
            
    # search stuff
    def submit_search(self):
        if self.search_focus:
            return rx.redirect("/search")
    
    def submit_search2(self):
        if self.search_disabled:
            if self.sort_info["sort"]:
                self.get_search_results(self.search_sort, self.search_sort_for,"","")
            else:
                self.get_search_results("","",self.search_sort,self.search_sort_for)
        else:
            self.get_search_results()
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        if not self.search_disabled:
            self.search_value = new
            
    def print(self, _):
        pass
            

    # big boy search 
    stop_thread:bool
    def get_search_results(self, search_sort:str = "", search_sort_for:str = "", filter = "", filter_for = ""):
        def mains():
            if search_sort and search_sort_for:
                response = self.get_from_api("games", f'f name, platforms, screenshots, cover, first_release_date   ; where version_parent = null; l 100; sort {search_sort} {search_sort_for};')
            elif filter and filter_for:
                response = self.get_from_api("games", f'f name, platforms, screenshots, cover, first_release_date   ; where version_parent = null; where {filter} = {filter_for}; l 100;')
                print(f'f name, platforms, screenshots, cover, first_release_date   ; where version_parent = null; where {filter}[{filter_for}]; l 100;')
            else:
                response = self.get_from_api("games", f'f name, platforms, screenshots, cover, first_release_date   ; search "{self.search_value}"; where version_parent = null; l 100;')
            self.search_results = []
            self.loading = True
            for result in response:
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
                            try:print(result["name"], "FAILED")
                            except:
                                print(result)
                                break
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
        self.stop_thread = True
        self.loading = True
        time.sleep(1)
        self.stop_thread = False
        thread = threading.Thread(target=mains)
        thread.start()
        