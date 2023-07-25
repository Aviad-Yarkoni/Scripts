import os
import datetime
import hashlib



def file_details (file_path,file_name):
   return {'name':file_name,
           'path':file_path,
           'size':file_size(file_path),
           'access time':file_access_time(file_path),
           'modify time':change_unix_time( file_modify_time(file_path)),
           'create time':file_create_time(file_path),
           }

def get_dir_content (directory):
   return os.listdir(directory) 
   
def file_size (files_path):
    return os.path.getsize(files_path)

def is_directory (files_path):
    return os.path.isdir(files_path)

def file_modify_time(files_path):
   return os.path.getmtime(files_path)

def file_access_time(files_path):
   return os.path.getatime(files_path)

def file_create_time(files_path):
   return os.path.getctime(files_path)

def change_unix_time (unix_time):
   return datetime.datetime.fromtimestamp (unix_time)
 

def do_file_hash(file_path):
    hash_file = hashlib.sha256()
    read_file = open(file_path, 'rb')
    while(True):
        sometext = read_file.read(20000)
        readlen = len(sometext)
        if readlen == 0:
            return hash_file.hexdigest()
        hash_file.update(sometext)


