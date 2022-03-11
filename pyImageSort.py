#
# Name: pyImageSort.py
#
# Date 18/02/2022
#
# Description: Takes image(s) and extracts text for later processing...
#
# Requirements: sudo apt install tesseract-ocr
# cmd line example: tesseract image_path text_result.txt -l eng --psm 6
#
 
import os
import pytesseract
 
directory = os.getcwd()
 
for filename in os.listdir(directory):
   if os.path.isfile(filename):
       if filename.endswith(".jpg"):
           output = pytesseract.image_to_string(filename)
          
           with open(filename + ".txt", 'w') as f:
               f.writelines(output) 