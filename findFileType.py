import os

def set_search_directory(directory):
    global search_directory
    search_directory = directory

def set_output_file_path(output_file):
    global output_file_path
    output_file_path = output_file

def set_file_type_to_search(file_type):
    global file_type_to_search
    
    if file_type.startswith("."):
        file_type_to_search = file_type
    else: 
        file_type_to_search = "." + file_type
    

def find_files():
    if not search_directory or not output_file_path:
        # todo - change label in gui?
        return
    
    files = []

    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if file.endswith(file_type_to_search):
                files.append(os.path.join(root, file))

    with open(output_file_path, 'w') as f:
        for fmw_file in files:
            file_name = os.path.basename(fmw_file)
            f.write(fmw_file + '; ' + file_name + '\n')

    print(f"Es wurden {len(files)} Dateien gefunden und in {output_file_path} geschrieben.")

search_directory = None
output_file_path = None
file_type_to_search = None
