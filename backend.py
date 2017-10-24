import pwd


def check_user_exists(userName):
  """
    Function checks if user exists on the machine
    @params:
      userName {string}: Username of user being checked for existence
  """
  try:
    # Searches /etc/passwd for entry with username userName
    pwd.getpwnam(userName)
    print("User '%s' exists" % (userName))
  except KeyError:
    print("User '%s' does not exist" % (userName))
  


  
