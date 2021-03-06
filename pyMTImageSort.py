#!/usr/bin/env python3
# 
# Name: pyMTImageSort.py
#
# Date 17/03/2022
#
# Description: Takes image(s) and extracts text for later processing... 
# add multithreading... or multiprocessing, whichever works best really 
# intention is to run it all in a docker container 
#  
# https://hub.docker.com/r/clearlinux/tesseract-ocr 
# https://hub.docker.com/r/tensorflow/tensorflow 
#
# Requirements: pip install tesseract 
# cmd line: tesseract image_path text_result.txt -l eng --psm 6

import os
import multiprocessing 
import pytesseract

# CPUCOUNT = int(multiprocessing.cpu_count()) / 2
CPUCOUNT = 2 
processCount = 0 
jobs = [] 

def OCRImage(i, fn): 
    output = pytesseract.image_to_string(fn)

    with open(fn + ".txt", 'w') as f:
        f.writelines(output)

if __name__ == '__main__': 
    directory = os.getcwd()

    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            if filename.endswith(".jpg"):
                if os.path.isfile(filename + ".txt"):  
                    pass
                else: 
                    if processCount in range(CPUCOUNT):
                        p = multiprocessing.Process(target = OCRImage, args = (processCount, filename))                         
                        jobs.append(p)
                        p.start() 
