# get_os_name_if_elif_else.py

import platform

osName = platform.system()

# if os is windows
if osName == "Windows":
    print('Windows detected')

# if os is Linux
elif osName == "Linux":
    print('Linux detected')

# else os not known
else:
    print('os not known')

input('')

