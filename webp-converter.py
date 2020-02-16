from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

from subprocess import check_output
import os

Tk().withdraw()

webp_string = askopenfilename(title="Select cwebp.exe")
input_folder = askdirectory(title="Select the input folder")
webp_output_dir = askdirectory(title="Select the output folder")
directory = os.fsencode(input_folder)

webp_string +=  " -q 80 "
input_folder += "\\"
webp_output_dir += "\\"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".png"): 
        command_string = webp_string + "\"" + input_folder + filename + "\"" + " -o " + "\"" + webp_output_dir + filename[:-3] + "webp" + "\""
        #print(command_string)
        print (check_output(command_string, shell=True).decode())
        continue
    elif filename.endswith(".jpg"):
        command_string = webp_string + "\"" + input_folder + filename + "\"" + " -o " + "\"" + webp_output_dir + filename[:-3] + "webp" + "\""
        #print(command_string)
        print (check_output(command_string, shell=True).decode())
        continue
    else:
        continue

