import json,pathlib
from typing import Any

class Configuration:
    def __init__(self):
        self.ark_manager_location: str = str(pathlib.Path(__file__).parent.absolute()) + "/"
        self.config_path: str = self.ark_manager_location + "../config/"
        self.base_files_path: str = self.ark_manager_location + "../base_files/"
        try:
            self.files_locations = self.__get_config("locations.json")
        except Exception as e:
            print(e)

    def __get_config(self,file: str) -> Any:
        try:
            with open(self.config_path+file, 'r') as json_file:
                data = json.load(json_file)
                return data
        except:
            raise Exception("Could not read {}.".format(file))

    def __get_base_file(self,file: str):
        try:
            with open(self.base_files_path+file, 'r') as base_file:
                return base_file.read().splitlines()
        except:
            raise Exception("Could not read {}.".format(file))

    def get_server_starter_settings(self) -> Any:
        try:
            return self.__get_config("server_starter.json")
        except Exception as e:
            print(e)
    
    def get_game_user_settings(self) -> Any:
        try:
            return self.__get_config("game_user_settings.json")
        except Exception as e:
            print(e)

    def get_game_settings(self) -> Any:
        try:
            return self.__get_config("game.json")
        except Exception as e:
            print(e)

    def get_base_game_user_settings(self):
        try:
            return self.__get_base_file("base_game_user_settings.ini")
        except Exception as e:
            print(e)