#!/usr/bin/python3

def check_sudo_user_password():
  """
  Function checks if sudo users are set to require passwords
  
  Searches the /etc/sudoers file for the entry 'NOPASSWD'
  If this setting exists in the file, then that means a sudo user 
  will be able to execute sudo commands without having to use a password
  
  Parameters
  ----------
  None
     
  Returns
  -------
  bool
    True if sudo users must use passwords to execute sudo commands
    False if sudo users do not have to use passwords to execute sudo commands
      
  """
  # String to search
  str = 'NOPASSWD' 
  
  # Storing open file object for the /etc/sudoers file
  sudoFile = open("/etc/sudoers", 'r')
  
  # If str exists in sudoFile, return True
  # else return false
  if str in sudoFile.read():
    print('true')
    sudoFile.close()
    return True
  else:
    sudoFile.close()
    print('false')
    return False


  
    
    
    