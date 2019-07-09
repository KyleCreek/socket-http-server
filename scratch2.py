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

    ### Note: The following is created as a means for Reference later in the Program
    # ------------------------------------------------------------------------------ #
    
    # Create a list to store all Resource names and populate - This is for Reference 
    # Later in the script.
    all_files = []
    all_dirs = ['webroot']
    for (dirname, dirnames, filenames) in walk(os.getcwd() + '\webroot'):
        for filename in filenames:
            all_files.append(filename)
        for dirname in dirnames:
            all_dirs.append(dirname)
    #print("All Files", all_files)
    print("All Dirs", all_dirs)



    # Create a dictionary of MIME Types for comparison
    mime_dictionary = mimetypes.types_map
    
    
    # ------------------------------------------------------------------------------ #        
    
    # Split the input based on the "/"
    path_elements = path.split('/')
    print("Path Elemenets", path_elements)

    # Isolate the last element
    path = path_elements[-1]

    # If the element has a ".", we can assume that it is a file, otherwise assume it is 
    # A directory
    if "." in path:
        #print("Resource")
        # --- Validate that the resource is available ---     
        
        # Case Statment where File Exists
        if path in all_files:
            #print("This is in all files")
            # Create a File Directory based on the provided path
            directory_file = os.getcwd() + '\webroot\\' + '\\'.join(path_elements)
            
            # Write content to Binary File
            with open(directory_file, 'rb') as binary_file:
                content = binary_file.read()
                #print(content)
            
            # Check the Mime Type
            #print("------")
            #print("Performing Mime Check")
            mime_check = path_elements[-1].split('.')
            mime_check = '.' + mime_check[-1]
            try:
                mime_type = mime_dictionary[mime_check]
                print(mime_type, "mime_type")
            except KeyError:
                print("Not In mime Dictionary")
        
        # Case Statement where the desired resource is not available
        else:
            print("This is not in all files")
            # --- Raise 404 Error --- #
    
    # Case Statement where Resource expects a path
    else:
        # Handle a '/' Case
        if len(path_elements[-1]) == 0:
            pass
            # Handle Web Root
        # Case Statement where non '/' file was passed to Browser
        else:
            # Make Sure that the Directory is Valid
            if path in all_dirs:
                directory_file = os.getcwd() + '\\webroot'
                direc_files = os.listdir(directory_file)

                # Write List Contents to Binary Format
                content = ''
                for data in direc_files:
                    content = content + data + '\r\n'
                content = content.encode('utf-8')
                #print(content)
            # Re-direct where Directory is not valid
            else:
                print("That is not in the Directory")
        
        
    
        return None


path_list = ['/images','/a_web_page.html','/images/sample_1.png', 'test.txt','/', '/wrong']
for path in path_list:
    response_path(path)
    print("*----------------------*")

