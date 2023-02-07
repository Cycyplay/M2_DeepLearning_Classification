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
    inputfolder = ''
    outputfolder = 'cropped_images/'
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
       if opt == '-h':
          print ('test.py -i <inputfile> -o <outputfile>')
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfolder = arg
       elif opt in ("-o", "--ofile"):
          outputfolder = arg
    
    images = load_images_from_folder(inputfolder)
    images = [image[0:300,0:300] for image in images]
    #print(images)
    for i in range(len(images)):
        images[i] = cv2.resize(images[i],(64,64),interpolation = cv2.INTER_AREA)
        cv2.imwrite(os.path.join(outputfolder,str(i)+".jpg"),images[i])

    outputNumpyFusion = np.array([])
    for im in images:
        np.append(outputNumpyFusion,im);

    np.save(os.path.join(outputfolder,"numpyFusion"),outputNumpyFusion)

if __name__ == "__main__":
   main(sys.argv[1:])
