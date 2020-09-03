from typing import Any
from update import Update
from configuration import Configuration

class Process:
    def __init__(self):
        self.configuration: Configuration = Configuration()
        self.update: Update = Update()

    def process_server_starter(self):
        try:
            arguments: str = "#!/bin/bash\n"
            configs: Any = self.configuration.get_server_starter_settings()
            for tag in configs:
                arguments += str(configs[tag])
            arguments += "\n"
            self.update.update_server_starter(arguments)
            print("server_starter.sh updated.")
        except:
            raise Exception("Could not process server_starter.")

    def process_game_settings(self):
        try:
            arguments: str = "[/script/shootergame.shootergamemode]\n"
            configs: Any = self.configuration.get_game_settings()
            for tag in configs:
                arguments += str("{0}={1}\n".format(tag,configs[tag]))
            self.update.update_game_settings(arguments)
            print("Game.ini updated.")
        except:
            raise Exception("Could not process game_settings.")

    def process_game_user_settings(self):
        try:
            arguments: str = "[ServerSettings]\n"
            configs: Any = self.configuration.get_game_user_settings()
            for tag in configs:
                arguments += str("{0}={1}\n".format(tag,configs[tag]))
            arguments += "\n"
            base_game_user_settings_lines = (
                self.configuration.get_base_game_user_settings()
            )
            for line in base_game_user_settings_lines:
                arguments += str("{0}\n".format(line))
            self.update.update_game_user_settings(arguments)
            print("GameUserSettings.ini updated.")
        except:
            raise Exception("Could not process game_user_settings.")

    def update_all(self):
        print("\n---------------")
        print("Starting Update.\n")
        self.process_server_starter()
        self.process_game_settings()
        self.process_game_user_settings()
        print("\nUpdate finished")
        print("---------------\n")