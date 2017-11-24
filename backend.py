#!/usr/bin/python3

import os
        
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
        Represents how many times a user may attempt to change passwored
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
       
