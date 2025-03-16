Set objFSO=CreateObject("Scripting.FileSystemObject")
Set objSH=CreateObject("WScript.Shell")
Dim actualpath, newfolder
a=msgbox("Oh ! Bonjour, tu vas bien ?", 36, "Ah, bonjour !")
If a=6 Then
a=msgbox("En fait, j'en ai strictement rien "+chr(224)+" faire...", 64, "Balec")
Else
a=msgbox("Ooooh :(... J'en ai rien "+chr(224)+" faire... Cheh", 64, "Cheh")
End If
a=msgbox("BON ! C'est pas tout, on est pas l"+chr(224)+" pour parler de nos vies ! Moi j'ai d'autres gens "+chr(224)+" pirater !", 16, "J'ai d'autres chats "+chr(224)+" fouetter")
a=msgbox("O"+chr(249)+" en "+chr(233)+"tais-je ? Ah oui... Ben ?! Tu m'a l'air "+chr(233)+"tonn"+chr(233)+" ! Ah oui... Je suis un hacker c'est "+chr(231)+"a ?", 36, "Eh oui ;)")
If a=7 Then
a=msgbox("Une autre raison ? Ne r"+chr(233)+"ponds pas j'en ai rien "+chr(224)+" faire", 64, "Ah bah c'est pas moi ^^")
Else
a=msgbox("BOUH ! Je vais effacer tous tes fichiers ! Haha, je pourrais mais je vais jouer un peu avant avec toi, comme un chat et une souris, tu vois ? Le chat joue avec la souris, elle en meurt mais passons ce d"+chr(233)+"tail ;)", 48, "Je vais tout effacer !")
End If
a=msgbox("J'ai du potentiel, je vais te montrer...", 64, "Observe !")
a=msgbox("Je ne sais pas moi... Je peux cr"+chr(233)+"er des dossiers et fichiers rigolos, vois par exemple :", 64, "D"+chr(233)+"monstration !")
actualpath = objFSO.GetAbsolutePathName(".")
newfolder = actualpath+"\Eheh"
objFSO.CreateFolder(newfolder)
objSH.Run(newfolder)
WScript.Sleep 1000
objFSO.CreateFolder(newfolder+"\1Donc voil"+chr(224))
WScript.Sleep 1000
objFSO.CreateFolder(newfolder+"\2Je peux cr"+chr(233)+"er")
WScript.Sleep 1000
objFSO.CreateFolder(newfolder+"\3Des dossiers")
WScript.Sleep 1000
objFSO.CreateFolder(newfolder+"\4"+chr(192)+" volont"+chr(233))
a=msgbox("Et c'est pas tout ! Tiens :", 48, "C'est pas fini !")
Set OutPutFile = objFSO.OpenTextFile(newfolder+"\Yey.txt" ,8 , True)
objSH.Run(newfolder+"\Yey.txt")
OutPutFile.Write "Re-Bonjour !"
OutPutFile.Write chr(13)+chr(10)+"Donc voilà je peux aussi te blinder de dossiers et de textes, certes, mais aussi de bugs... Là je contrôle ton ordi d'une certaine façon."