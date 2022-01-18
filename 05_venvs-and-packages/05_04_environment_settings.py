# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os

#test = os.environ['VIRTUAL_ENV']
#print(test)

secret = os.environ['SECRET']
print(secret)

env = os.environ['ENVIRONMENT']
print(env)

#Set environment variables in activate.bat or activate.ps1 bash
