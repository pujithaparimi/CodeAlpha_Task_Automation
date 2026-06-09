import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_files = 0

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")
        moved_files += 1

print(f"\nTotal JPG files moved: {moved_files}")
print("Task completed successfully!")
print("Task completed successfully!")