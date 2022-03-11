#
# Name: pyImageSortMT.py
#
# Date 18/02/2022
#
# Description: Takes image(s) and extracts text for later processing... 
# add multithreading... or multiprocessing, whichever works best really 
#
# Requirements: sudo apt install tesseract-ocr
# cmd line example: tesseract image_path text_result.txt -l eng --psm 6
#
 
import os
import multiprocessing 
import pytesseract

cpuCount = multiprocessing.cpu_count()
threadCount = cpuCount / 2

directory = os.getcwd()

for filename in os.listdir(directory):
   if os.path.isfile(filename):
       if filename.endswith(".jpg"):
           # do mutlithreading... 
           output = pytesseract.image_to_string(filename)
          
           with open(filename + ".txt", 'w') as f:
               f.writelines(output) 
