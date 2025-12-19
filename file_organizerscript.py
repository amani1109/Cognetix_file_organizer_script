import os
import shutil

print("FILE ORGANIZER PROGRAM")
folder_path = input("Enter the folder path you want to organize: ")
if not os.path.exists(folder_path):
    print("Folder does not exist.")
else:
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            file_name, file_extension = os.path.splitext(item)
            if file_extension == "":
                folder_name = "No_Extension"
            else:
                folder_name = file_extension[1:]
            new_folder_path = os.path.join(folder_path, folder_name)
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            shutil.move(item_path, os.path.join(new_folder_path, item))

    print("Files organized successfully!")
