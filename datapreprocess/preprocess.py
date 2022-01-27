import os
from re import sub
import shutil
import random
import argparse
from sre_parse import SubPattern


class file_preprocess:
    def __init__(self, src_folder, dst_folder):
        self.src_folder = src_folder
        self.dst_folder = dst_folder
        self.file_list = os.listdir(src_folder)
    
    def create_folder(self):
        for file in self.file_list:
            if not (os.path.isdir(self.dst_folder + file.split('_')[0])):
                os.makedirs(os.path.join(self.dst_folder + file.split('_')[0]))
                
    def move_file_by_age(self):
        for file in self.file_list:
            shutil.move(self.src_folder + '/' + str(file), self.dst_folder + '/' + file.split('_')[0] + '/' + str(file))
        
        print('File move finished for {} files' .format(len(self.file_list)))
        shutil.rmtree(self.src_folder)
    
    def print_length_of_files_by_age(self):
        for file in self.file_list:
            path = self.src_folder + '/' + str(file)
            print(str(file) + ' have : ' + str(len(os.listdir(path))) + ' files. ')
            
    def merge_folder(self):
        for i in range(0,91,5):
            for j in range(i+1, i+5):
                sub_path = self.src_folder+'/'+str(j)
                print(sub_path)
                if os.path.isdir(self.src_folder+'/'+str(j)):
                    for files in os.listdir(sub_path):
                        shutil.move(self.src_folder+'/'+str(j)+'/'+ str(files), self.src_folder+'/'+str(i)+'/'+str(files))        
                    shutil.rmtree(self.src_folder+'/'+str(j)+'/')
        print('merge finish')
        
    def random_remove(self, num):
        random_files = random.sample(self.file_list, num)

        for file in random_files:
            os.remove(self.src_folder+'/'+str(file))

        print('{} random files removed'.format(num))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_path', type=str, help='enter your src path')
    parser.add_argument('--dst_path', type=str, help='enter your dst path')
    parser.add_argument('--random_num', type=int, default=0, help='enter random remove num')
    parser.add_argument('--create_folder', default=False, action='store_true', help='create folder by age')
    parser.add_argument('--move_files', default=False, action='store_true', help='move files')
    parser.add_argument('--merge_files', default=False, action='store_true', help='merge files')
    parser.add_argument('--random_remove', default=False, action='store_true', help='random remove files')
    parser.add_argument('--print_length', default=False, action='store_true', help='print lengths')
    opt = parser.parse_args()

    src_path = opt.src_path
    dst_path = opt.dst_path
    num = opt.random_num

    preprocess = file_preprocess(src_path, dst_path)

    if opt.create_folder is True:
        preprocess.create_folder()
    
    if opt.move_files is True:
        preprocess.move_file_by_age()
    
    if opt.print_length is True:
        preprocess.print_length_of_files_by_age()
    
    if opt.merge_files is True:
        preprocess.merge_folder()
    
    if opt.random_remove is True:
        preprocess.random_remove(num)