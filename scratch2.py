import socket
import sys
import traceback
from os import listdir
from os.path import isfile, join
from os import walk
import mimetypes
import os

def response_path(path):
    """
    This method should return appropriate content and a mime type.
    If the requested path is a directory, then the content should be a
    plain-text listing of the contents with mimetype `text/plain`.
    If the path is a file, it should return the contents of that file
    and its correct mimetype.
    If the path does not map to a real location, it should raise an
    exception that the server can catch to return a 404 response.
    Ex:
        response_path('/a_web_page.html') -> (b"<html><h1>North Carolina...",
                                            b"text/html")
        response_path('/images/sample_1.png')
                        -> (b"A12BCF...",  # contents of sample_1.png
                            b"image/png")
        response_path('/') -> (b"images/, a_web_page.html, make_type.py,...",
                             b"text/plain")
        response_path('/a_page_that_doesnt_exist.html') -> Raises a NameError
    """

    # TODO: Raise a NameError if the requested content is not present
    # under webroot.
    
    
    ### Note: 'path' will be passed to the function in the following format:
    # /images/sample_1.png
    # /a_web_page.html
    # /images/
    
    ### Note: Function Must Do the following:
    #1: Validate Provided Path
    #2: Map to Data Based on the provided path
    #3: Determine Resource Mimetype
    #4: Turn Resource into bytes 

    # Create a list to store all Resource names and populate - This is for Reference 
    # Later in the script.
    all_files = []
    for (dirname, dirnames, filenames) in walk(os.getcwd() + '\webroot'):
        for filename in filenames:
            all_files.append(filename)
    print("All Files", all_files)
        
    # Split the input based on the "/"
    path_elements = path.split('/')
    print("Path Elemenets", path_elements)

    # Isolate the last element
    path = path_elements[-1]

    # If the element has a ".", we can assume that it is a file, otherwise assume it is 
    # A directory
    if "." in path:
        print("Resource")
        # --- Validate that the resource is available --- 
        
        # Create a list to store all Resource names and populate
        all_files = []
        for (firname, dirnames, filenames) in walk(os.getcwd() + '\webroot'):
            for filename in filenames:
                all_files.append(filename)
        print("All Files", all_files)
        
        
        # Verify the Files are within the Servers Resources
        if path in all_files:
            print("This is in all files")
        else:
            print("This is not in all files")
            # --- Raise 404 Error --- #
    else:
        print("File Path")
    
    return None


path_list = ['/images','/a_web_page.html','/images/sample_1.png', 'test.txt']
for path in path_list:
    response_path(path)
    print("*----------------------*")

