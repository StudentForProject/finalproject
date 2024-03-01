"""
Custom helper for repetitive functions
"""
import os
import sys
import shutil

def remove_folder(folder_path):
    """
    Try to remove the folder at the specified path. Prints feedback successful or not.
    """
    try:
        shutil.rmtree(folder_path)
        print(f'Folder "{folder_path}" and its contents have been removed successfully.')
    except FileNotFoundError:
        print(f'Folder "{folder_path}" does not exist.')
    except Exception as e:
        print(f'Error removing folder "{folder_path}": {e}')

def remove_file(file_path):
    """
    Try to remove the file at the specified path. Prints feedback successful or not.
    """
    try:
        os.remove(file_path)
        print(f'File "{file_path}" deleted successfully.')
    except FileNotFoundError:
        print(f'File "{file_path}" does not exist.')
    except Exception as e:
        print(f'Error deleting file "{file_path}": {e}')

