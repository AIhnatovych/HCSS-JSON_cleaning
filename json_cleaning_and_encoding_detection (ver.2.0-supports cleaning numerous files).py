# -*- coding: utf-8 -*-

import json 
import re
import chardet
from os import listdir
from os.path import isfile, join

file_json = "/hypersonics177.json"

list_of_file = [f for f in listdir(path_files) if isfile( join(path_files, f)) and f[-1:-5]=='.json']
print(list_of_file)

def detect_file_encodind (file_name):
    rawdata = open(file_name, "rb").read()
    result = chardet.detect(rawdata)
    return result['encoding']
 

def clean_json_file (file_name, enc):
  with open(file_name, 'r', encoding=enc) as f:
      s = re.sub(r'[^A-Za-zА-Яа-я0-9./"{}()\'\;\?\!#@%^&\*\+\$№,-=\[\]]', ' ', f.read())
  with open(file_name, 'w') as f:
    f.write(s)
  return json.loads(s)

enc = detect_file_encodind(file_json)
print(enc)
print(clean_json_file(file_json,enc))

