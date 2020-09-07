# -*- coding: utf-8 -*-
"""Created for Hypersonic HCSS project
"""

import json 
import re
import chardet

file_json = "/hypersonics177.json"

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

