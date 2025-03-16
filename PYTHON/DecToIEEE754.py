def Fun():
    Answer=float(input("Give a decimal float value to transfer to IEEE754 standard hexadecimal : "))
    if Answer<0:
        S=1
        Answer*=-1
    else:
        S=0
    n=1
    if Answer>2**n:
        while Answer>2**(n+1):
            n+=1
    else:
        while Answer<2**n:
            n-=1
    E=127+n
    Divider=2**n
    MantisStep=(Answer/Divider-1)
    ListMantis=[]

    FinishedMantisLess=False
    for i in range(23):
        MantisStep*=2
        if MantisStep<1:
            Mantisnbr=0
        else:
            Mantisnbr=1
            MantisStep-=1
        ListMantis.append(Mantisnbr)
        if MantisStep==0:
            FinishedMantisLess=True
    if MantisStep<0.5:
        FinishedMantisLess=True
    
    EBinary=""
    exptwo=7
    for i in range(8):
        if E>=2**exptwo:
            EBinary+="1"
            E-=2**exptwo
        else:
            EBinary+="0"
        exptwo-=1
    FinalBinaryList=[str(S)]
    for i in range(len(EBinary)):
        FinalBinaryList.append(EBinary[i])
    for i in ListMantis:
        FinalBinaryList.append(str(i))
    
    if not FinishedMantisLess:
        R=True
        IndFinalBinaryList=-1
        while R:
            if FinalBinaryList[IndFinalBinaryList]=="1":
                FinalBinaryList[IndFinalBinaryList]="0"
            else:
                FinalBinaryList[IndFinalBinaryList]="1"
                R=False
            IndFinalBinaryList-=1
    
    FinalBinaryStr="".join(FinalBinaryList)
    
    ListCharacter="0123456789ABCDEF"
    BinaryExtract=""
    HexaFinal=""
    DecOfChar=0
    Ind=0
    for i in range(8):
        for k in range(4):
            BinaryExtract+=FinalBinaryStr[Ind]
            Ind+=1
        exptwo=3
        for IndExtract in range(4):
            if BinaryExtract[IndExtract]=="1":
                DecOfChar+=2**exptwo
            exptwo-=1
        HexaFinal+=ListCharacter[DecOfChar]
        DecOfChar=0
        BinaryExtract=""
    
    print("Decimal    :     "+str(((-1)**S)*Answer))
    print("Binary     :     "+FinalBinaryStr)
    print("Hexadecimal:     "+HexaFinal)
Fun()