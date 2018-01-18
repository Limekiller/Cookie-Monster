Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c cookies.bat"
oShell.Run strArgs, 0, false