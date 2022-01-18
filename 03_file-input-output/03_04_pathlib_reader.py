# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
import pathlib
import csv




path=pathlib.Path('C:\\Users\\jsiu\\Documents\\codingnomads\\python-201-main_jsiu\\python-201-main\\03_file-input-output\\file-counter\\filecounts.csv')


with open(path, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)