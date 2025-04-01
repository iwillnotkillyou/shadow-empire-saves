import subprocess
import time

def pull():
    subprocess.run(["git", "pull"])

def pushAll():
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", "m"])
    subprocess.run(["git", "push"])

if __name__ == '__main__':
    start = time.time()
    pull()
    pushAll()
    while True:
        current_time = time.time()
        if current_time-start > 1:
            print("checked")
            pull()
            pushAll()
        start = current_time
