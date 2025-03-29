import os
import psutil
import time
import webbrowser
import subprocess
import shutil
from PIL import ImageGrab

def open_chrome():
    subprocess.run("start chrome", shell=True)

def open_calculator():
    subprocess.run("calc", shell=True)

def open_notepad():
    subprocess.run("notepad", shell=True)

def open_cmd():
    subprocess.run("cmd", shell=True)

def open_task_manager():
    subprocess.run("taskmgr", shell=True)

def open_control_panel():
    subprocess.run("control", shell=True)

def open_file_explorer():
    subprocess.run("explorer", shell=True)

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def get_ram_usage():
    return f"RAM Usage: {psutil.virtual_memory().percent}%"

def get_disk_usage():
    return f"Disk Usage: {psutil.disk_usage('/').percent}%"

def wait_5_seconds():
    time.sleep(5)
    return "Waited for 5 seconds."

def get_current_time():
    return f"Current Time: {time.ctime()}"

def get_system_info():
    return {
        "CPU": psutil.cpu_percent(),
        "RAM": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage('/').percent
    }

def create_folder(folder_name="NewFolder"):
    os.makedirs(folder_name, exist_ok=True)
    return f"Folder '{folder_name}' created."

def delete_folder(folder_name="NewFolder"):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        return f"Folder '{folder_name}' deleted."
    return "Folder not found."

def list_files(directory="."):
    return os.listdir(directory)

def create_text_file(filename="sample.txt", content="Hello, world!"):
    with open(filename, "w") as file:
        file.write(content)
    return f"File '{filename}' created."

def delete_file(filename="sample.txt"):
    if os.path.exists(filename):
        os.remove(filename)
        return f"File '{filename}' deleted."
    return "File not found."

def open_url(url="https://www.google.com"):
    webbrowser.open(url)
    return f"Opened {url} in browser."

def search_google(query="Python programming"):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searched for '{query}' on Google."

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_gmail():
    webbrowser.open("https://mail.google.com")

def take_screenshot(filename="screenshot.png"):
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    return f"Screenshot saved as {filename}."

def lock_system():
    subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)
    return "System locked."

def shutdown_system():
    subprocess.run("shutdown /s /t 10", shell=True)
    return "System will shut down in 10 seconds."

def restart_system():
    subprocess.run("shutdown /r /t 10", shell=True)
    return "System will restart in 10 seconds."

def empty_recycle_bin():
    subprocess.run("rd /s /q C:\\$Recycle.Bin", shell=True)
    return "Recycle Bin emptied."

def list_running_processes():
    return [p.info["name"] for p in psutil.process_iter(["name"])]

def kill_process(process_name="notepad.exe"):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == process_name:
            proc.kill()
            return f"Process '{process_name}' terminated."
    return "Process not found."

def adjust_volume(level=50):
    subprocess.run(f"nircmd.exe setsysvolume {level * 655.35}", shell=True)
    return f"Volume set to {level}%."

# Mapping functions to their names
FUNCTIONS = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "open_notepad": open_notepad,
    "open_cmd": open_cmd,
    "open_task_manager": open_task_manager,
    "open_control_panel": open_control_panel,
    "open_file_explorer": open_file_explorer,
    "get_cpu_usage": get_cpu_usage,
    "get_ram_usage": get_ram_usage,
    "get_disk_usage": get_disk_usage,
    "wait_5_seconds": wait_5_seconds,
    "get_current_time": get_current_time,
    "get_system_info": get_system_info,
    "create_folder": create_folder,
    "delete_folder": delete_folder,
    "list_files": list_files,
    "create_text_file": create_text_file,
    "delete_file": delete_file,
    "open_url": open_url,
    "search_google": search_google,
    "open_youtube": open_youtube,
    "open_gmail": open_gmail,
    "take_screenshot": take_screenshot,
    "lock_system": lock_system,
    "shutdown_system": shutdown_system,
    "restart_system": restart_system,
    "empty_recycle_bin": empty_recycle_bin,
    "list_running_processes": list_running_processes,
    "kill_process": kill_process,
    "adjust_volume": adjust_volume
}
