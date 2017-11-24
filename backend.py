#!/usr/bin/python3.5

import os
import re
        
def check_password_policy(changeTries=None, maxDays=None, maxLen=None, minLen=None) -> bool:
    """
    Checks if passwords policy is enforced
    
    Scrubs the /etc/login.defs file for parameters:
    [
        PASS_CHANGE_TRIES, PASS_MAX_DAYS, 
        PASS_MAX_LEN, PASS_MIN_LEN
    ]
    
    User can set values for these parameters to match
    
    Parameters
    ----------
    
    changeTries : int
        DEFAULT = None
        Represents how many times a user may attempt to change password
        before they are locked out
    maxDays : int
        DEFAULT = None
        Represents maximum days that a password will stay valid
    maxLen : int    
        DEFAULT = None
        Represents maximum length of new passwords
    minLen : int
        DEFAULT = None
        Represents minimum length of new passwords
        
    Returns
    -------
    
    bool
        True if parameters set by user match what is in /etc/login.defs
        False otherwise
        
       
    """
       
    loginFile = open("/etc/login.defs", 'r')
    
    # List of lines containing values we are checking
    lines = []
    
    # Will hold translated key/value pairs from the 'lines' list
    valueDict = {}
    
    # Filtering lines in /etc/login.defs to only save lines with the 
    # search values
    for line in loginFile:
        if (
                ('PASS_MAX_DAYS' in line or
                'PASS_CHANGE_TRIES' in line or
                'PASS_MIN_LEN' in line or
                'PASS_MAX_LEN' in line) and
                # Prevents commented lines from being included
                '#' not in line
            ):
            
            # Saves line to 'lines' array
            lines.append(line)
    
    # Closes file '/etc/login.defs'
    loginFile.close()
            
    '''
    Translates lines[] into a dictionary
    
    Example lines[] state is ['PASS_MAX_DAYS\t9999\n']
    
    Translated sample: {'PASS_MAX_DAYS': '9999'}
    '''
    for entry in lines:
        key = entry.split('\t')[0]
        value = re.sub("\D", "", entry.split('\t')[1])
        valueDict[key] = value
    
    # Testing print.  Remove.
    print(valueDict)
        
                
        
    
    # if 'PASS_MAX_DAYS' in loginFile.read():
    #     loginFile.close()
    #     print('True')
        
check_password_policy()