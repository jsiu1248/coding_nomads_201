# Add your file counter code here.
# Then add more code that writes the file counts to a `.csv` file.

import csv
data=[]
with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])



    for line in reader:
        data.append(line)
print(data)


with open('new_file.csv', 'w', newline='') as csvfile:
    new_file = csv.writer(csvfile)

    new_file.writerows(data)
 # I have to remember to indent and check out the documentation for all of this

 # pandas vs csv and reading one line at a time vs whole

