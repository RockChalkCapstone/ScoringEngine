#!/usr/bin/python3

import os
        
fileList = []
filename = "init"

for entry in os.scandir("/etc/pam.d"):
   if not entry.name.startswith('.') and entry.is_file():
       fileList.append(entry.name)

if "common-password" in fileList:
  filename = "/etc/pam.d/common-password"
  
print(filename)
       
       
# password [success=2 default=ignore] pam_unix.so obscure sha512 minlen=8