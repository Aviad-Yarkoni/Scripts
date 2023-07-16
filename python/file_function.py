import os
import datetime



def file_size(file_name):
    return os.path.getsize(file_name)
    
def file_path (file_name):
    return os.path.join (file_name)
    
def is_directory (file_name):
    return os.path.isdir (file_name)

def file_Creation_time (file_name):
     return os.path.getctime (file_name)
    

def file_modification_time (file_name):
     return os.path.getmtime (file_name)
    

def file_access_time (file_name):
     return os.path.getatime (file_name)

def change_unix_time (unix_time):
     return datetime.datetime.fromtimestamp(unix_time)

def get_dir_content (dirpath):
    return os.listdir(dirpath)





# a = file_access_time ("/home/osboxes/devsecops/alice")
# print( a )
# print (change_unix_time (a))


# a = file_Creation_time ("/home/osboxes/devsecops/alice")
# print( {a} )
# print (change_unix_time (a))

# a = file_modification_time ("/home/osboxes/devsecops/alice")
# print( {a} )
# print (change_unix_time (a))