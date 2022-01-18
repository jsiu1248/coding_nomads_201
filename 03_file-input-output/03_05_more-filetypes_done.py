# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.


# record unique type files
# count how many of each type
# start with one layer

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
