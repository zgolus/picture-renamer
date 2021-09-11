import os
import exifread

path = "/home/jakub/Pictures/test"

file_list = os.scandir(path)

for file in file_list:
    with open(path + "/" + file.name, 'rb') as fh:
        tags = exifread.process_file(fh)
        date_taken = tags["EXIF DateTimeOriginal"]
        file_name, file_ext = os.path.splitext(path + "/" + file.name)
        os.rename(path + "/" + file.name, path + "/" + str(date_taken) + "." + file_ext)
        print(f"Renamed {file.name} to {str(date_taken)} {file_ext}")