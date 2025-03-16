def Fun():
    Answer=str(input("Give an IEEE754 standard hexadecimal value to transfer to decimal : "))
    while len(Answer)!=8:
        Answer=str(input("Give an IEEE754 standard hexadecimal value to transfer to decimal : "))
    Answer=Answer.upper()
    HexaChar="0123456789ABCDEF"
    BinaryListStr=""
    for i in range(8):
        CharSelect=Answer[i]
        ValueDecOfHexaChar=HexaChar.find(CharSelect)
        exptwo=3
        for i in range(4):
            if ValueDecOfHexaChar>=2**exptwo:
                BinaryListStr+="1"
                ValueDecOfHexaChar-=2**exptwo
            else:
                BinaryListStr+="0"
            exptwo-=1
    S=int(BinaryListStr[0])
    EStrBinary=(BinaryListStr[1:9])
    MantisStrBinary=(BinaryListStr[9:32])
    EDec=0
    exptwo=7
    for i in range(8):
        if EStrBinary[i]=="1":
            EDec+=2**exptwo
        exptwo-=1
    EDec-=127
    MantisDec=1
    for i in range(23):
        if MantisStrBinary[i]=="1":
            MantisDec+=2**exptwo
        exptwo-=1
    Final=((-1)**S)*(2**EDec)*(MantisDec)
    print("Decimal    :     "+str(Final))
    print("Binary     :     "+BinaryListStr)
    print("Hexadecimal:     "+Answer)
Fun()