import json,os

const_script_folder: str = ''
const_script_name: str = ''

def load_config_files():
    global const_script_folder,const_script_name
    with open('config.json') as json_file:
        data = json.load(json_file)
        const_script_folder = data['script_location']
        const_script_name = data['script_name']

def run_server():
    command = const_script_folder + "./" + const_script_name
    os.system(command)

if __name__ == "__main__" :
    try:
        load_config_files()
        run_server()
    except:
        print("Deu ruim")