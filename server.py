import json,os,threading

const_script_folder: str = ''
const_script_name: str = ''

def load_config_files():
    global const_script_folder,const_script_name
    with open('config.json') as json_file:
        data = json.load(json_file)
        const_script_folder = data['script_location']
        const_script_name = data['script_name']

def run_server():
    command: str = const_script_folder + "./" + const_script_name + "& "
    os.system(command)

def stop_server():
    command: str = "pkill ShooterGameServer"
    os.system(command)

def listen_commands():
    while(True):
        command = input("Digite o comando:")
        if(command == "run"):
            run_server()
        elif(command == "stop"):
            stop_server()


if __name__ == "__main__" :
    try:
        load_config_files()
        listen_commands()
    except:
        print("Deu ruim")