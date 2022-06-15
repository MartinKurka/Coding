import os
import subprocess as sp

def main():
    while True:
        name = input("\nEnter your command: ")
        if name == "info":
            # os.system('cd C:\\users\\martin.kurka\\Documents\\githu\\Coding\\System info')
            # os.system('informations.py')
            output = sp.getoutput('python3.8 informations.py')
            print(output)

if __name__ == "__main__":
    main()