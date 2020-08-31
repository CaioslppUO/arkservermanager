import json,os,time

const_script_folder: str = ''
const_script_name: str = ''
const_server_config_file: str = ''
const_game_config_file: str = ''
const_base_server_config_file: str = "./base_server_config.ini"
const_server_configs = None
const_game_configs = None
const_starter_configs = None

def load_config_files():
    global const_script_folder,const_script_name
    with open('config.json') as json_file:
        data = json.load(json_file)
        const_script_folder = data['script_location']
        const_script_name = data['script_name']

    global const_server_config_file,const_server_configs
    with open('server_config.json') as json_file:
        data = json.load(json_file)
        const_server_configs = data
        const_server_config_file = data['server_config_file']

    global const_game_configs,const_game_config_file
    with open('game_config.json') as json_file:
        data = json.load(json_file)
        const_game_configs = data
        const_game_config_file = data['game_config_file']

    global const_starter_configs
    with open('starter_config.json') as json_file:
        data = json.load(json_file)
        const_starter_configs = data

def run_server():
    command: str = const_script_folder + "./" + const_script_name + "& "
    os.system(command)

def stop_server():
    command: str = "killall ShooterGameServer"
    os.system(command)
    time.sleep(4)
    command: str = "killall ShooterGameServer"
    os.system(command)
    time.sleep(4)

def listen_commands():
    command: str = input("Digite o comando:")
    while(True):
        if(command == "run"):
            run_server()
        elif(command == "stop"):
            stop_server()
        elif(command == "update"):
            stop_server()
            process_server_config_file()
            process_game_config_file()
            process_starter_config()
        command: str = input("Digite o comando:")

def set_server_configs():
    command: str = ""
    for tag in const_server_configs:
        if(tag != "server_config_file"):
            command += (str(tag + "=" + const_server_configs[tag] + "\n"))
    return command

def write_server_config_file(file_content):
    with open(const_server_config_file, 'w') as file:
        file.write(file_content)
    
def process_server_config_file():
    command: str = ""
    flag = True
    with open(const_base_server_config_file, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            command += (line + "\n")
            if(line == "[ServerSettings]"):
                flag = False
            if(line == ""):
                flag = True
            if(flag == True):
                command += set_server_configs()
                flag = False
    if(command != ""):
        write_server_config_file(command)

def set_game_configs():
    command: str = ""
    for tag in const_game_configs:
        if(tag != "game_config_file"):
            command += (str(tag + "=" + const_game_configs[tag] + "\n"))
    return command

def write_game_config_file(file_content: str):
    with open(const_game_config_file, 'w') as file:
        file.write(file_content)

def process_game_config_file():
    command: str = "[/script/shootergame.shootergamemode]\n"
    command += set_game_configs()
    if(command != ""):
        write_game_config_file(command)

def process_starter_config():
    command = ""
    for tag in const_starter_configs:
        command += str(const_starter_configs[tag] + "\n")
    with open(const_script_folder + const_script_name, 'w') as file:
        file.write(command)

if __name__ == "__main__" :
    try:
        load_config_files()
        listen_commands()
    except:
        print("Deu ruim")