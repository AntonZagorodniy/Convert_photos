import os
import subprocess

# def get_current_dir():
result = 'Result'
current_dir = os.path.dirname(os.path.abspath(__file__))
result_dir = os.path.join(current_dir, result)
os.chdir(current_dir)
try:
    os.mkdir(result_dir)
except OSError:
    pass
# return current_dir

print(result_dir)

convert = subprocess.run('convert') #, 'input.jpg -resize 200 output.jpg')   #(current_dir, 'convert')
print(convert)
# convert()
# convert input.jpg -resize 200 output.jpg