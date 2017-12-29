C:\Python27\Scripts\Pyinstaller.exe --upx-dir="C:\Program Files\UPX\upx.exe" client.spec

move /y dist\scanner.exe .
del *.pyc
REM del *.spec
rmdir /s /q dist
rmdir /s /q build