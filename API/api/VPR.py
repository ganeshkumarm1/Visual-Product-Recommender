# -*- coding: utf-8 -*-
# @Author: GaNeShKuMaRm
# @Date:   2017-02-08 16:43:06
# @Last Modified by:   GaNeShKuMaRm
# @Last Modified time: 2017-02-13 20:18:41

from PIL import Image
from werkzeug import secure_filename
import math
import requests
import webbrowser
import os
import uuid


def save_image(request):
    image = request.files['image']
    image_name = str(uuid.uuid4())
    temp = str(image.filename).split('.')
    ext = temp[len(temp) - 1]
    image_name = image_name + '.' + ext
    image.save(os.path.join(os.path.dirname(__file__), '../temp_images/'+ image_name))
    return image_name

def get_coors(request):
    coors = request.form
    rounded_coors = {}
    for coor in coors:
        rounded_coors[coor] = round(float(coors[coor]))
    return rounded_coors

def crop(filename, coors):
    x = coors['x']
    y = coors['y']
    w = coors['w']
    h = coors['h']
    img = Image.open(os.path.join(os.path.dirname(__file__), '../temp_images/'+ filename))
    img_crop = img.crop((x, y, x + w, y + h))
    img_crop.save(os.path.join(os.path.dirname(__file__), '../temp_images/'+'crop_' + filename))
    return 'crop_' + filename

def google_reverse(file_path):
    file_path = os.path.join(os.path.dirname(__file__), '../temp_images/'+file_path)
    search_url = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (file_path, open(file_path, 'rb')), 'image_content': ''}
    response = requests.post(search_url, files=multipart, allow_redirects=False)
    fetch_url = response.headers['Location']
    return fetch_url

def delete_images(original_image, crop_image):
    os.remove(os.path.join(os.path.dirname(__file__), '../temp_images/'+original_image))
    os.remove(os.path.join(os.path.dirname(__file__), '../temp_images/'+crop_image))
