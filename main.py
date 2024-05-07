import os
import shutil
import sys
from collections import defaultdict

def organize_files(base_path):
    # Count occurrences of each file number for .MP4 files
    mp4_count = defaultdict(int)
    file_paths = defaultdict(list)

    # First pass to collect file information
    for filename in os.listdir(base_path):
        if filename.endswith(('.MP4', '.LRV', '.THM')):
            file_number = filename[4:8]
            file_paths[file_number].append(filename)
            if filename.endswith('.MP4'):
                mp4_count[file_number] += 1
    
    # Save original paths before moving
    with open(os.path.join(base_path, 'original_paths.txt'), 'w') as f:
        # Second pass to move files if there are multiple MP4s with the same number
        for file_number, files in file_paths.items():
            if mp4_count[file_number] > 1:  # Create folder only if more than one MP4 file with the same number
                folder_name = f"Video_{file_number}"
                folder_path = os.path.join(base_path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                for filename in files:
                    original_path = os.path.join(base_path, filename)
                    new_path = os.path.join(folder_path, filename)
                    shutil.move(original_path, new_path)
                    print(f"Moved '{filename}' to '{new_path}'")
                    f.write(f"{new_path}={original_path}\n")

def undo_organization(base_path):
    paths_file = os.path.join(base_path, 'original_paths.txt')
    
    if not os.path.exists(paths_file):
        print("No organization to undo.")
        return
    
    # Read the original paths and move files back
    with open(paths_file, 'r') as file:
        for line in file:
            new_path, original_path = line.strip().split('=')
            shutil.move(new_path, original_path)
            print(f"Moved '{new_path}' back to '{original_path}'")
    
    # Remove empty folders
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)
            print(f"Removed empty folder: {folder_path}")

    os.remove(paths_file)
    print("Undo complete.")

if __name__ == "__main__":
    # Use the current directory as the base directory
    base_directory = os.getcwd()
    if len(sys.argv) > 1 and sys.argv[1] == '-undoLast':
        undo_organization(base_directory)
    else:
        organize_files(base_directory)
    
