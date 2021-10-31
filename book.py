from typing import KeysView
import urllib
import requests
import string
import os.path
from bs4 import BeautifulSoup

newtextfile = 'data/Alice.txt'

def make_txt(site):
    url = urllib.request.urlopen(site)
    html = url.read()

    pulled = BeautifulSoup(html)

    new = pulled.decode('utf-8')
    str(new)
    with open(newtextfile, 'w', encoding='utf-8') as f:
        f.write(new)

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def punc(string):
    punc = '''!()-[];:'"\,<>./?@#$%^&*_~'''
    for q in string:  
        if q in punc:  
            string = string.replace(q, "") 
    return string

def punc2(file_name):
    with open(newtextfile,'r',encoding="utf-8") as f:
        data = f.read()
    with open(newtextfile,"w+",encoding="utf-8") as f:
        f.write(punc(data))

def list(file):
    my_file = open("data/Alice.txt", "r", encoding='utf-8')
    content = my_file.read()
    content_list = content.split(" ")
    converted_list = []

    for element in content_list:
        converted_list.append(element.strip())
    return converted_list

def frequency(newlist):
    newdict = dict()
    for x in newlist:
        words = x.split(' ')
        for q in words:
            if q in newdict:
                newdict[q] += 1
            else:
                newdict[q] = 1
    for key in list(newdict.keys()):
        print(key, ':', newdict[key])
    return newdict

def top10(data, mostusedwords=True):
    return

def main():
    url = 'https://www.gutenberg.org/files/11/11-0.txt'
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    make_txt(url)
    editedtext = punc2(newtextfile)
    newlist = list(editedtext)
    finallist = frequency(newlist)
    best = top10(finallist, mostusedwords=True)
   
if __name__ == "__main__":
   main()


# I am so sorry, I cannot pull the top used words
# I was able to make a list of them but have spent
# too much time on figuring this out for tonight
# that I don't have any more time. I will try and 
# make it work the correct way by the end of the day
# tomorrow but as of now I am submitting my code as is
# (it's 12:30) and turning in my write up about it.
