import os
import graphlab
import numpy as np
from PIL import Image

image_dir = '../Dataset/Resized/'
image_sarray = graphlab.image_analysis.load_images(image_dir, 'auto', with_path=True, recursive=True)
image_sarray.add_column(graphlab.SArray([iid + 1 for iid in range(0, len(image_sarray))]), name='id')
image_sarray.add_column(graphlab.SArray([image_sarray['path'][i].split('/')[-1].split('_')[0] for i in range(0, len(image_sarray))]), name='label')
image_array = []
for path in image_sarray['path']:
    img = Image.open(path)
    try:
        data = np.asarray( img, dtype='uint8' )
        flat = data.flatten()
        image_array.append(flat)
    except SystemError:
        data = np.asarray( img.getdata(), dtype='uint8' )
        image_array.append(data)
image_sarray.add_column(graphlab.SArray(image_array), name="image_array")
#image_sarray.remove_column('path')
image_sarray.save('../Dataset_SFrame/image_data_without_deepfeatures')