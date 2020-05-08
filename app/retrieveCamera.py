import os
from Camera import Camera

PATH = "/sys/class/video4linux"

def getCameraList():
    """
    Get a list of cameras found in the video4linux directory

    Returns:
        Camera[List] -- A list of Camera objects
    """
    cameras = []

    for dirname, subdirs, filelist in os.walk(PATH):
        
        for d in subdirs:
            # get camera names
            with open(dirname + '/' + d + '/name', 'r') as file:
                name = file.read().replace('\n', '')

            # get camera index
            with open(dirname + '/' + d + '/index', 'r') as file:
                index = file.read().replace('\n', '')

            c = Camera(name, index)
            cameras.append(c)

    return cameras



if __name__ == "__main__":
    print("\nGetting video devices")
    cameras = getCameraList()
    
    for c in cameras:
        print(c)

    print()