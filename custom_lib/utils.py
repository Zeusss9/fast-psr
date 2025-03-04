import os

def create_folder(saved_folder):
    try:
        os.mkdir(saved_folder)
        print(f"Directory '{saved_folder}' created successfully.")
    except FileExistsError:
        print(f"Directory '{saved_folder}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{saved_folder}'.")
    except Exception as e:
        print(f"An error occurred: {e}")