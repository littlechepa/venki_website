from inspect import currentframe, getframeinfo # To get filename and line numbers
import os
from dash import html


def print_line_info(print_file_name = True):
    '''
    Get the current file name and line number in Python script. The line number is taken from the caller, i.e. where this function is called.

    Parameters
    ----------
    print_file_name : boolean
        If True, print the file name and line number to stdout.
    
    Returns
    -------
    None.

    Examples
    --------
    >>> print_line_info()

    >>> print_line_info(print_file_name = False)
    '''

    frameinfo = getframeinfo(currentframe().f_back)
    filename = frameinfo.filename.split('/')[-1]
    linenumber = frameinfo.lineno
    loc_str = 'Line: %d' % (linenumber)
    if print_file_name:
        print("********* Here at %s" % (loc_str), " File name : ", filename)
    else:
        print("********* Here at %s" % (loc_str))

def render_certificate():
    folder_path = 'assets/certificates'
    cert_children = []
    for root, _, files in os.walk(folder_path):    
        for file_name in files:
            file_name = os.path.join(root, file_name)
            # cert_children.append(html.Img(src=file_name,style = {"margin":"10px",'width': '100%', 'height': '600px'}))
            cert_children.append(html.Img(src = file_name, className = "cert-img"))
    return cert_children