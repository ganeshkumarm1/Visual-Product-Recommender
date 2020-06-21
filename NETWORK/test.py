# -*- coding: utf-8 -*-
# @Author: GaNeShKuMaRm
# @Date:   2017-02-24 13:38:32
# @Last Modified by:   GaNeShKuMaRm
# @Last Modified time: 2017-02-26 10:44:52

import graphlab
import os
from PIL import Image
image_data = graphlab.SFrame("Dataset_SFrame/image_data")
image_train, image_test = image_data.random_split(.9, seed=5)
print image_test
sample = image_test[18:19]
print sample['path']
knn_model = graphlab.nearest_neighbors.create(image_train,features=["deep_features"],label="path")
result = knn_model.query(sample)
print result[0]['reference_label']
print result[1]['reference_label']
print result[2]['reference_label']
print result[3]['reference_label']
print result[4]['reference_label']
