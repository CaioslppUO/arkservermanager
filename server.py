import json,os,time

const_script_folder: str = ''
const_script_name: str = ''
const_server_config_file: str = ''
const_server_configs = None

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

def run_server():
    command: str = const_script_folder + "./" + const_script_name + "& "
    os.system(command)

def stop_server():
    command: str = "killall ShooterGameServer"
    os.system(command)

def listen_commands():
    command: str = input("Digite o comando:")
    while(True):
        if(command == "run"):
            run_server()
        elif(command == "stop"):
            stop_server()
            time.sleep(4)
            stop_server()
            time.sleep(4)
        command: str = input("Digite o comando:")

def set_server_configs():
    command: str = ""
    command += str("XPMultiplier=" + const_server_configs['XPMultiplier'] + "\n")
    return command

def write_server_config_file(file_content):
    with open(const_server_config_file, 'w') as file:
        file.write(file_content)

def process_server_config_file():
    command = ""
    flag = True
    with open(const_server_config_file, 'r') as file:
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

if __name__ == "__main__" :
    try:
        load_config_files()
        #listen_commands()
        process_server_config_file()
    except:
        print("Deu ruim")