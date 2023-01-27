import numpy as np
import cv2
import os
import sys, getopt

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def main(argv):
    folder = ''
    opts, args = getopt.getopt(argv,"hi:o",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == "-i":
            folder = arg

    if (folder == ""):
        print("Need folder")
        sys.exit()

    images = load_images_from_folder(folder)
    output = np.array(images)

    print(len(output))
    np.save(os.path.join(folder,"numpyImageArray"),output)

if __name__ == "__main__":
    main(sys.argv[1:])
