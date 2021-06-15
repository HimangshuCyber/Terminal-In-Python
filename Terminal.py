import subprocess
from subprocess import call
import os
import time
import platform
import socket
import webbrowser
import requests
import re
import threading
import random
import pyautogui
import keyboard
from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
while True:
         code = input('@Coding Fever $ ')
         if code == 'ipconfig':
                  print('DESKTOP: ' + host_name)
                  print('LOCAL IPS: ' + host_ip)
                  print('PUBLIC IPS: 49.37.36.7')
         if code == 'sudo-ping':
                  host = input('Enter website to ping: ')
                  number = input('Enter the amount of requests: ')

                  def ping(host):
                                    param = '-n' if platform.system().lower() == 'windows' else '-c'
                                    command = ['ping', param, number, host]
                                    return subprocess.call(command)
                  print(ping(host))

         if code == 'sudo execute-catfish':
                  time.sleep(2)
                  print('KILLER T IS WORKING..')
                  time.sleep(2)
                  print('KILLER T IS WORKING...')
                  time.sleep(2)
                  print("KILLER T IS WORKING....")
                  time.sleep(2)
                  webbrowser.open('https://www.grabify.link/')
         if code == 'cls':
                  os.system('cls')
         if code == 'KILL locate-ip':
                  webbrowser.open('https://ip-api.com/docs/api:json')
                  link = input('')
                  reponse = requests.get(link).json()
                  print(reponse)
         if code == 'Kill BRUTE':
                  character="0123456789abcdefghijklmnopqrstuvwxyz"
                  character_list = list(character)
                  password = pyautogui.password('Password you want to check: ')
                  guess_password=''
                  guesses = 0
                  passwo = 'h'
                  
                  while (guess_password != password):
                            guess_password=random.choices(character_list, k=len(password))
                            print('Checked ' + str(guess_password) + ' Trying next')
                            guessed = str(guess_password)
                            guesses = guesses + 1

                            if guess_password == list(password):
                                    print('PASSWORD GUESSED! TOOK ' + str(guesses) + ' GUESSES')
                                    if guesses > 100000:
                                            print('PASSWORD IS STRONG ENOUGH')
                                            print("HACKER WON'T TRY THIS HARD. ALTHOUGH IF HE DOES IT IS LIKELY TO BE HACKED")
                                            break
                                    else: 
                                            print('WEAK PASSWORD. VURNERABLE TO DICTIONARY ATTACKES')
                                            break
                                            f =open('C:/Users/Desktop/Passwords.txt', 'w+')
                                            f.writelines('Hey')
                                             

 

                            if keyboard.is_pressed("q") == True:
                                                           print('')
                                                           print("Process Stopped. Couldn't find " + str(password) + " Guesses: " + str(guesses) )
                                                           break

         if code == 'cls':
                  os.system('cls')
         if code == 'list':
                  dir_list = os.listdir(path)
                  print(dir_list)
         if code == 'list -a':
                  file = input('')
                  dir_list2 = os.listdir(file)
                  print(dir_list2)
         if code == 'nano-folder':
                  name = input('')
                  os.mkdir(name)
         if code == 'nano-file txt':
                  folder = input('Folder or path: ')
                  nome = input('')
                  def main():
                           f =open(folder + '/' + nome + '.txt', 'w+')



                  if __name__ == "__main__":
                           main()
         if code == 'nano r':
                  neme = input('')
                  os.remove(neme)
                  print('Successfully Deleted ' + neme)
         if code == 'wifi-lists':
                  time.sleep(2)
                  command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
                  profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
                  wifi_list = []
                  if len(profile_names) != 0:
                                        for name in profile_names:
                                                        wifi_profile = {}
                                                        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                                                        #    We use the regular expression to only look for the absent cases so we can ignore them.
                                                        if re.search("Security key           : Absent", profile_info):
                                                                continue
                                                        else:
                                                                #    Assign the ssid of the wifi profile to the dictionary.
                                                                wifi_profile["ssid"] = name
                                                                #    These cases aren't absent and we should run the 
                                                                #    "key=clear" command part to get the password.
                                                                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                                                                #    Again run the regular expression to capture the 
                                                                #    group after the : (which is the password).
                                                                password = re.search("Key Content            : (.*)\r", profile_info_pass)
                                                                #    Check if we found a password using the regular expression. 
                                                                #    Some wifi connections may not have passwords.
                                                                if password == None:
                                                                        wifi_profile["password"] = None
                                                                else:
                                                                        #    We assign the grouping (where the password is contained) that 
                                                                        #    we are interested in to the password key in the dictionary.
                                                                        wifi_profile["password"] = password[1]
                                                                        #    We append the wifi information to the variable wifi_list.
                                                                        wifi_list.append(wifi_profile) 

                                                                        for x in range(len(wifi_list)):
                                                                                print(wifi_list[x]) 
         if code == 'auto-click':
                if messagebox.askyesno('Hey there!', "Are you sure?") == True:
                                call(["C:/Users/Nilutpal/Downloads/AutoClickerShocker-Setup.exe"])
         if code == 'python3 HOIC.exe':
                call(["C:/Users/Nilutpal/Desktop/hoic2.1.exe"])
         if code == 'break':
                break
         if code == 'rap':
                print('Bap Boop Beep Boop Bap Bap Beep Boop Beep Bap.')
         if code == 'grab-ip':
                webbrowser.open('grabify.link')