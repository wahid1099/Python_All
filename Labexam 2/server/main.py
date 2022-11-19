import glob
import time
import shutil
import os
import zipfile
source_path = '../source/*'
destination_path = '../destination/'
idx = 0
all_working_files = []
while True:
    source_object = glob.glob(source_path)
    if len(source_object) > 0 and idx < len(source_object):
        full_obj_path = source_object[idx]
        if full_obj_path not in all_working_files:
            source_object_path = full_obj_path.split('/')
            print("source_object_path is", source_object_path)
            file_name = source_object_path[2].split('.')[0]
            print("file name is", file_name)
            extension_name = source_object_path[2].split('.')[1]
            print("extension_name is", extension_name)
            print(f'\n\nWorking on file:{full_obj_path}')
            if extension_name == 'txt':
                all_lines = []
                with open(full_obj_path, 'r') as sour_file:
                    for lines in sour_file.readlines():
                        all_lines.append(lines)

                all_files = []
                print('copying file to the server.')

                for item in range(3):
                    full_file_name = f'{file_name}_{item+1}.txt'
                    with open(full_file_name, 'w') as des_file:
                        des_file.write(''.join(all_lines[:(item+1)*10]))
                    des_file.close()
                    all_files.append(full_file_name)

                print('zipping the file.')
                time.sleep(1)
                zip_file_name = f'{file_name}.zip'
                zip_file_path = f'./{zip_file_name}'
                with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                    for item in all_files:
                        zip_file.write(item)
                        os.remove(item)
                zip_file.close()
                print('copying the zip file to the destination')
                time.sleep(1)
                shutil.copy(zip_file_path, destination_path)
                os.remove(zip_file_path)
                print('extracting the zip file')
                time.sleep(1)
                with zipfile.ZipFile(f'{destination_path}{zip_file_name}') as zf:
                    zf.extractall(f'{destination_path}')
                os.remove(f'{destination_path}{zip_file_name}')
                os.remove(full_obj_path)
                print(f'Operation done file:{full_obj_path}')
            elif extension_name == 'py':
                all_working_files.append(full_obj_path)
                idx += 1
                print('Running python script:', end="")
                for i in range(5):
                    time.sleep(1)
                    print('.', end='')
                print("\n")
                try:
                    os.system(f'python {full_obj_path}')
                    os.remove(full_obj_path)
                except os.error:
                    print(os.error)
                # os.remove(full_obj_path)
                print('\n----End of the script----')
        else:
            idx += 1
    else:
        idx = 0
