import numpy as np
from skimage import io, img_as_float
import os
import tempfile
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Update this function if not using discrete labels from a csv format
def open_image(data):
    filename = secure_filename(data.filename)
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    handle, filepath = tempfile.mkstemp()
    f = os.fdopen(handle)  # convert raw handle to file object
    return img_as_float(io.imread(data))

CACHED_RESULT = open_image(RESULT_IMAGE_PATH)
FLAG = "thingies go here"

def score_submission(uploaded_file):
    THRESHOLD = 0.001
    #try:
    print("opening image: ",uploaded_file)
    submitted_data = open_image(uploaded_file)
    acc = (submitted_data - CACHED_RESULT).abs().max()
    print("done checking images")

    return (acc < THRESHOLD)