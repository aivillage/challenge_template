# AI Village challeges

Here are some example challeges for the AI Village CTF.

Please see the FGSM challenge for a docker challenge, and the clusters for a normal challege.	

# Testing

These are going to be uploaded to Google Cloud to run via Cloud Run. The command they use to run this is testable by running this:
```
docker build -t fgsm . && docker run -e PORT=8080 -p 127.0.0.1:80:8080/tcp -it fgsm
```