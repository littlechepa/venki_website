from inspect import currentframe, getframeinfo # To get filename and line numbers


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

    