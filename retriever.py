from sentence_transformers import SentenceTransformer
import numpy as np
from automation_functions import FUNCTIONS

model = SentenceTransformer("all-MiniLM-L6-v2")

function_descriptions = {
    "open_chrome": "Open Google Chrome browser",
    "open_calculator": "Open calculator application",
    "open_notepad": "Open Notepad text editor",
    "open_cmd": "Open command prompt",
    "open_task_manager": "Open task manager",
    "open_control_panel": "Open control panel",
    "open_file_explorer": "Open file explorer",
    "get_cpu_usage": "Retrieve current CPU usage percentage",
    "get_ram_usage": "Retrieve current RAM usage percentage",
    "get_disk_usage": "Retrieve current disk usage percentage",
    "wait_5_seconds": "Pause execution for 5 seconds",
    "get_current_time": "Retrieve the current system time",
    "get_system_info": "Get system details including CPU, RAM, and Disk usage",
    "create_folder": "Create a new folder",
    "delete_folder": "Delete an existing folder",
    "list_files": "List all files in a directory",
    "create_text_file": "Create a new text file",
    "delete_file": "Delete a specific file",
    "open_url": "Open a URL in the browser",
    "search_google": "Search Google with a specific query",
    "open_youtube": "Open YouTube",
    "open_gmail": "Open Gmail",
    "take_screenshot": "Take a screenshot and save it",
    "lock_system": "Lock the system",
    "shutdown_system": "Shutdown the system in 10 seconds",
    "restart_system": "Restart the system in 10 seconds",
    "empty_recycle_bin": "Empty the recycle bin",
    "list_running_processes": "List all running processes",
    "kill_process": "Terminate a specific process",
    "adjust_volume": "Adjust system volume level"
}

embeddings = {func: model.encode(desc) for func, desc in function_descriptions.items()}

def retrieve_function(prompt):
    prompt_embedding = model.encode(prompt)
    similarities = {func: np.dot(prompt_embedding, emb) for func, emb in embeddings.items()}
    best_match = max(similarities, key=similarities.get)
    
    if similarities[best_match] > 0.7:
        return best_match
    return None
