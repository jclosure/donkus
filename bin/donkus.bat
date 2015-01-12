@Echo OFF

set BINPATH=%~dp0
cd "%BINPATH%..\"
python "runserver.py" %*