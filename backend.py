import pwd


def check_user_exists(userName):
  """
    Checks if user exists on the machine
    
    Parameters
    ----------
    userName : str
      Username of user being checked for existence
      
    Returns
    -------
    int
      0 if user exists
      1 if user does not exist
      
  """
  try:
    # Searches /etc/passwd for entry with username userName
    pwd.getpwnam(userName)
    print("User '%s' exists" % (userName))
    return 0
  except KeyError:
    print("User '%s' does not exist" % (userName))
    return 1
  


check_user_exists('test')
