import os
import shutil
import PIL
from PIL import Image

base_folder = '../Dataset/Original'
sub_folders = ['hat', 'shoe', 'watch']

def get_files(path):
    return os.listdir(path)

def rename_images(images, sub_folder):
    base = 1
    path = base_folder + '/' + sub_folder
    for image in images:
        ext = image.split('.')[1]
        renamed_image = path + '/' + sub_folder + '_' + str(base) + '.' + ext
        old_image = path + '/' + image
        shutil.move(old_image, renamed_image)
        base += 1
    print "Renamed " + sub_folder

def resize_image(image, path, sub_folder):
    file_path = os.path.join(path, image)
    img = Image.open(file_path)
    img = img.resize((32, 32), Image.ANTIALIAS)
    if not os.path.exists('../Dataset/Resized/' + sub_folder):
        os.makedirs('../Dataset/Resized/' + sub_folder)
    new_path = os.path.join('../Dataset/Resized/' + sub_folder + '/', image)
    #img.save(new_path)

def main():
    for sub_folder in sub_folders:
        path = base_folder + '/' + sub_folder
        images = get_files(path)
        rename_images(images, sub_folder)
        images = get_files(path)
        for image in images:
            resize_image(image, path, sub_folder)
        print "Resized " + sub_folder

main()