import numpy as np

import os
from PIL import Image 
import tempfile
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Update this function if not using discrete labels from a csv format
def convert_label_file_string_to_labels(data):
    lines = data.split("\n")
    if len(lines) != 20:
        return None
    processed_data = []
    for line in lines:
        processed_data.append(np.array(
            [
                int(label) for label in (
                    l.strip() for l in data.split(",")
                    ) if len(label) != 0
            ],
            dtype=np.int32
        ))
    return np.concatenate(processed_data)

with open(TESTING_LABELS_PATH, "r") as f:
    CACHED_LABELS = convert_label_file_string_to_labels(f.read())

CACHED_RESULT = open_local_image("result.png") 

def score_submission(uploaded_file):
    THRESHOLD = 0.001
    submitted_data = open_image(uploaded_file)
    if len(submitted_data.shape) != len(CACHED_RESULT.shape):
        return False
    for a,b in zip(submitted_data.shape,CACHED_RESULT.shape):
        if a != b:
            print(a,b)
            return False

    acc = (np.abs(submitted_data - CACHED_RESULT)).max()

    return (acc < THRESHOLD)