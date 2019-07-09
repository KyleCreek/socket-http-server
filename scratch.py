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
    
    
    # --- Validate Provided Path --- #
    # Creates a list of all FILES in the directory

    # Establish the Current Workinf Directory and add the "Webroot"
    file_path = os.getcwd() + "\webroot"
    #print("filepath", file_path)

    #for file_ in os.listdir(file_path):
    #    if os.path.isfile(file_path+file):
    #        print(file_)
    #    elif os.path.isdir(file_path+file):
    #        print("Directory")
    #f = []
    #f2 = []

    #for (dirpath, dirnames, filenames) in walk(file_path):
    #    f.append(filenames)
    #for thing in f:
    #    print(thing)


    # Parse the Path for examination and comparison to content
    # and determine if it is a file or path
    
    # Create a list of the Path, length of the list is greater than
    # 2, then We know a directory has been passed
    path_elements = path.split(".")
    
    # Case Statement to Handle Files
    if len(path_elements) > 1:
        print("This is a file", path_elements)


    
        # --- Determine Resource MimeType --- #
        ### Note: File Resources typically appear as "xxx.yyy"
        ### Note: This Section is Currently Working!!
        # Create a dictionary of MIME Types for comparison
        mime_dictionary = mimetypes.types_map
        
        # Compare the provided resource extension to existing extensions
        # and return the value.

        # Split the Path Provided to the Function
        mime_check = path.split(".")
        # Add the period back into the Check
        mime_check = '.' + mime_check[-1]
        
        # Assign the Mime Type once it is determined to be in the 
        # Dictionary
        try:
            mime_type = mime_dictionary[mime_check]
        except KeyError:
            raise NotImplementedError
            
        # --- Map Data Based On Provided Path --- #
        retrieve_path = file_path + path
        print(retrieve_path)

        with open(retrieve_path, 'rb') as binary_file:
            content = binary_file.read()
        

        # --- Turn Resource into Bytes --- # 

        

        # TODO: Fill in the appropriate content and mime_type give the path.
        # See the assignment guidelines for help on "mapping mime-types", though
        # you might need to create a special case for handling make_time.py
        #
        # If the path is "make_time.py", then you may OPTIONALLY return the
        # result of executing `make_time.py`. But you need only return the
        # CONTENTS of `make_time.py`.
        
        #content = b"not implemented"
        #mime_type = b"not implemented"

    
    # Case Statement to Handle Directories
    ### Note: This section currently Works
    else:
        # Re-Route the File Path to return Text of Directory
        get_path = file_path + path

        # Obtain all the content from that directory
        contents = os.listdir(get_path)

        # Write all the content as a bit string
        content = ''
        for data in contents:
            content = content + data + '\r\n'
        content = content.encode('utf-8')
        #print(content)
        mime_type = b"text/plain"


    return content, mime_type


paths = ['\\a_web_page.html', '\\favicon.ico','\\images\\','\\images\\sample_1.png']

test = response_path('\\images\\sample_1.png')
print("THis is test", test)
