import sys
import subprocess
from subprocess import Popen, PIPE
import random

def gfx():
    print("""
        ███▄    █  ███▄ ▄███▓ ▄▄▄       ██▓███       █████▒▒█████   ██▀███          
        ██ ▀█   █ ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒   ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒        
        ▓██  ▀█ ██▒▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒   ▒████ ░▒██░  ██▒▓██ ░▄█ ▒        
        ▓██▒  ▐▌██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒   ░▓█▒  ░▒██   ██░▒██▀▀█▄          
        ▒██░   ▓██░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░   ░▒█░   ░ ████▓▒░░██▓ ▒██▒        
        ░ ▒░   ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░    ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░        
        ░ ░░   ░ ▒░░  ░      ░  ▒   ▒▒ ░░▒ ░         ░       ░ ▒ ▒░   ░▒ ░ ▒░        
        ░   ░ ░ ░      ░     ░   ▒   ░░           ░ ░   ░ ░ ░ ▒    ░░   ░         
                ░        ░         ░  ░                       ░ ░     ░             
                                                                                    
        ██▓    ▄▄▄      ▒███████▒▓██   ██▓     ██████  ██░ ██  ██▓▄▄▄█████▓  ██████ 
        ▓██▒   ▒████▄    ▒ ▒ ▒ ▄▀░ ▒██  ██▒   ▒██    ▒ ▓██░ ██▒▓██▒▓  ██▒ ▓▒▒██    ▒ 
        ▒██░   ▒██  ▀█▄  ░ ▒ ▄▀▒░   ▒██ ██░   ░ ▓██▄   ▒██▀▀██░▒██▒▒ ▓██░ ▒░░ ▓██▄   
        ▒██░   ░██▄▄▄▄██   ▄▀▒   ░  ░ ▐██▓░     ▒   ██▒░▓█ ░██ ░██░░ ▓██▓ ░   ▒   ██▒
        ░██████▒▓█   ▓██▒▒███████▒  ░ ██▒▓░   ▒██████▒▒░▓█▒░██▓░██░  ▒██▒ ░ ▒██████▒▒
        ░ ▒░▓  ░▒▒   ▓▒█░░▒▒ ▓░▒░▒   ██▒▒▒    ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
        ░ ░ ▒  ░ ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▓██ ░▒░    ░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░    ░    ░ ░▒  ░ ░
        ░ ░    ░   ▒   ░ ░ ░ ░ ░ ▒ ▒ ░░     ░  ░  ░   ░  ░░ ░ ▒ ░  ░      ░  ░  ░  
            ░  ░     ░  ░  ░ ░     ░ ░              ░   ░  ░  ░ ░                 ░  
                        ░         ░ ░                                               
                            A script nobody asked for 
                                by Hev (a lazy shit)

        """)


def options():

    nmap_command = ['sudo', 'nmap', '-A', '-sS', '-sV', '-O', '-sU', '0.0.0.0', '-p', '00']

    ip = input("Enter an IP Address: ")
    nmap_command[7] = ip

    port = input("Enter a port or port range: ")
    nmap_command[9] = port

    input_check = False
    while input_check == False:
        aggro = input("Would you like to perform an aggressive scan? (warning: loud) y/n: ")
        if aggro == "y":
            nmap_command.remove('-sS')
            nmap_command.remove('-O')
            nmap_command.remove('-sV')
            while input_check == False:
                udp_input = input("Would you like to scan UDP ports? y/n: ")
                if udp_input == "y":
                    input_check = True
                elif udp_input == "n":
                    nmap_command.remove('-sU')
                    input_check = True
                else:
                    print("Invalid Command")
        elif aggro == "n": 
            nmap_command.remove('-A')
            while input_check == False:
                sv_input = input("SYN scan? (stealthy) y/n: ")
                if sv_input == "y":
                    input_check = True
                elif sv_input == "n":
                    nmap_command.remove('-sS')
                    input_check = True
                else:
                    print("Invalid Command")

            input_check = False
            while input_check == False:
                os_input = input("Would you like to detect operating systems? y/n: ")
                if os_input == "y":
                    input_check = True
                elif os_input == "n": 
                    nmap_command.remove('-O')
                    input_check = True
                else:
                    print("Invalid Command")

            input_check = False
            while input_check == False:
                ss_input = input("Would you like to detect software versions? y/n: ")
                if ss_input == "y":
                    input_check = True
                elif ss_input == "n":
                    nmap_command.remove('-sV')
                    input_check = True
                else:
                    print("Invalid Command")

            input_check = False
            while input_check == False:
                udp_input = input("Would you like to scan UDP ports? y/n: ")
                if udp_input == "y":
                    input_check = True
                elif udp_input == "n":
                    nmap_command.remove('-sU')
                    input_check = True
                else:
                    print("Invalid Command")

        else:
            print("Invalid Command")       

    execute(nmap_command)

def execute(nmap_command):
    print(f'You are running the following command: {nmap_command}')
    exe_check = input ("Would you to execute this? y/n: ")
    if exe_check == "y":
        process = Popen(nmap_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode())
    else:
        exit_msg = ["Please don't leave, there's more demons to toast!", "Let's beat it -- This is turning into a bloodbath! ", "You're trying to say you like terminal better than me, right?", "Don't leave yet, there's a demon around that corner!", "Don't go now, there's a dimensional shambler waiting at the shell prompt!", "Get outta here and go back to your boring programs", "Look bud, you leave now and you forfeit your body count."]
        random_msg = random.choice(exit_msg)
        print(random_msg)
        input("Press any key to quit")
        

gfx()
options()