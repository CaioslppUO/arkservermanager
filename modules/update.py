import configuration
class Update:
    def __init__(self):
        self.configuration = Configuration()

    def __write_update(self,file: str,content: str) -> None:
        try:
            with open(file, 'w') as config_file:
                config_file.write(content)
        except:
            raise Exception("Could not write to {}.".format(file))

    def update_server_starter(self,arguments: str):
        try:
            self.__write_update(
                self.configuration.files_locations['server_start_location'] +
                self.configuration.files_locations['server_start_name'],
                arguments
            )
        except Exception as e:
            print(e)

    def update_game_settings(self,arguments: str):
        try:
            self.__write_update(
                self.configuration.files_locations['config_files_location'] +
                "Game.ini",
                arguments
            )
        except Exception as e:
            print(e)
    
    def update_game_user_settings(self,arguments: str):
        try:
            self.__write_update(
                self.configuration.files_locations['config_files_location'] +
                "GameUserSettings.ini",
                arguments
            )
        except Exception as e:
            print(e)