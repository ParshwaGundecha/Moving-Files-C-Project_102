import os
import shutil

from_dir = 'C:/Users/Nitesh/Downloads'
to_dir = 'C:/Users/Nitesh/Documents'

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    name, extension = os.path.splitext(i)

    if extension == '':
        continue
    elif extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + i

        if os.path.exists(path2):
            print('Moving' + i + '......')
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print('Moving' + i + '......')
            shutil.move(path1, path3)
