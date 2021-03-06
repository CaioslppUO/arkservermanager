#!/usr/bin/python3
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
        print("Server Running")
        print("\n")
        os.system(command)

    def stop(self):
        print("\n---------------")
        print("Stopping server.\n")
        command: str = "killall ShooterGameServer"
        while(str(os.system(command)) != "256"):
            os.system(command)
        print("\nServer stopped.")
        print("---------------\n")

    def update(self):
        print("\n---------------")
        print("Starting Update.\n")
        self.stop()
        Process().update_all()
        print("\nUpdate finished")
        print("---------------\n")

    def listen_commands(self):
        command: str = input("~ :")
        try:
            while(True):
                os.system("clear")
                print("Commands: run,update,stop,exit\n")
                if(command == "run"):
                    self.run()
                elif(command == "stop"):
                    self.stop()
                elif(command == "update"):
                    self.update()
                elif(command == "exit"):
                    self.stop()
                    exit(0)
                else:
                    print("Invalid command.")
                time.sleep(5)
                command = input("~ :")
        except:
            raise

if __name__ == "__main__":
    try:
        Control().listen_commands()
    except Exception as e:
        print(e)
