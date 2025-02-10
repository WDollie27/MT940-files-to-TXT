# -*- coding: utf-8 -*- FOR CONVERSION OF MT940 FILES TO TEXT FILES
"""
Created on Mon Nov  4 14:34:00 2024

@author: waseemd
"""

import os
import shutil
from datetime import datetime

def convert_archive_and_cleanup_files(source_dir, archive_dir):
    """
    Converts files in the source directory (except folders, .py, and .bat files) to .txt files,
    moves them to the archive directory organized in a folder named with today's date, 
    and removes the original files.

    :param source_dir: Directory containing the files.
    :param archive_dir: Directory to store archived .txt files.
    """
    # Ensure source and archive directories exist
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Get today's date for folder naming
    today_date = datetime.now().strftime("%Y-%m-%d")
    archive_subfolder = os.path.join(archive_dir, today_date)
    
    # Create a folder for today's archive if it doesn't exist
    if not os.path.exists(archive_subfolder):
        os.makedirs(archive_subfolder)
    
    # Process each item in the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        
        # Skip folders, Python files, and Batch files
        if os.path.isdir(item_path) or item.lower().endswith((".py", ".bat")):
            continue
        
        # Convert to .txt file
        txt_filename = os.path.splitext(item)[0] + ".txt"
        txt_path = os.path.join(source_dir, txt_filename)

        try:
            # Read the content of the file
            with open(item_path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Write the content to a .txt file
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(content)
            
            # Move the .txt file to the archive folder
            shutil.move(txt_path, os.path.join(archive_subfolder, txt_filename))
            print(f"Converted and archived: {item_path} -> {txt_filename}")

            # Remove the original file after successful conversion
            os.remove(item_path)
            print(f"Removed original file: {item_path}")

        except Exception as e:
            print(f"Error processing file '{item}': {e}")
    
    print(f"All files have been processed, archived, and original files removed from '{source_dir}'.")

# Example usage
source_directory = r"C:\Users\waseemd\Desktop\RMB Test"  # Replace with the path to your source directory
archive_directory = r"C:\Users\waseemd\Desktop\RMB Test\Archive"  # Replace with the path to your archive directory
convert_archive_and_cleanup_files(source_directory, archive_directory)




