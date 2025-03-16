Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objSh = CreateObject("Wscript.Shell")
Set ListPathSelect=CreateObject("System.Collections.ArrayList")
Set ListTypes=CreateObject("System.Collections.ArrayList")
Set ListFilm=CreateObject("System.Collections.ArrayList")
Set ListPaths=CreateObject("System.Collections.ArrayList")
Dim nbrmax, pasPath, Before, LenPath1, RsrchLoseCncl, Canceled, Listf, objrec, dossier, path1, path2, objrecorigine, ListTypes, SelTypes, pas, FilmToOpen, pathtof, TypeToOpen, Film, SelFilms, FilmName, FilmName_

path1 = "E:\TEST_CDI"			'Erreur numéro 1: Changez le chemin après le signe égal entre guillemets pour le nouveau chemin valide (Ne mettez de \ à la fin)

Canceled=0
RsrchLoseCncl=0
Before=0

Function ListFilmByType()
Set ListTypes=CreateObject("System.Collections.ArrayList")
Set ListFilm=CreateObject("System.Collections.ArrayList")
Set ListPaths=CreateObject("System.Collections.ArrayList")
TypeToOpen=""
pas=1
dossier=""
LenPath1=0
SelTypes=""
If Not objFSO.FolderExists(Cstr(path1)) Then
a = MsgBox("/!\ Erreur num"+chr(233)+"ro 1 /!\"+chr(13)+chr(10)+"Appelez une personne exp"+chr(233)+"riment"+chr(233)+"e pour r"+chr(233)+"gler le probl"+chr(232)+"me"+chr(13)+chr(10)+chr(13)+chr(10)+chr(192)+" l'adresse du correcteur; la ligne o"+chr(249)+" est consign"+chr(233)+" le chemin est la ligne 9 du code",16,"Chemin non existant")
Canceled=1
Else
LenPath1=Len(path1)+2

For Each objFolder In objFSO.GetFolder(path1).SubFolders
dossier=Mid(Cstr(objFolder),Cint(LenPath1))
ListTypes.Add dossier
Next

For Each Types In ListTypes
SelTypes=SelTypes+Cstr(pas)+". "+Cstr(Types)+chr(13)+chr(10)
pas=pas+1
Next
pas=1

nbrmax=0
For Each Items In ListTypes
nbrmax=nbrmax+1
Next
TypeToOpen=InputBox("Choisissez le type du film avec le nombre correspondant"+chr(13)+chr(10)+SelTypes,"Type du film")
If Not IsEmpty(TypeToOpen) Then
While Not IsNumeric(TypeToOpen) And Canceled=0
TypeToOpen=InputBox("Veuillez entrer le type du film avec un nombre compris entre 1 et "+Cstr(nbrmax)+chr(13)+chr(10)+SelTypes,"Type du film")
If IsEmpty(TypeToOpen) Then
Canceled=1
End If
Wend
While nbrmax-TypeToOpen<0 Or TypeToOpen<=0 Or Not IsNumeric(TypeToOpen) And Canceled=0
TypeToOpen=InputBox("Choisissez le type du film avec un nombre compris entre 1 et "+Cstr(nbrmax)+chr(13)+chr(10)+SelTypes,"Type du film")
If IsEmpty(TypeToOpen) Then
Canceled=1
End If
Wend
If Canceled=0 Then
If ListTypes.item(TypeToOpen-1)="DOCUMENTAIRE" Then
For Each Cote In objFSO.GetFolder(path1+"\DOCUMENTAIRE").SubFolders
For Each objFilm In objFSO.GetFolder(Cstr(Cote)).SubFolders
Film=Mid(Cstr(objFilm),Len(Cstr(Cote))+2)
ListFilm.Add Film
ListPaths.Add objFilm
Next
Next

Else
For Each objFilm In objFSO.GetFolder(path1+"\"+ListTypes.item(TypeToOpen-1)).SubFolders
Film=Mid(Cstr(objFilm),LenPath1+Len(ListTypes.item(TypeToOpen-1))+1)
ListFilm.Add Film
ListPaths.Add objFilm
Next
End If

Else
a=msgbox("Vous avez annul"+chr(233)+" votre recherche.",64,"Recherche annul"+chr(233)+"e")
End If

Else
a=msgbox("Vous avez annul"+chr(233)+" votre recherche.",64,"Recherche annul"+chr(233)+"e")
Canceled=1
End If
End If
End Function

Function KeyWord()
objrec = InputBox("Donnez un mot-cl"+chr(233)+" du titre."+chr(13)+chr(10)+chr(201)+"vitez les accents pour nous aider ;)"+chr(13)+chr(10)+"Exemple:"+chr(13)+chr(10)+"Napol"+chr(233)+"on Bonaparte -> Napol"+chr(233)+"on"+chr(13)+chr(10)+"Napol"+chr(233)+"on -> Napoleon","Mot-cl"+chr(233),"Entrez le mot ici")
If Not IsEmpty(objrec) Then
objrec=Cstr(objrec)
objrecorigine = Ucase(Left(objrec,1))+Mid(objrec,2)
objrec = Ucase(Cstr(objrec))

Else
a=msgbox("Vous avez annul"+chr(233)+" votre recherche.",64,"Recherche annul"+chr(233)+"e")
Canceled=1
End If
End Function

Function SelectTheFilm()
Listf=0
SelFilms=""
Call ListFilmByType()
If Canceled=0 Then
Call KeyWord()
pas=1
pasPath=0

Set ListPathSelect=CreateObject("System.Collections.ArrayList")
For Each Film In ListFilm
If InStr(1,Film,objrec,1)<>0 Then
Listf=Listf+1
SelFilms=SelFilms+Cstr(pas)+". "+Cstr(Film)+chr(13)+chr(10)
ListPathSelect.Add ListPaths.item(pasPath)
pas=pas+1
End If
pasPath=pasPath+1
Next
End If
End Function

Call SelectTheFilm()

While RsrchLoseCncl=0 And Not Canceled=1
If Listf=0 Then
If Before=0 Then
RetryCancel=msgbox("Nous sommes d"+chr(233)+"sol"+chr(233)+"s, aucun film n'a le mot "+objrecorigine+" dans son titre. Voulez-vous r"+chr(233)+"essayer avec un autre mot cl"+chr(233)+" ?",21,"Oups...")
Else
RetryCancel=msgbox("Voulez-vous r"+chr(233)+"essayer avec un autre mot cl"+chr(233)+" ?",21,"R"+chr(233)+"essayer ?")
End If
Before=0
If RetryCancel=4 Then
Call SelectTheFilm()
Else
RsrchLoseCncl=1
a=msgbox("Vous avez annul"+chr(233)+" votre recherche.",64,"Recherche annul"+chr(233)+"e")
End If

Else
RsrchLoseCncl=1
If Listf=1 Then
FilmToOpen=MsgBox("Nous vous avons trouv"+chr(233)+" un film :)"+chr(13)+chr(10)+SelFilms+chr(13)+chr(10)+"Est-ce le bon film ?",36,"Ouverture du film")
If FilmToOpen=7 Then
Listf=0
RsrchLoseCncl=0
Before=1
Else
FilmToOpen=1
End If
Else
FilmToOpen=MsgBox("Nous vous avons trouv"+chr(233)+" quelques films :)"+chr(13)+chr(10)+SelFilms+chr(13)+chr(10)+"Le film recherch"+chr(233)+" est-il dans la liste ?",36,"Ouverture du film")
If FilmToOpen=7 Then
Listf=0
RsrchLoseCncl=0
Before=1

Else
nbrmax=0
For Each Items In ListPathSelect
nbrmax=nbrmax+1
Next
FilmToOpen=InputBox("Choisissez un film dans la liste."+chr(13)+chr(10)+SelFilms,"Ouverture du film")
If IsEmpty(FilmToOpen) Then
Canceled=1
a=msgbox("Vous avez annul"+chr(233)+" votre recherche.",64,"Recherche annul"+chr(233)+"e")
Else
While Not IsNumeric(TypeToOpen) And Canceled=0
TypeToOpen=InputBox("Choisissez un film dans la liste avec un nombre compris entre 1 et "+Cstr(nbrmax)+chr(13)+chr(10)+SelTypes,"Type du film")
If IsEmpty(TypeToOpen) Then
Canceled=1
End If
Wend
While nbrmax-FilmToOpen<0 Or TypeToOpen<=0 And Canceled=0
FilmToOpen=InputBox("Choisissez un film dans la liste avec un nombre compris entre 1 et "+Cstr(nbrmax)+chr(13)+chr(10)+SelFilms,"Ouverture du film")
If IsEmpty(TypeToOpen) Then
Canceled=1
End If
Wend
End If
End If
End If

If RsrchLoseCncl=1 And Not Canceled=1 Then
FilmName=ListPathSelect.Item(FilmToOpen-1)
FilmName_=Replace(FilmName," ","_",1,-1)
objFSO.MoveFolder FilmName, FilmName_
objSh.Run(FilmName_)
WScript.Sleep 1500
objFSO.MoveFolder FilmName_, FilmName
WScript.Sleep 100
a=MsgBox("Recherche effectu"+chr(233)+"e avec succ"+chr(232)+"s."+chr(13)+chr(10)+"Effectuez un clic droit sur le film pour l'ouvrir avec VLC"+chr(13)+chr(10)+"Code: Arthur LE BARS ;)",4160,"Merci !")
End If
End If
Wend