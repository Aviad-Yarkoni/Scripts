from file_handle import do_file_hash

def append_file_to_list (file_parameters,all_data):
    all_data.append(file_parameters)



def get_storage_type  (type):
    storage_type = []
    return storage_type



def append_to_list_file(list_file,item,atribute):
    list_file.append({'path':item['path'],atribute:item[atribute]})
    return sorted(list_file,key=lambda x:x[atribute])



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
    doplicate_files={}
    for item in file_list:
        item_path = item ['path']
        hash_file = do_file_hash(item_path)
        if hash_file in files_store:
            doplicate_path = files_store[hash_file]
            doplicate_files.update ([(item_path,doplicate_path)])
        else:
            files_store.update ({hash_file:item_path})
    return doplicate_files

        











a=[{'size':1,'path':'/home/osboxes/devsecops/alice'},{'size':2,'path':'/home/osboxes/devsecops/alice'},{'size':98,'path':'blabla'},{'size':1,'path':'blabla'},{'size':4,'path':'blabla'},{'size':4,'path':'blabla'}]
print (is_duplicate(a))