#!/usr/bin/env python3

import os
import json
import requests

path = "suppliers-data/descriptions/"
img_path = "suppliers-data/images/"
#url = "http://localhost/fruits"

path_dir = os.listdir(path)
fruit_dict = {}

for text in path_dir:
  if text.endswith("txt"):
    image_name = text.split(".")[0]
    with open(path+text, "r") as textfile:
      data = textfile.read()
      data = data.split("\n")
      fruit_dict = {"name" : data[0], "Weight" : int(data[1].strip("lbs")), "Description" : data[2], "image_name" : image_name + ".jpeg"} 


"""files = os.listdir(path)
for file in files:
  if file.endswith("txt"):
    with open(path + file, 'r') as f:
    #grab the file name, ex. 001, 002 to use for image file
      fruit_name = os.path.splitext(file)[0]
      data = f.read()
      data = data.split("\n")
      fruit_dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2] }    
  print(fruit_dic)"""
