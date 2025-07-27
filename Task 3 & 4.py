# Task 3
import requests
import numpy

print("Requests version:", requests.__version__)
print("NumPy version:", numpy.__version__)


import pkg_resources

installed_packages = pkg_resources.working_set
for package in installed_packages:
    print(f"{package.project_name}=={package.version}")
