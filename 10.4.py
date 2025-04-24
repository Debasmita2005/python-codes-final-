# Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.

import shutil

source_file = "source.txt"
destination_file = "target.txt"

shutil.copy(source_file, destination_file)

print("File copied from 'source' to 'target' successfully.")
