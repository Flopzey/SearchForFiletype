import os

def find_files(directory, output_file):
    files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xlsx"): #<-
                files.append(os.path.join(root, file))

    with open(output_file, 'w') as f:
        for fmw_file in files:
            file_name = os.path.basename(fmw_file)
            f.write(fmw_file + '; ' + file_name + '\n')

    print(f"Es wurden {len(files)} Dateien gefunden und in {output_file} geschrieben.")

directory = r"H:\\placeholder" #<-
output_file = r"C:\\placeholder\\placeholder\\output.txt" #<-

find_files(directory, output_file)
