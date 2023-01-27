import numpy as np
import cv2
import os
import sys, getopt

BAROQUE = 0
CUBISME = 1
EXPRESIONNISME = 2
IMPRESSIONISME = 3
MANNIERISME = 4
NEOCLASSICISME = 5
POINTILLISIME = 6
POPART = 7
SURREALISME = 8

def importNumpyArray(path):
    array = np.load(path)
    return array

def main(argv):
    x_test = []
    x_train = []
    y_test = []
    y_train = []

    ### LABELS
    for i in range(9):
        y_train.extend([i] * 760)
        y_test.extend([i] * 189)

        ### LABELS

    ### IMAGE
    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Baroque/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Cubism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Expressionism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Impressionism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Mannerism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Neoclassicism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Pointillism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_PopArt/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    test = importNumpyArray("../images/FORMATTED_IMAGES/Cropped_Surrealism/numpyImageArray.npy")
    x_test.extend(test[760:])
    x_train.extend(test[:760])

    ### IMAGE
    y_test = np.array(y_test)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    x_train = np.array(x_train)

    np.save(os.path.join("./","x_test"),x_test)
    np.save(os.path.join("./","x_train"),x_train)
    np.save(os.path.join("./","y_test"),y_test)
    np.save(os.path.join("./","y_train"),y_train)

if __name__ == "__main__":
    main(sys.argv[1:])
