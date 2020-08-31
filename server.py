import json,os,time

const_script_folder: str = ''
const_script_name: str = ''
const_server_config_file: str = ''

def load_config_files():
    global const_script_folder,const_script_name
    with open('config.json') as json_file:
        data = json.load(json_file)
        const_script_folder = data['script_location']
        const_script_name = data['script_name']

    global const_server_config_file
    with open('server_config.json') as json_file:
        data = json.load(json_file)
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

def process_server_config_file():
    with open(const_server_config_file, 'r') as file:
        for line in file:
            print(line)

if __name__ == "__main__" :
    try:
        load_config_files()
        #listen_commands()
        process_server_config_file()
    except:
        print("Deu ruim")