import os

os.system("pip3 install cx_Freeze")
os.system("sudo apt install -y patchelf")
os.system("python3 setup.py build")