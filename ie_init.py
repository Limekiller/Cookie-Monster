import webview
import win32inet
import os, subprocess
import threading

os.system('.\cookies.cmd')

def clear_cookies():
    global thread_loop
    while thread_loop:
        time.sleep(10)
        subprocess.call(".\psexec64.exe -l c:\windows\system32\RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 271")


thread_loop = True
cwd = os.getcwd()
splash = (cwd+'\Splash\index.html')
webview.create_window("Cookie Monster", splash, width=900, height=700)
thread_loop = False