import os
import shutil


def organize(path): 
    file_type = {
        ".jpg": "Images",
        ".png": "Images",
        ".gif": "Images",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".mp4": "Videos",
        ".mov": "Videos",
    } # file type with correspondig folder
    
    file = os.listdir(path)

    #add logic for organizing..


if __name__ == "__main__":
    path = input("Enter path: ")
    organize(path)

