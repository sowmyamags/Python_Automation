#!/usr/bin/env python3

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

path = "suppliers-data/images/"
image_dir = os.listdir(path)

for image in image_dir:
  if image.endswith(".jpeg"):
    picture = path + image
    with open(picture, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
