# pyImageSort - OCR and sort images

Python project for sorting digitised images using OCR etc. Ultimately the intention is to run this in a docker container but this is only the start so there is not much to see yet... oh, and the logic is wrong. It works, just not the way it is supposed to. 

https://hub.docker.com/r/clearlinux/tesseract-ocr or https://hub.docker.com/r/tensorflow/tensorflow 

Tensorflow is probably better as it runs as a simple command shell... Eventually, build a bespoke container using alpine Linux etc. 

First run 'sudo apt install tesseract-ocr' then...

# pip installer 
sudo apt install pip or sudo apk add py3-pip 
pip install --upgrade pip
pip install <package>  
Make sure to run 'pip install pytesseract' NOT 'tesseract' 
  
pip freeze > requirements.txt 
pip install -r requirements.txt 

Run 'python3 pyImageSort.py' from directory with images. 

grep -i '<search term>' <files>
The -i ignores the case of the strings, also use '<term1 >\|<term 2>\|...' for multiple serach terms.
