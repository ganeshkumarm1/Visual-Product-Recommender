# -*- coding: utf-8 -*-
# @Author: GaNeShKuMaRm
# @Date:   2017-02-25 20:38:47
# @Last Modified by:   GaNeShKuMaRm
# @Last Modified time: 2017-02-25 20:51:27

import graphlab

baseURL = "Dataset_SFrame/image_data_with_deepfeatures/df-"
flag = True
for i in range(1, 4):
    temp_data = graphlab.SFrame(baseURL + str(i))
    if flag:
        image_data = temp_data
        flag = False
    else:
        image_data = image_data.append(temp_data)

image_data.save('Dataset_SFrame/image_data')
print "Completed!"