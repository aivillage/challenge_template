# The Extended Challenge Template
Are you looking to serve up a challenge, and want as much control as possible?  You can take your shoes off and get comfy then. Also, if you are looking to develop a new flag server template and its very different from any of the existing ones, this is your spot too! All flag server templates should extend from this template, as it will be the base minimum requirements to be deployed.

The Extended Challenge Template is the barebones of what is needed to run a challenge with a flag server through our deployment strategy. You do need to ensure that your Dockerfile exposes port 80, and that you are hosting an HTTP server on port 80. If your service is not responsive, the health checks will report the delays in responses, and we'd likely purge and redeploy another instance of it, so please avoid signficant lag in responses to basic queries.

With all extended type questions, the ctfd.message will be set on the CTFd server to tell the users to follow the link to the flag server. This will be handled by the deployment process, and you can use the ctfd.message configuration parameter for other purposes when using this template.


```json
{
    "ctfd": {
        "type": "extended",
        "name": "todo: Change me to the name of your challenge!",
        "category": "todo: Put challenge category here!",
        "message": "todo: Put all the challenge details to be displayed to the user here! Supports HTML and Markdown, but please save anything with intricate back and forth for implementation as a flag server",
        "value": 100,
        "flag_type": "static",
        "flag": "todo: Define your flag/answer here!",
        "attempt_limit": -1
    },
    "static_files": {
        "public_files": {
            "name_of_the_file_locally": "name_of_file_to_user"
        }
    },
    "deployment": {
        "dockerfile": "Dockerfile",
        "setup_type": "install.sh",
        "run_type": "run.sh"
    }
}
```

Note that the ctfd.type has been changed to "extended" to indicate that this question requires more than what CTFd supports.
The static files will be pushed to the gateway server and served up statically for the fastest response times and least overhead on our private network. All files in a challenge folder will, by default, be added to the docker instance as well.

The new section, "deployment", requires that you define a path to your Dockerfile for your challenge, and requires you put in a "setup_type". The Extended Challenge Template, in its bare bones nature, will simply run `sh install.sh` in the directory that your challenge has been copied into by the Dockerfile in order to install any dependencies or prepare anything needed. Your `run.sh` script should start your HTTP flag server on port 80.