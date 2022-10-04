import os,json
def search_files(path, extension):
    directory_files=[]
    new_path = path.split(" ")
    new_path = new_path[2]
    try:
        directory_content= os.listdir(new_path)
    except:
        return[]
    
    for file in directory_content:
        if file.endswith(extension):
            directory_files.append(file)
    print(directory_files is not None)         
    return directory_files
    
def read_data(files=""):
    data = []
    for file in files:
        convert_file = file.split(" ")
        convert_file = convert_file[2]
        try:
            with open(convert_file, 'r') as json_file:
                json_object = json.load(json_file)
                data.append(json_object)
        except:
            return[]        
    return data
   
 