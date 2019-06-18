from flask import Flask, request, flash, redirect, url_for, send_from_directory, render_template
import json
app = Flask(__name__, static_url_path="", static_folder=".")
from check import score_submission

CONFIGURATION = {}
with open("challenge_definition.json", "r") as f:
    CONFIGURATION = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        try:
            response = score_submission(file)
            if response:
                return render_template(
                    "index.html",
                    challenge_name=CONFIGURATION["ctfd"]["name"],
                    challenge_description=CONFIGURATION["ctfd"]["message"],
                    submission_response=CONFIGURATION["custom_flag_check"]["congratulations_message"],
                    flag=CONFIGURATION["ctfd"]["flag"]
                )
            else:
                return render_template(
                    "index.html",
                    challenge_name=CONFIGURATION["ctfd"]["name"],
                    challenge_description=CONFIGURATION["ctfd"]["message"],
                    submission_response=CONFIGURATION["custom_flag_check"]["consolation_message"],
                )
        except:
            return render_template(
                "index.html",
                challenge_name=CONFIGURATION["ctfd"]["name"],
                challenge_description=CONFIGURATION["ctfd"]["message"],
                submission_response="Something broke, try again",
            )
    return render_template(
            "index.html",
            challenge_name=CONFIGURATION["ctfd"]["name"],
            challenge_description=CONFIGURATION["ctfd"]["message"],
        )

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))