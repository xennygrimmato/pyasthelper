import subprocess


def func():
    filename = "xyz.py"
    child = subprocess.Popen(['python', filename])

