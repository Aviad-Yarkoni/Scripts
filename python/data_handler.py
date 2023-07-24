from file_handler import do_file_hash

def append_file_to_list (file_parameters,all_data):
    all_data.append(file_parameters)
    return all_data


def get_storage_type ():
    storage_type = []
    return storage_type



def append_to_list_file(list_file,item,atribute):
    list_file.append ({'path':item['path'],atribute:item[atribute]})
    list_file=sorted(list_file,key=lambda x:x[atribute])
    return list_file



def get_highest_files (list_file,atribute,n=10):
    biggest_file = []
    for file in list_file:
        if len(biggest_file) < n:
            biggest_file = append_to_list_file(biggest_file,file,atribute)
            continue

        if file [atribute] > biggest_file[0][atribute]:
            biggest_file.pop(0)
            biggest_file = append_to_list_file(biggest_file,file,atribute)
    return biggest_file




def get_lowest_files (list_file,atribute,n=10):
    biggest_file = []
    for file in list_file:
        if len(biggest_file) < n:
            biggest_file = append_to_list_file(biggest_file,file,atribute)
            continue

        if file [atribute] < biggest_file[-1][atribute]:
            biggest_file.pop(-1)
            biggest_file = append_to_list_file(biggest_file,file,atribute)
    return biggest_file




def is_duplicate (file_list):
    files_store = {}
    duplicate_files={}
    for item in file_list:
        item_path = item ['path']
        hash_file = do_file_hash(item_path)
        if hash_file in files_store:
            duplicate_path = files_store[hash_file]
            duplicate_files[item_path]=duplicate_path
            continue
        files_store [hash_file] = item_path
    return duplicate_files

 


def get_dirs_size (files_list):
    dirs_size={}
    for item in files_list:
        dir_path = item['path'].rsplit('/',1)[0]
        if dir_path in dirs_size:
            dirs_size [dir_path]= dirs_size[dir_path]+item['size']
            continue
        dirs_size[dir_path] = item ['size']
    return dirs_size



        
# a=[{'size':1,'path':'/home/osboxes/devsecops/alice'},
#    {'size':2,'path':'/home/osboxes/devsecops/alice'},
#    {'name': 'b', 'path': '/home/osboxes/devsecops/david/b' },
#     {'name': 'a', 'path': '/home/osboxes/devsecops/david/a'},
#     {'size':176,'path':'/home/osboxes/devsecops/david/alice'},
#     {'name': 'b', 'path': '/home/osboxes/devsecops/david/forscript/asd/b', 'size': 0, 'access time': 1690060192.7957535, 'modify time':795753, 'create time': 1690060192.7957535}, 
#     {'name': 'a', 'path': '/home/osboxes/devsecops/david/forscript/a', 'size': 0, 'access time': 1690060162.7723832, 'modify time':2023, 'create time': 1690060162.7723832}]
# #print (get_highest_files (a,'size'))
# for item in is_duplicate(a).items():
#     print (item)