Set objSh = CreateObject("WScript.Shell")
Dim actualpath
actualpath = WScript.ScriptFullName
objSh.Run actualpath
Dim a
a=0
While a<>2
a=msgbox("Oups")
Wend