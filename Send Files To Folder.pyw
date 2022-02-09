import sys
import os
from tkinter import *
from tkinter.simpledialog import askstring
import shutil
import winsound

def main():


    root = Tk()
    root.withdraw()
    prompt = askstring("", "Name For Folder?")
    
    files = sys.argv
    files = files[1:]

    files_path = os.path.dirname(files[0])

    folder_name = (prompt)

    path = os.path.join(files_path, folder_name)
    
    os.mkdir(path)

    for items in files:
        shutil.move(items, path)
    
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    
    exit()

    #root.mainloop()

    

    




if __name__ == "__main__":
    main()