Dim nbr_dossiers
Dim nbr_sous_dossiers
Dim chemin
Dim pas
Dim Liste_dossiers
Dim cancel
Liste_dossiers = Cstr("Liste des dossiers cr"+chr(233)+chr(233)+"s :"+chr(13)+chr(10))
pas = 0
Set obj = CreateObject("Scripting.FileSystemObject")
chemin = InputBox("Quel est le chemin ?","Informations")
If Not IsEmpty(chemin) Then
nbr_dossiers = InputBox("Combien de dossiers faut-il faire ?","Informations")
nbr_sous_dossiers = MsgBox("Y a t'il des sous-dossiers a cr"+chr(233)+"er ?",36,"Informations")
If nbr_sous_dossiers=6 Then
nbr_sous_dossiers = 1
Else
nbr_sous_dossiers = 0
End If

While pas<Cint(nbr_dossiers)

If pas=0 Then

nom_dossier = InputBox("Quel nom voulez vous donner au dossier num"+chr(233)+"ro "& pas+1 &" ?","Informations")
If Not obj.FolderExists(Cstr(chemin)+"\"+Cstr(nom_dossier)) Then
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier))
Else
While obj.FolderExists(Cstr(chemin)+"\"+Cstr(nom_dossier))
nom_dossier = InputBox("Ce dossier existe d"+chr(233)+"j"+chr(224)+", veuillez entrer un autre nom.","Informations")
Wend
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier))
End If
Liste_dossiers=Liste_dossiers+Cstr(nom_dossier)

ElseIf pas=1 Then

nom_dossier = InputBox("Quel nom voulez vous donner au dossier num"+chr(233)+"ro "& pas+1 &" ?"+chr(13)+chr(10)+Liste_dossiers,"Informations")
If Not obj.FolderExists(Cstr(chemin)+"\"+Cstr(nom_dossier)) Then
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier))
Else
While obj.FolderExists(Cstr(chemin)+"\"+Cstr(nom_dossier))
nom_dossier = InputBox("Ce dossier existe d"+chr(233)+"j"+chr(224)+", veuillez entrer un autre nom.","Informations")
Wend
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier))
End If
Liste_dossiers = Liste_dossiers+","+Cstr(nom_dossier)

Else

nom_dossier = InputBox("Quel nom voulez vous donner au dossier num"+chr(233)+"ro "& pas+1 &" ?"+chr(13)+chr(10)+Liste_dossiers,"Informations")
If Not obj.FolderExists(Cstr(chemin)+"\"+Cstr(nom_dossier)) Then
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier))
Else
While obj.FolderExists(Cstr(chemin)+"\"+Cstr(nom_dossier))
nom_dossier = InputBox("Ce dossier existe d"+chr(233)+"j"+chr(224)+", veuillez entrer un autre nom.","Informations")
Wend
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier))
End If
Liste_dossiers = Liste_dossiers+","+Cstr(nom_dossier)
End If

If nbr_sous_dossiers=1 Then
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier)+"\COURS")
a = obj.CreateFolder(Cstr(chemin)+"\"+Cstr(nom_dossier)+"\HORS-COURS")
End If
pas = pas+1
Wend
a=MsgBox("Vos dossiers ont "+chr(233)+"t"+chr(233)+" cr"+chr(233)+chr(233)+"s avec succ"+chr(232)+"s !"+chr(13)+chr(10)+Liste_dossiers,64,"Fin du processus")
End If