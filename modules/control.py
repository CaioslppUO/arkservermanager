from configuration import Configuration
from process import Process
import os,time

class Control:
    def __init__(self):
        self.configuration = Configuration()

    def run(self):
        command: str = "{0}./{1}& ".format(
            self.configuration.files_locations['server_start_location'],
            self.configuration.files_locations['server_start_name']
        )
        print("\n")
        os.system(command)

    def stop(self):
        command: str = "killall ShooterGameServer"
        os.system(command)
        time.sleep(4)
        os.system(command)
        time.sleep(2)
        print("\n")

    def update(self):
        self.stop()
        Process().update_all()
        print("\n")

    def listen_commands(self):
        command: str = input(":")
        try:
            while(True):
                if(command == "run"):
                    self.run()
                elif(command == "stop"):
                    self.stop()
                elif(command == "update"):
                    self.update()
                else:
                    print("Invalid command.")
                time.sleep(5)
                command = input(":")
        except:
            raise

if __name__ == "__main__":
    try:
        Control().listen_commands()
    except Exception as e:
        print(e)