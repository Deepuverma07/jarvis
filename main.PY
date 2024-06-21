import os

import eel


eel.init("www")

# open at host



os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# tell which file is of frontend

eel.start('index.html', mode=None, host='localhost', block=True)

