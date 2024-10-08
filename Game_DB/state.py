import reflex as rx
import dotenv
import os
import requests
import time
import threading
import json
import os
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
    
    def int(self, info, number):
        if int(info["aggregated_rating"]) >= number:
            return True
        else:
            return False
    
    @rx.var()
    def search_disabled(self) -> bool:
        return self.sort or self.sort_for
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
            self.sort_for = ""
        if self.search_results == [] and self.loading:
            self.search_results_loading = True
        else:
            self.search_results_loading =  False
    
    
        
        
        
    # sort
    sort:str
    sort_for:str
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
    }
    
    def fix_thing(to_fix):
        for thing in to_fix:
            print(thing)
            thing["value"] = thing["id"]
            thing.pop("id")
            thing["label"] = thing["name"]
            thing.pop("name")    
        return to_fix
    sort_for_options:list[dict[str, str]] = []
    sort_options = [
        {
            "value":"first_release_date",
            "label":"Release date",
            "sort":True
        },
        {
            "value":"rating",
            "label":"Average Rating",
            "sort":True
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
            self.sort_for = new["value"]
            self.submit_search2()
        except:
            self.sort_for = ""
        
    def set_sort(self, new):
        self.sort_info = new
        try:
            self.sort = new["value"]
            self.sort_for_disabled = False
            self.sort_for_options = self.sort_fors[new["label"]]
            if self.sort_for:
                self.submit_search2()
        except:
            # this runs if thething is none
            self.sort_for_disabled = True
            self.sort = ""
            time.sleep(1)
    
    
    
    
    
    
    # filter
    filter:str
    filter_for:str
    filter_for_disabled:bool = True
    filter_fors:dict = {}
    filter_fors["Genre"] = get_from_api2(endpoint="genres", payload="f name, id; l 500;")
    filter_fors["Genre"] = fix_thing(filter_fors["Genre"])
    filter_fors["Game Engine"] = get_from_api2(endpoint="game_engines", payload="f name, id; l 500;")
    filter_fors["Game Engine"] = fix_thing(filter_fors["Game Engine"])
    filter_fors["Platform"] = get_from_api2(endpoint="platforms", payload="f name, id; l 500;")
    filter_fors["Platform"] = fix_thing(filter_fors["Platform"])
    filter_fors["Player Perspective"] = get_from_api2(endpoint="player_perspectives", payload="f name, id; l 500;")
    filter_fors["Player Perspective"] = fix_thing(filter_fors["Player Perspective"])
    filter_fors["Theme"] = get_from_api2(endpoint="themes", payload="f name, id; l 500;")
    filter_fors["Theme"] = fix_thing(filter_fors["Theme"])
    filter_fors["Franchise"] = get_from_api2(endpoint="franchises", payload="f name, id; l 500;")
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 500;"))
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 1000;"))
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 1500;"))
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 2000;"))
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 2500;"))
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 3000;"))
    filter_fors["Franchise"].extend(get_from_api2(endpoint="franchises", payload="f name, id; l 500; offset 3500;"))
    print(len(filter_fors["Franchise"]))
    filter_fors["Franchise"] = fix_thing(filter_fors["Franchise"])
    filter_fors["Game mode"] = get_from_api2(endpoint="game_modes", payload="f name, id; l 500;")
    filter_fors["Game mode"] = fix_thing(filter_fors["Game mode"])
    
    
    filter_fors["Game Engine"] = get_from_api2(endpoint="game_engines", payload="f name, id; l 500;")
    filter_fors["Game Engine"].extend(get_from_api2(endpoint="game_engines", payload="f name, id; l 500; offset 500;"))
    filter_fors["Game Engine"].extend(get_from_api2(endpoint="game_engines", payload="f name, id; l 500; offset 1000;"))
    filter_fors["Game Engine"].extend(get_from_api2(endpoint="game_engines", payload="f name, id; l 500; offset 1500;"))
    filter_fors["Game Engine"].extend(get_from_api2(endpoint="game_engines", payload="f name, id; l 500; offset 2000;"))
    filter_fors["Game Engine"].extend(get_from_api2(endpoint="game_engines", payload="f name, id; l 500; offset 2500;"))
    print(len(filter_fors["Game Engine"]))
    print(len(filter_fors["Platform"]))
    
    filter_fors["Game Engine"] = fix_thing(filter_fors["Game Engine"])
    data = json.dumps(filter_fors, indent=4)
    open(os.path.join(os.getcwd(), "assets","sort_options.json"), "w").write(json.dumps(filter_fors, indent=4))
    # print(json.dumps(filter_fors))
    filter_for_options:list[dict[str, str]] = []
    filter_options = [
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
            "value":"platforms",
            "label":"Platform",
            "sort":False
        },
        {
            "value":"game_modes",
            "label":"Game mode",
            "sort":False
        },
        {
            "value":"genres",
            "label":"Genre",
            "sort":False
        },
    ]
    filter_info:dict
    def set_filter_for(self, new):
        try:
            self.filter_for = new["value"]
            self.submit_search2()
        except:
            # this runs if thething is none
            self.filter_for = ""
        
    def set_filter(self, new):
        self.filter_info = new
        try:
            self.filter = new["value"]
            self.filter_for_disabled = False
            self.filter_for_options = self.filter_fors[new["label"]]
            if self.filter_for:
                self.submit_search2()
        except:
            self.filter_for_disabled = True
            self.filter = ""
            time.sleep(1)
    
            
            
            
            
            
            
            
    # search stuff
    def submit_search(self):
        if self.search_focus:
            return rx.redirect("/search")
    
    def submit_search2(self):
        if self.sort and self.sort_for:
            
            if self.filter and self.filter_for:
                self.get_search_results(self.sort,self.sort_for,self.filter,self.filter_for)
            else:
                self.get_search_results(self.sort, self.sort_for,"","")
        elif self.filter and self.filter_for:
            self.get_search_results("","",self.filter,self.filter_for)
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
    def get_search_results(self, sort:str = "", sort_for:str = "", filter = "", filter_for = ""):
        def mains():
            if sort and sort_for:
                if filter and filter_for:
                    response = self.get_from_api("games", f'f *   ; where version_parent = null; l 100; where {filter} = {filter_for}; sort {sort} {sort_for};')    
                else:
                    response = self.get_from_api("games", f'f *   ; where version_parent = null; l 100; sort {sort} {sort_for};')
            elif filter and filter_for:
                response = self.get_from_api("games", f'f *   ; search "{self.search_value}"; where version_parent = null; where {filter} = {filter_for}; l 100;')
                print(f'f *   ; where version_parent = null; where {filter}[{filter_for}]; l 100;')
            else:
                response = self.get_from_api("games", f'f *   ; search "{self.search_value}"; where version_parent = null; l 100;')
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
        
    def get_screenshots(self, screenshot_ids):
        try:
            screenshots = []
            for screenshot in screenshot_ids:
                ss_response = self.get_from_api("screenshots", f"f *; where id = {screenshot};")
                ss_url = "https:" + ss_response[0]["url"]
                screenshots.append(ss_url)
            return screenshots
            print(screenshots)
        except:pass   
        
    # platform stuff
    search_results_loading:bool
    platforms_search_results:list[dict[str,str]]
    # ideas
    # generation
    # alphabetical
    # family
    
    platform_sort_options:list = [
        {
            "value":"generation",
            "label":"Generation" 
        },
        {
            "value":"name",
            "label":"Alphabetical"
        }
    ]
    platform_sort_for_options:list[dict[str,str]] = [
        {
            "value":"asc",
            "label":"Ascending"
        },
        {
            "value":"desc",
            "label":"Decending",
        }
    ]
    def platform_set_sort_for(self, new):
        try:
            self.sort_for = new["value"]
            self.on_platform_submit()
        except:
            self.sort_for = ""
        
    def platform_set_sort(self, new):
        try:
            self.sort = new["value"]
            self.sort_for_disabled = False
            # self.sort_for_options = self.sort_fors[new["label"]]
            if self.sort_for:
                self.on_platform_submit()
        except:
            # this runs if thething is none
            self.sort_for_disabled = True
            self.sort = ""
            time.sleep(1)
    def on_platform_submit(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
        if self.sort and self.sort_for:
            self.platform_get_search_results(self.sort, self.sort_for)
        else:
            self.platform_get_search_results()
            
    def platform_get_search_results(self, sort:str = "", sort_for:str = ""):
        def mains():
            if sort and sort_for:
                response = self.get_from_api("platforms", f'f *   ; sort {sort} {sort_for}; l 100;')
            else:
                response = self.get_from_api("platforms", f'f *   ; search "{self.search_value}"; l 100;')
            self.platforms_search_results = []
            self.loading = True
            for result in response:
                if self.stop_thread:
                    return
                try:
                    cover_response = self.get_from_api("platform_logos", f"f *; where id = {result['platform_logo']};")
                    url = "https:" + cover_response[0]["url"]
                    url = url.replace("thumb", "cover_big_2x")
                    if url == "":
                        raise Exception()
                except:
                    try:
                        cover_response = self.get_from_api("platform_logos", f"f *; where id = {result['platform_logo']};")
                        url = "https:" + cover_response[0]["url"]
                        print(result["name"], " IS SECOND AT")
                    except:
                        try:print(result["name"], "FAILED")
                        except:
                            print(result)
                            break
                        pass
                try:
                    result["img"] = url
                    url = ""
                except:pass
                self.platforms_search_results.append(result)
                print(result, "RESULT   ")
            self.loading = False
        self.stop_thread = True
        self.loading = True
        time.sleep(1)
        self.stop_thread = False
        thread = threading.Thread(target=mains)
        thread.start()
    
    
    
    
    
    
    
    
    
    #characters 
    
    search_results_loading:bool
    characters_search_results:list[dict[str,str]]
    # ideas
    # generation
    # alphabetical
    # family
    
    character_sort_options:list = [
        {
            "value":"name",
            "label":"Alphabetical"
        }
    ]
    character_sort_for_options:list[dict[str,str]] = [
        {
            "value":"asc",
            "label":"Ascending"
        },
        {
            "value":"desc",
            "label":"Decending",
        }
    ]
    def character_set_sort_for(self, new):
        try:
            self.sort_for = new["value"]
            self.on_character_submit()
        except:
            self.sort_for = ""
        
    def character_set_sort(self, new):
        try:
            self.sort = new["value"]
            self.sort_for_disabled = False
            # self.sort_for_options = self.sort_fors[new["label"]]
            if self.sort_for:
                self.on_character_submit()
        except:
            # this runs if thething is none
            self.sort_for_disabled = True
            self.sort = ""
            time.sleep(1)
    def on_character_submit(self):
        if self.sort and self.sort_for:
            self.character_get_search_results(self.sort, self.sort_for)
        else:         
            self.character_get_search_results()
            
    def character_get_search_results(self, sort:str = "", sort_for:str = ""):
        def mains():
            print("HEHEHHAHAHHA")
            if sort and sort_for:
                print("AA")
                response = self.get_from_api("characters", f'f *   ; sort {sort} {sort_for}; l 100;')
            else:
                response = self.get_from_api("characters", f'f *   ; search "{self.search_value}"; l 100;')
            self.characters_search_results = []
            self.loading = True
            for result in response:
                if self.stop_thread:
                    return
                try:
                    cover_response = self.get_from_api("character_mug_shots", f"f *; where id = {result['mug_shot']};")
                    url = "https:" + cover_response[0]["url"]
                    url = url.replace("thumb", "cover_big_2x")
                    if url == "":
                        raise Exception()
                except:
                    try:
                        cover_response = self.get_from_api("character_mug_shots", f"f *; where id = {result['mug_shot']};")
                        url = "https:" + cover_response[0]["url"]
                        print(result["name"], " IS SECOND AT")
                    except:
                        try:print(result["name"], "FAILED")
                        except:
                            print(result)
                            break
                        pass
                try:
                    result["img"] = url
                    url = ""
                except:pass
                self.characters_search_results.append(result)
                print(result, "RESULT   ")
            self.loading = False
        self.stop_thread = True
        self.loading = True
        time.sleep(1)
        self.stop_thread = False
        thread = threading.Thread(target=mains)
        thread.start()