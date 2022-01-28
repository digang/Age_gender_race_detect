from distutils import filelist
from fileinput import filelineno
import os
import shutil
import random
import os.path

src_dir = '../labels/train/'
target_dir = '../labels/val/'
src_files = (os.listdir(src_dir))

train_folders = os.listdir(src_dir)
for folder in train_folders:
    folder_dir = os.path.join(src_dir, folder)
    if os.path.isdir(folder_dir):
        os.makedirs(os.path.join(target_dir,folder))
        file_list = os.listdir(folder_dir)
        choices = random.sample(file_list, int(len(file_list) * 0.1))
        for file in choices:
            shutil.move(os.path.join(src_dir + '/' + folder + '/',file), target_dir + '/' + folder +'/' +file)

print('finished ! ')