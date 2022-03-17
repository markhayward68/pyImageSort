#
# Name: pyMTImageSort.py
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
# import re 
import multiprocessing 
import pytesseract

# CPUCOUNT = multiprocessing.cpu_count() / 2 
CPUCOUNT = 2 
processCount = 0 
jobs = [] 


def OCRImage(i, fn): 
    print("Process " + str(i + 1) + ":Output " + fn)
    # output = pytesseract.image_to_string(fn)

    with open(fn + ".txt", 'w') as f:
        # f.writelines(output)
        f.writelines("Process " + str(i + 1) + ":Output " + fn)


if __name__ == '__main__': 
    directory = os.getcwd()

    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            if filename.endswith(".jpg"):
                try:  
                    f.open(filename + ".txt") 

                    # do nothing... must be better way than this... 

                    f.close()
                except: 
                    # imageNumber = os.path.splitext(filename)[0] - removes extension 
                    # imageNumber = re.search(r'\d+', filename).group(0) # returns number in filename  

                    if processCount in range(CPUCOUNT):
                        p = multiprocessing.Process(target=OCRImage, args = (processCount, filename)) 
                        
                        jobs.append(p)

                        p.start() 