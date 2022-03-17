#
# Name: pyImageSortMT.py
#
# Date 18/02/2022
#
# Description: Takes image(s) and extracts text for later processing... 
# add multithreading... or multiprocessing, whichever works best really 
#
# Requirements: sudo apt install tesseract-ocr
# cmd line: tesseract image_path text_result.txt -l eng --psm 6
#
 
import os
import re 
import multiprocessing 
import pytesseract

# cpuCount = multiprocessing.cpu_count() / 2
cpuCount = 2 
processCount = 0 

directory = os.getcwd()

for filename in os.listdir(directory):
    if os.path.isfile(filename):
        if filename.endswith(".jpg"):
            if processCount < cpuCount:
                try:  
                    f.open(filename + ".txt") 
                except: 
                    # imageNumber = os.path.splitext(filename)[0] - removes extension 
                    imageNumber = re.search(r'\d+', filename).group(0) 

                    if (int(imageNumber) % 2) == 0: 
                        # process 1
                        output = pytesseract.image_to_string(filename)

                        with open(filename + ".txt", 'w') as f:
                            f.writelines(output) 
                        
                            processCount-= 1
                    else: 
                        # process 2
                        output = pytesseract.image_to_string(filename)

                        with open(filename + ".txt", 'w') as f:
                            f.writelines(output) 
                        
                            processCount-= 1                    