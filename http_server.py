import socket
import sys
import traceback
from os import listdir
from os.path import isfile, join
from os import walk
import mimetypes

def response_ok(body=b"This is a minimal response", mimetype=b"text/plain"):
    """
    returns a basic HTTP response
    Ex:
        response_ok(
            b"<html><h1>Welcome:</h1></html>",
            b"text/html"
        ) ->
        b'''
        HTTP/1.1 200 OK\r\n
        Content-Type: text/html\r\n
        \r\n
        <html><h1>Welcome:</h1></html>\r\n
        '''
    """
    
    ### Note a Standard HTTP Response:
    # Status Line       | HTTP-version status-code reason-phrase
    # Response Headers  | response-header-name: response-header-valuex
    # Blank Line        |
    # Response Body     | <h1>My Home Page </h1>
    
    ### Note: We are including the MimeType of the file to assist the 
    # Browser in displaying the information
    
    return b"\r\n".join([
            b"HTTP/1.1 200 OK",
            b"Content-Type: " + mimetype,
            b"",
            body,
            ])

def response_method_not_allowed():
    """Returns a 405 Method Not Allowed response"""

    ### The purpose of this function is simply to build the HTTP Response
    # Where the input HTTP is not of the "GET" Variety.
    
    # TODO: Implement response_method_not_allowed
    return b"\r\n".join([
            b"HTTP/1.1 405 RESPONSE NOT ALLOWED",
            b"",
            b"You Can't do that on this Server!"
            ])


def response_not_found():
    """Returns a 404 Not Found response"""
    ### The purpose of this function is simply to build the HTTP Response
    # Where the input HTTP does not map to a correct resource.
    
    # TODO: Implement response_not_found
    return b"\r\n".join([
            b"HTTP/1.1 404 NOT FOUND",
            b"",
            b"WEB PAGE CANNOT BE LOCATED"
            ])



def parse_request(request):
    """
    Given the content of an HTTP request, returns the path of that request.
    This server only handles GET requests, so this method shall raise a
    NotImplementedError if the method of the request is not GET.
    """
    
    ### Content Received is that of an HTTP "GET" Request. HTTP
    # Get Requests take the following form:
    # GET URL Version  |GET /docs/index.html HTTP/1.1
    # Host: host:port  |Host: www.nowhere123.com 
    
    
    
    # Splits the "GET" request into a list based on the Carriage Return
    # Line Feed. Then, assigns the First line of that list variables
    # Method, URL, and version
    
    ### Note: URI will be of the form "/docs/index.html"
    method, uri, version = request.split("\r\n")[0].split(" ")
    print("method", method, "uri", uri, "version", version)
    
    # Raises Implementation Error if the Request is not "GET"
    if method != "GET":
        raise NotImplementedError
    
    return uri



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


def server(log_buffer=sys.stderr):
    
    ### This portion of code represents where we set up a server. This is 
    ### meant to emulate some server that may exist on the web.
    
    # Set the Server's Address
    address = ('127.0.0.1', 10000)
    # Create a Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    
    # Bind the socket to the Server's Adress
    sock.bind(address)
    
    # Allow the Socket to Listen to Requests 
    sock.listen(1)

    try:
        # Outer 'While' Loop handles incoming connection
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()  # blocking
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                request = ''
                
                # Inner 'While' Loop recieves that data from the connection
                # This recieves information in segments of 1024 bits
                # It is broken when it recieves the "CRLF" line
                
                ### Note: The recieved information will be in the form of a
                # HTTP "GET" request
                while True:
                    data = conn.recv(1024)
                    request += data.decode('utf8')

                    if '\r\n\r\n' in request:
                        break
		

                print("Request received:\n{}\n\n".format(request))

                # TODO: Use parse_request to retrieve the path from the request.
                
                
                try:
                    # Process "GET" request to obtain desired resource
                    path = parse_request(request)

                    # TODO: Use response_path to retrieve the content and the mimetype,
                    # based on the request path.
                    
                    # Obtain the content and mimetype based on user request.
                    return_content, return_mime_type = response_path(path)
    
                    # TODO; If parse_request raised a NotImplementedError, then let
                    # response be a method_not_allowed response. If response_path raised
                    # a NameError, then let response be a not_found response. Else,
                    # use the content and mimetype from response_path to build a 
                    # response_ok.
                    
                    # Build the HTTP Response to send to the user based on the 
                    # mimetpy and content
                    response = response_ok(
                        body = return_content,
                        mimetype = return_mime_type,
                    )
                
                # Not Implemented Error will re-direct to the not allowed
                # Function
                except NotImplementedError:
                    response = response_method_not_allowed()
                # Name Error will redirect to the "Response Not Found" Error
                except NameError:
                    response = response_not_found()
                

                conn.sendall(response)
            except:
                traceback.print_exc()
            finally:
                conn.close() 

    except KeyboardInterrupt:
        sock.close()
        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    #server()
    #sys.exit(0)

