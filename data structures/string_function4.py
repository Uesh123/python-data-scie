file= input('enter the file name')
if file.endswith('.png'):
    print('its a png file')
elif file.endswith('.jpg'):
    print("its a jpgfile")
elif file.endswith('.docx'):
    print('its a doc file')
elif file.endswith('.py')or file.endswith('ipynb'):
    print('its a python file')
else:
    print('unidentified file, destroy your computer')