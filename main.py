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
    
    files = os.listdir(path)
    for file in files:
        extension = os.path.splitext(file)[1] # access file extension

        if extension in file_type:
            category = file_type[extension]
            category_path = os.path.join(path, category)

            if not os.path.exists(category_path): # create new folder if there isn't one already
                os.makedirs(category_path)
        
            source = os.path.join(path, file)
            dest = os.path.join(category_path, file)

            shutil.move(source, dest)


if __name__ == "__main__":
    path = input("Enter path: ")
    organize(path)

