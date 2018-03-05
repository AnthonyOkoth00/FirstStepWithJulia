import os
import glob
import pandas as pd
import math

import numpy as np
from scipy.misc import imread, imsave, imresize
from natsort import natsorted

from labelConverter import label2int

# path of data files
path = "../firstStepWithJulia/"

# Input image dimensions
img_rows, img_cols = 32, 32

# Keep initial image aspect ratio or not
keepRatio = False

# Suffix of the created directories and files
suffix = "Preproc_" + str(img_rows) + "_" + str(img_cols) + ("_kr" if keepRatio else "")

# Create the directories if needed
if not os.path.exists(path + "/train" + suffix):
    os.makedirs(path + "/train" + suffix)
if not os.path.exists(path + "/test" + suffix):
    os.makedirs(path + "/test" + suffix)

### Images preprocessing ###


