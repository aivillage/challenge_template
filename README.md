# AI Village CTFd Challenges
## Description
Each "flag" on the CTF board is defined by a CTFd challenge. These usually
have to be entered individually in CTFd's GUI, but that process has been 
automated by the village's [challenge injector plugin](https://gitlab.com/aivillage/ctfd_challenge_injector_plugin). 
Use the injector's challenge format to add your own challenge and it will be 
automatically added as a flag to the village's CTF.
## Challenges
### Standard Challenges
Standard challenges check a string submitted by a contestant against the 
answer, otherwise known as the flag. They're defined by JSON files and can
include additional files that will be available for download no the
challenge's page.
### Extended Challenges
Extended challenges spin up up a Docker container to perform additional 
processing. Containers are defined by a Dockerfile inside of the challenge's
directory. They must return a string that can be checked for correctness.
