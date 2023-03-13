# two arguments: folder name, new folder name
import sys
import os
from PIL import Image

# grab first and second argument
old_folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new folder exists, if not create it
if not os.path.exists(new_folder):
    os.mkdirs(new_folder)

# loop through files in folder
for infile in os.listdir(old_folder):
    img = Image.open(old_folder + infile)

    # remove extension from filename
    filename, extension = os.path.splitext(infile)

    # convert images to png and save to the new folder
    img.save(new_folder + filename + '.png', 'png')
    print('all done!')
