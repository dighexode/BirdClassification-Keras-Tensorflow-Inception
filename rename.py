import os
from argparse import ArgumentParser

if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('source_folder', help='input the source folder path')
    args = argparser.parse_args()
    source_folder = args.source_folder
    index = 0
    for root_folder1, sub_folder1, file_list1 in os.walk(source_folder):
        for file_name1 in file_list1:
            source_file_path = root_folder1 + os.sep + file_name1
            destination_file_path = root_folder1 + os.sep + 'other_' + str(index) + '.jpg'
            if source_file_path.find('jpg') > -1:
                os.rename(source_file_path, destination_file_path)
                index += 1