import os
import threading
import pythoncom
import time
import win32com.client

# This version literally uses IE itself, opening it in a new window and deleting its cookies. This is not a very
# good program, it's mostly just for my personal use.

# Every 10 seconds, run a batch file that nukes Internet Explorer's cookies. Efficiency!
def clear_cookies():
    global thread_loop
    while thread_loop:
        time.sleep(10)
        os.system('.\cookies.bat')


thread_loop = True
cwd = os.getcwd()
splash = (cwd+'\Splash\index.html')

os.system('.\cookies.bat')
threading.Thread(target=clear_cookies).start()

ie = win32com.client.Dispatch("InternetExplorer.Application")
ie.AddressBar = False
ie.Width, ie.Height = 900, 700
ie.Visible = 1
ie.Navigate(splash)

# Every 10 seconds, check to see if Internet Explorer is still running
while True:
    time.sleep(10)
    apps_in_use = []
    wmi=win32com.client.GetObject('winmgmts:')
    for p in wmi.InstancesOf('win32_process'):
        apps_in_use.append(p.name)
    if 'iexplore.exe' not in apps_in_use:
        thread_loop = False
        break
