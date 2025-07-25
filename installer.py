import time
import subprocess
import requests
import os
import webbrowser

afterrec = """
(if phone doesn't rebooted to recovry, do it yourself (Volume Up + Power Button)
Now you need to wipe all data. To do this, select Factory reset > Format data/factory reset.
Note for beginners: This will erase all your data — the phone will be completely wiped!
Next, select Format cache partition and Format system partition.
Now it's time for the actual installation.
In recovery, choose Apply update > Update from ADB.
"""

url = "https://github.com/yaragirodev/EvolutionX-dipper-installer/releases/download/files/recovery.img"
script_dir = os.path.dirname(os.path.abspath(__file__))
recovery_path = os.path.join(script_dir, "recovery.img")
firm_path = os.path.join(script_dir, "evoX.zip")

print("Do you want to download EvolutionX recovery and system?")
yesno = input("Y/N - ")

if yesno.lower() == "y":
    filename = url.split("/")[-1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    print("Downloading recovery image...")
    response = requests.get(url)
    
    with open(filepath, "wb") as f:
        f.write(response.content)
    
    print(f"Downloaded to: {filepath}")
    time.sleep(1)
    webbrowser.open("https://drive.google.com/file/d/1HcWgaafeCxwMWP1CNYIPxu70rJlZiWPF/view")
    input("Please, install it yourself and put in folder wih script, after it press ENTER.")
    time.sleep(1)
    subprocess.run(['fastboot', 'flash', 'recovery', recovery_path])
    time.sleep(2)
    subprocess.run(['fastboot', 'reboot', 'recovery'])
    time.sleep(0.5)
    print(afterrec)
    input("after all press ENTER.")
    time.sleep(1)
    subprocess.run(['adb', 'sideload', firm_path])
    time.sleep(0.5)
    print("Done! Thx for using my programm! I hope i helped you!")
    input("PRESS ENTER TO EXIT")

if yesno.lower() == "n":
    recpath = input("Your Recovery Path (you can just drop file into cmd) - ")
    firmpath = input("Your firmware (.zip) path - ")
    time.sleep(1)
    subprocess.run(['fastboot', 'flash', 'recovery', recpath])
    time.sleep(2)
    subprocess.run(['fastboot', 'reboot', 'recovery'])
    time.sleep(0.5)
    print(afterrec)
    input("after all press ENTER.")
    time.sleep(1)
    subprocess.run(['adb', 'sideload', firmpath])
    time.sleep(0.5)
    print("Done! Now you can reboot to system! Thx for using my programm! I hope i helped you!")
    input("PRESS ENTER TO EXIT")