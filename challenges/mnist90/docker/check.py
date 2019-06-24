import pandas as pd
import numpy as np
ALLOWED_EXTENSIONS = set(['csv'])
RESULT_CSV_PATH = "mnist_labels.csv"
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Update this function if not using discrete labels from a csv format
def open_labels(open_file):
	if isinstance(open_file,str):
		open_file = open(open_file,"r")

	df = pd.read_csv(open_file)
	if '7' in df.columns:
		data = np.array([7] + list(df['7'].values))
	else: 
		data = df['label'].values
	return data


CACHED_RESULT = np.array(open_labels(RESULT_CSV_PATH))

def score_submission(temp_file):
    THRESHOLD = 0.9
    #try:
    submitted_data = open_labels(temp_file)
    acc = np.mean(submitted_data == CACHED_RESULT)
    print("done checking images")

    return (acc > THRESHOLD)

if __name__ == '__main__':
	l = open_labels("mnist_labels.csv")
	print(l[:10])

	l = open_labels("with_header.csv")
	print(l[:10])

	l = open_labels("pandas_out.csv")
	print(l[:10])