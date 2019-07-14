import numpy as np
from skimage import io, img_as_float


ALLOWED_EXTENSIONS = set(['jpg'])
RESULT_IMAGE_PATH = "result.png"
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Update this function if not using discrete labels from a csv format
def open_image(open_file):
    return img_as_float(io.imread(open_file))


CACHED_RESULT = open_image(RESULT_IMAGE_PATH)
FLAG = "thingies go here"

def score_submission(temp_file):
    THRESHOLD = 0.001
    #try:
    submitted_data = open_image(temp_file)
    acc = np.max(np.abs(submitted_data - CACHED_RESULT))
    print("done checking images")

    return (acc < THRESHOLD)