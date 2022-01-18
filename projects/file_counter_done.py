# Add the code for the file counter script that you wrote in the course.
import pathlib

file_types={}


pic_path=pathlib.Path('C:\\Users\\jsiu\\Pictures')
#iterdir - iterates over the files in directory

for filepath in pic_path.iterdir(): #looking over where the pictures are and iterating over them


    if filepath.suffix in file_types: # be careful of logic
        file_types[filepath.suffix]=file_types[filepath.suffix]+1 # getting the suffix out

    else:
        file_types[filepath.suffix] = 1
print(file_types)
#how to get the suffix out?
