import os
import subprocess


def get_current_dir():
    source = 'Source'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.join(current_dir, source)
    return current_dir


def get_result_dir():
    result = 'Result'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    result_dir = os.path.join(current_dir, result)
    try:
        os.mkdir(result_dir)
    except OSError:
        pass
    return result_dir


def get_jpg_list():
    jpg_list = []
    current_dir = get_current_dir()
    file_list = os.listdir(current_dir)
    for file in file_list:
        if file.endswith('.jpg'):
            jpg_list.append(file)
    return jpg_list


def convert_photo():
    current_dir = get_current_dir()
    result_dir = get_result_dir()
    jpg_list = get_jpg_list()
    for i, file in enumerate(jpg_list):
        current_dir_photo = os.path.join(current_dir, jpg_list[i])
        result_dir_photo = os.path.join(result_dir, 'new_' + jpg_list[i])
        str = 'convert {0} -resize 200 {1}'.format(current_dir_photo, result_dir_photo)
        convert = subprocess.run(str)
        print(convert)


convert_photo()
