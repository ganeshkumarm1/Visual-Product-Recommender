# -*- coding: utf-8 -*-
# @Author: GaNeShKuMaRm
# @Date:   2017-02-08 16:36:45
# @Last Modified by:   GaNeShKuMaRm
# @Last Modified time: 2017-02-13 20:18:50

from flask import Flask, url_for, request
from flask_cors import CORS, cross_origin
import os
import imp

VPR = imp.load_source('VPR', 'api/VPR.py')

app = Flask('VPR_WEB_API')
cors = CORS(app)

@app.route('/')
def api_root():
    return 'Success'

@app.route('/search', methods=['POST'])
@cross_origin()
def search():
    image_name = VPR.save_image(request)
    coors = VPR.get_coors(request)
    crop_image = VPR.crop(image_name, coors)
    fetch_url = VPR.google_reverse(crop_image)
    VPR.delete_images(image_name, crop_image)
    return fetch_url

if __name__ == '__main__':
    app.run()