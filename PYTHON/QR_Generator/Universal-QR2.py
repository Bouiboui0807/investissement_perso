print("Que transformer en code QR ?")
DataStr = str(input("> "))
print("")
print("Quel niveau de récupération souhaitez-vous ?")
print("")
print("L : 7%")
print("M : 15%")
print("Q : 25%")
print("H : 30%")
ECC_Req = str(input("Choisissez L, M, Q, ou H : "))
print("")
print("Voulez vous en avoir une image ?")
print("")
print("1 : Oui")
print("2 : Non")
ImgRep = str(input("Choisissez 1 ou 2 : "))
print("")

def Fill8(Var,times):
    if len(Var) < times*8:
        Numb = times*8-len(Var)
        Final = Numb*"0" + Var
    else:
        Final = Var
    return(Final)

def BinTra(Var):
    ind = 0
    final = ""
    while Var >= 2**(ind):
        ind += 1
    for i in range(ind):
        if Var >= 2**(ind-i-1):
            final += "1"
            Var -= 2**(ind-i-1)
        else:
            final += "0"
    return(final)

def ConvertChar(Char):
    Nbr = ord(Char)
    if Nbr <= 126 and Nbr >= 32:
        Section = 1
    elif Nbr <= 191 and Nbr >= 161:
        Section = 2
    elif Nbr <= 255 and Nbr >=192:
        Section = 3
    else:
        Section = 4
    if Section == 1:
        AttLen = 1
        TraChar = Fill8(BinTra(Nbr),1)
    elif Section == 2:
        AttLen = 2
        TraChar = "11000010" + Fill8(BinTra(Nbr),1)
    elif Section ==3:
        AttLen = 2
        TraChar = "11000011" + Fill8(BinTra(Nbr-64),1)
    else:
        AttLen = 0
        TraChar = "Le charactère suivant est indisponible pour le mode de QR code utilisé : " + Char
    return(TraChar,AttLen,Section)

Spec_len_V_ECC = [[17,14,11,7],
                  [32,26,20,14],
                  [53,42,32,24],
                  [78,62,46,34],
                  [106,84,60,44],
                  [134,106,74,58],
                  [154,122,86,64],
                  [192,152,108,84],
                  [230,180,130,98],
                  [271,213,151,119],
                  [321,251,177,137],
                  [367,287,203,155],
                  [425,331,241,177],
                  [458,362,258,194],
                  [520,412,292,220],
                  [586,450,322,250],
                  [644,504,364,280],
                  [718,560,394,310],
                  [792,624,442,338],
                  [858,666,482,382],
                  [929, 711, 509, 403],
                  [1003, 779, 565, 439],
                  [1091, 857, 611, 461],
                  [1171, 911, 661, 511],
                  [1273, 997, 715, 535],
                  [1367, 1059, 751, 593],
                  [1465, 1125, 805, 625],
                  [1528, 1190, 868, 658],
                  [1628, 1264, 908, 698],
                  [1732, 1370, 982, 742],
                  [1840, 1452, 1030, 790],
                  [1952, 1538, 1112, 842],
                  [2068, 1628, 1168, 898],
                  [2188, 1722, 1228, 958],
                  [2303, 1809, 1283, 983],
                  [2431, 1911, 1351, 1051],
                  [2563, 1989, 1423, 1093],
                  [2699, 2099, 1499, 1139],
                  [2809, 2213, 1579, 1219],
                  [2953, 2331, 1663, 1273]]

VersionInfoSup7 = ["000111110010010100",
"001000010110111100",
"001001101010011001",
"001010010011010011",
"001011101111110110",
"001100011101100010",
"001101100001000111",
"001110011000001101",
"001111100100101000",
"010000101101111000",
"010001010001011101",
"010010101000010111",
"010011010100110010",
"010100100110100110",
"010101011010000011",
"010110100011001001",
"010111011111101100",
"011000111011000100",
"011001000111100001",
"011010111110101011",
"011011000010001110",
"011100110000011010",
"011101001100111111",
"011110110101110101",
"011111001001010000",
"100000100111010101",
"100001011011110000",
"100010100010111010",
"100011011110011111",
"100100101100001011",
"100101010000101110",
"100110101001100100",
"100111010101000001",
"101000110001101001"]

Blocks_Spec = [[[19,7,1,19,0,0],[16,10,1,16,0,0],[13,13,1,13,0,0],[9,17,1,9,0,0]],
               [[34,10,1,34,0,0],[28,16,1,28,0,0],[22,22,1,22,0,0],[16,28,1,16,0,0]],
               [[55,15,1,55,0,0],[44,26,1,44,0,0],[34,18,2,17,0,0],[26,22,2,13,0,0]],
               [[80,20,1,80,0,0],[64,18,2,32,0,0],[48,26,2,24,0,0],[36,16,4,9,0,0]],
               [[108,26,1,108,0,0],[86,24,2,43,0,0],[62,18,2,15,2,16],[46,22,2,11,2,12]],
               [[136,18,2,68,0,0],[108,16,4,27,0,0],[76,24,4,19,0,0],[60,28,4,15,0,0]],
               [[156,20,2,78,0,0],[124,18,4,31,0,0],[88,18,2,14,4,15],[66,26,4,13,1,14]],
               [[194,24,2,97,0,0],[154,22,2,38,2,39],[110,22,4,18,2,19],[86,26,4,14,2,15]],
               [[232,30,2,116,0,0],[182,22,3,36,2,37],[132,20,4,16,4,17],[100,24,4,12,4,13]],
               [[274,18,2,68,2,69],[216,26,4,43,1,44],[154,24,6,19,2,20],[122,28,6,15,2,16]],
               [[324,20,4,81,0,0],[254,30,1,50,4,51],[180,28,4,22,4,23],[140,24,3,12,8,13]],
               [[370,24,2,92,2,93],[290,22,6,36,2,37],[206,26,4,20,6,21],[158,28,7,14,4,15]],
               [[428,26,4,107,0,0],[334,22,8,37,1,38],[244,24,8,20,4,21],[180,22,12,11,4,12]],
               [[461,30,3,115,1,116],[365,24,4,40,5,41],[261,20,11,16,5,17],[197,24,11,12,5,13]],
               [[523,22,5,87,1,88],[415,24,5,41,5,42],[295,30,5,24,7,25],[223,24,11,12,7,13]],
               [[589,24,5,98,1,99],[453,28,7,45,3,46],[325,24,15,19,2,20],[253,30,3,15,13,16]],
               [[647,28,1,107,5,108],[507,28,10,46,1,47],[367,28,1,22,15,23],[283,28,2,14,17,15]],
               [[721,30,5,120,1,121],[563,26,9,43,4,44],[397,28,17,22,1,23],[313,28,2,14,19,15]],
               [[795,28,3,113,4,114],[627,26,3,44,11,45],[445,26,17,21,4,22],[341,26,9,13,16,14]],
               [[861,28,3,107,5,108],[669,26,3,41,13,42],[485,30,15,24,5,25],[385,28,15,15,10,16]],
               [[932,28,4,116,4,117],[714,26,17,42,0,0],[512,28,17,22,6,23],[406,30,19,16,6,17]],
               [[1006,28,2,111,7,112],[782,28,17,46,0,0],[568,30,7,24,16,25],[442,24,34,13,0,0]],
               [[1094,30,4,121,5,122],[860,28,4,47,14,48],[614,30,11,24,14,25],[464,30,16,15,14,16]],
               [[1174,30,6,117,4,118],[914,28,6,45,14,46],[664,30,11,24,16,25],[514,30,30,16,2,17]],
               [[1276,26,8,106,4,107],[1000,28,8,47,13,48],[718,30,7,24,22,25],[538,30,22,15,13,16]],
               [[1370,28,10,114,2,115],[1062,28,19,46,4,47],[754,28,28,22,6,23],[596,30,33,16,4,17]],
               [[1468,30,8,122,4,123],[1128,28,22,45,3,46],[808,30,8,23,26,24],[628,30,12,15,28,16]],
               [[1531,30,3,117,10,118],[1193,28,3,45,23,46],[871,30,4,24,31,25],[661,30,11,15,31,16]],
               [[1631,30,7,116,7,117],[1267,28,21,45,7,46],[911,30,1,23,37,24],[701,30,19,15,26,16]],
               [[1735,30,5,115,10,116],[1373,28,19,47,10,48],[985,30,15,24,25,25],[745,30,23,15,25,16]],
               [[1843,30,13,115,3,116],[1455,28,2,46,29,47],[1033,30,42,24,1,25],[793,30,23,15,28,16]],
               [[1955,30,17,115,0,0],[1541,28,10,46,23,47],[1115,30,10,24,35,25],[845,30,19,15,35,16]],
               [[2071,30,17,115,1,116],[1631,28,14,46,21,47],[1171,30,29,24,19,25],[901,30,11,15,46,16]],
               [[2191,30,13,115,6,116],[1725,28,14,46,23,47],[1231,30,44,24,7,25],[961,30,59,16,1,17]],
               [[2306,30,12,121,7,122],[1812,28,12,47,26,48],[1286,30,39,24,14,25],[986,30,22,15,41,16]],
               [[2434,30,6,121,14,122],[1914,28,6,47,34,48],[1354,30,46,24,10,25],[1054,30,2,15,64,16]],
               [[2566,30,17,122,4,123],[1992,28,29,46,14,47],[1426,30,49,24,10,25],[1096,30,24,15,46,16]],
               [[2702,30,4,122,18,123],[2102,28,13,46,32,47],[1502,30,48,24,14,25],[1142,30,42,15,32,16]],
               [[2812,30,20,117,4,118],[2216,28,40,47,7,48],[1582,30,43,24,22,25],[1222,30,10,15,67,16]],
               [[2956,30,19,118,6,119],[2334,28,18,47,31,48],[1666,30,34,24,34,25],[1276,30,20,15,61,16]]]

Remainders = [0,7,7,7,7,7,0,0,0,0,0,0,0,3,3,3,3,3,3,3,4,4,4,4,4,4,4,3,3,3,3,3,3,3,0,0,0,0,0,0]

def Level(ECC_Req):
    if ECC_Req == "L" or ECC_Req == "l":
        Level = 0
    elif ECC_Req == "M" or ECC_Req == "m":
        Level = 1
    elif ECC_Req == "Q" or ECC_Req == "q":
        Level = 2
    elif ECC_Req == "H" or ECC_Req == "h":
        Level = 3
    return(Level)

LevECC = Level(ECC_Req)

LenDataAct = 0
ErrorMsg = ""
for i in range(len(DataStr)):
    TraChar, AttLen, Section = ConvertChar(DataStr[i])
    if Section != 4:
        LenDataAct += AttLen
    else:
        ErrorMsg = TraChar

if LenDataAct > (Spec_len_V_ECC[39])[LevECC] or ErrorMsg != "":
    if LenDataAct > (Spec_len_V_ECC[39])[LevECC]:
        print("Le message à encoder est trop long pour un QR code !")
        print("")
        print("Souhaitez vous :")
        print("1) Changer le message")
        print("2) Changer le niveau de récupération")
        Answer = int(input("Choisissez 1 ou 2 : "))
        print("")
    if ErrorMsg != "":
        print(ErrorMsg)
        print("")
        Answer = 1
    if Answer == 1:
        while len(DataStr) > (Spec_len_V_ECC[39])[LevECC] or ErrorMsg != "":
            print("Que transformer en code QR ?")
            DataStr = str(input("> "))
            LenDataAct = 0
            ErrorMsg = ""
            for i in range(len(DataStr)):
                TraChar, AttLen, Section = ConvertChar(DataStr[i])
                if Section != 4:
                    LenDataAct += AttLen
                else:
                    ErrorMsg = TraChar
            if ErrorMsg != "":
                print(ErrorMsg)
            if LenDataAct > (Spec_len_V_ECC[39])[LevECC]:
                print("Le message est encore trop long pour ce niveau de récupération.")
    else:
        while len(DataStr) > (Spec_len_V_ECC[39])[LevECC]:
            print("Quel niveau de récupération souhaitez-vous ?")
            print("")
            print("L : 7%")
            print("M : 15%")
            print("Q : 25%")
            print("H : 30%")
            ECC_Req = str(input("Choisissez L, M, Q, ou H : "))
            print("")
            LevECC = Level(ECC_Req)
            if len(DataStr) > (Spec_len_V_ECC[39])[LevECC]:
                print("Le message est encore trop long pour ce niveau de récupération.")

from math import*
import turtle as trl
from PIL import Image

trl.hideturtle()
trl.speed("fastest")
wn = trl.Screen()
trl.title("Code QR")

Version = 1
while len(DataStr) > (Spec_len_V_ECC[Version-1])[LevECC]:
    Version += 1

LenDataMax = (Spec_len_V_ECC[Version-1])[LevECC]

Version7sup = False
if Version >= 7:
    VersionInfo = VersionInfoSup7[Version-7]
    Version7sup = True

ECC_length = ((Blocks_Spec[Version-1])[LevECC])[1]

G1_Blocks = ((Blocks_Spec[Version-1])[LevECC])[2]
Len_Blocks1 = ((Blocks_Spec[Version-1])[LevECC])[3]
G2_Blocks = ((Blocks_Spec[Version-1])[LevECC])[4]
Len_Blocks2 = ((Blocks_Spec[Version-1])[LevECC])[5]

Rows = 21 + 4*(Version-1)
Cols = 21 + 4*(Version-1)

wn.setup(60+Rows*4,60+Cols*4)

if Version < 10:
    Char_Len_Count = 1
else:
    Char_Len_Count = 2

Remaind = Remainders[Version-1]

CoorPaterns = [[18],
[22],
[26],
[30],
[34],
[22,38],
[24,42],
[26,46],
[28,50],
[30,54],
[32,58],
[34,62],
[26,46,66],
[26,48,70],
[26,50,74],
[30,54,78],
[30,56,82],
[30,58,86],
[34,62,90],
[28,50,72,94],
[26,50,74,98],
[30,54,78,102],
[28,54,80,106],
[32,58,84,110],
[30,58,86,114],
[34,62,90,118],
[26,50,74,98,122],
[30,54,78,102,126],
[26,52,78,104,130],
[30,56,82,108,134],
[34,60,86,112,138],
[30,58,86,114,142],
[34,62,90,118,146],
[30,54,78,102,126,150],
[24,50,76,102,128,154],
[28,54,80,106,132,158],
[32,58,84,110,136,162],
[26,54,82,110,138,166],
[30,58,86,114,142,170]]

if Version != 1:
    Patern_used = CoorPaterns[Version-2]
    NoPatern = False
else:
    NoPatern = True

Each_Patern = []

def Att_Coo_Patern(Patern_used):
    Coor = []
    Len = len(Patern_used)
    if Len == 1:
        Coor = [2*[Patern_used[0]]]
    else:
        for i in range(Len-1):
            CoorAct = [Patern_used[i],6]
            Coor.append(CoorAct)
        for i in range(Len-1):
            Coor.append([6,Patern_used[i]])
            for j in range(Len):
                Coor.append([Patern_used[j],Patern_used[i]])
        for i in range(Len):
            CoorAct = [Patern_used[i],Patern_used[Len-1]]
            Coor.append(CoorAct)
    return Coor

if not NoPatern:
    Each_Patern = Att_Coo_Patern(Patern_used)

DataF = []

def Prep_DataF(DataF,Rows,Cols):
    for i in range(Rows):
        Line = Cols * "0"
        DataF.append(Line)
    return(DataF)

def Place_Rulers(DataF,Rows,Cols):
    for i in range(Cols):
        if i%2 == 0:
            DataF[6] = (DataF[6])[:i] + "1" + (DataF[6])[i+1:]
    for i in range(Rows):
        if i%2 == 0:
            DataF[i] = (DataF[i])[:6] + "1" + (DataF[i])[7:]
    return(DataF)

def Place_Reco(DataF,Rows,Cols):
    DataF[0] = 7*"1" + (DataF[0])[7:Cols-7] + 7*"1"
    DataF[6] = 7*"1" + (DataF[6])[7:Cols-7] + 7*"1"
    DataF[Rows-7] = 7*"1" + (DataF[Rows-7])[7:]
    DataF[Rows-1] = 7*"1" + (DataF[Rows-1])[7:]
    DataF[1] = "1000001" + (DataF[1])[7:Cols-7] + "1000001"
    DataF[5] = "1000001" + (DataF[5])[7:Cols-7] + "1000001"
    DataF[Rows-6] = "1000001" + (DataF[Rows-6])[7:]
    DataF[Rows-2] = "1000001" + (DataF[Rows-2])[7:]
    for i in range(3):
        DataF[2+i] = "1011101" + (DataF[2+i])[7:Cols-7] + "1011101"
    for i in range(3):
        DataF[Rows-5+i] = "1011101" + (DataF[Rows-5+i])[7:]
    DataF[Rows-8] = (DataF[Rows-8])[:8] + "1" + (DataF[Rows-8])[9:]
    return(DataF)

def Place_Scalers(DataF,Each_Patern):
    for item in Each_Patern:
        x = item[0]
        y = item[1]
        ActLi = DataF[y-2]
        ActLi = ActLi[:x-2] + "11111" + ActLi[x+3:]
        DataF[y-2] = ActLi
        ActLi = DataF[y-1]
        ActLi = ActLi[:x-2] + "10001" + ActLi[x+3:]
        DataF[y-1] = ActLi
        ActLi = DataF[y]
        ActLi = ActLi[:x-2] + "10101" + ActLi[x+3:]
        DataF[y] = ActLi
        ActLi = DataF[y+1]
        ActLi = ActLi[:x-2] + "10001" + ActLi[x+3:]
        DataF[y+1] = ActLi
        ActLi = DataF[y+2]
        ActLi = ActLi[:x-2] + "11111" + ActLi[x+3:]
        DataF[y+2] = ActLi
    return(DataF)

def Form_Version(VersionInfo):
    Horiz = []
    Verti = []
    for i in range(3):
        Line = ""
        for j in range(6):
            Line += VersionInfo[17-i-3*j]
        Horiz.append(Line)
    for i in range(6):
        Line = ""
        for j in range(3):
            Line += VersionInfo[17-3*i-j]
        Verti.append(Line)
    return(Horiz,Verti)

def Place_Version(DataF,Horiz,Verti,Cols,Rows):
    for i in range(6):
        for j in range(3):
            DataF[i] =(DataF[i])[:Cols-11] + Verti[i]+ (DataF[i])[Cols-8:]
    for i in range(3):
        for j in range(6):
            DataF[Rows-11+i] = Horiz[i]+ (DataF[Rows-11+i])[6:]
    return(DataF)

DataF = Prep_DataF(DataF,Rows,Cols)
DataF = Place_Rulers(DataF,Rows,Cols)
DataF = Place_Reco(DataF,Rows,Cols)
DataF = Place_Scalers(DataF,Each_Patern)

if Version7sup:
    Horiz,Verti = Form_Version(VersionInfo)
    DataF = Place_Version(DataF,Horiz,Verti,Cols,Rows)

NumbScal = len(Each_Patern)

rptPattern = ["11101100", "00010001"]

def Encodechar(Data):
    final = ""
    for i in range(len(Data)):
        TraChar, AttLen, Section = ConvertChar(Data[i])
        final += TraChar
    final += 4*"0"
    return(final)

def FillDL(Data, rpt, LenDataAct, MaxLen):
    Rest = MaxLen - LenDataAct
    for i in range(Rest):
        Data += rpt[i%2]
    return(Data)

def SplitMess(Message):             #For ECC
    ListNumbs = []
    for item in Message:
        Numbs = []
        Actu = item
        for i in range(int(len(item)/8)):
            FNumb = 0
            actuNBbin = Actu[:8]
            Actu = Actu[8:]
            for j in range(8):
                if actuNBbin[j] == "1":
                    FNumb += 2**(7-j)
            Numbs.append(FNumb)
        ListNumbs.append(Numbs)
    return(ListNumbs)

def Grouping(DataLong,LenBlock1,LenBlock2,Blocks1,Blocks2):
    Blocks = []
    for i in range(Blocks1):
        Blocks.append(DataLong[:LenBlock1*8])
        DataLong = DataLong[LenBlock1*8:]
    for i in range(Blocks2):
        Blocks.append(DataLong[:LenBlock2*8])
        DataLong = DataLong[LenBlock2*8:]
    return(Blocks)

Mode = "0100" #Byte Mode

def Organize_DC(Mode,DataStr,LenDataMax,rptPatern,CharLenCount,LenBlock1,LenBlock2,Blocks1,Blocks2,LenDataAct):
    DataLong = Mode
    Count = Fill8(BinTra(LenDataAct),CharLenCount)
    DataLong += Count
    DataLong += Encodechar(DataStr)
    DataLong = FillDL(DataLong, rptPatern,LenDataAct,LenDataMax)
    Blocks = Grouping(DataLong,LenBlock1,LenBlock2,Blocks1,Blocks2)
    return(Blocks)
    

Blocks = Organize_DC(Mode,DataStr,LenDataMax,rptPattern,Char_Len_Count,Len_Blocks1,Len_Blocks2,G1_Blocks,G2_Blocks,LenDataAct)
ListNumbersECC = SplitMess(Blocks)

def generate_galois_field():
    gf_exp = [0] * 512
    gf_log = [0] * 256

    x = 1
    for i in range(255):
        gf_exp[i] = x
        gf_log[x] = i
        x <<= 1
        if x & 0x100:
            x ^= 0x11d

    for i in range(255, 512):
        gf_exp[i] = gf_exp[i - 255]

    return gf_exp, gf_log

def rs_generator_poly(degree, gf_exp, gf_log):
    gen = [1]
    for i in range(degree):
        next_gen = [0] * (len(gen) + 1)
        for j in range(len(gen)):
            next_gen[j] ^= gen[j]
            next_gen[j + 1] ^= gf_exp[(gf_log[gen[j]] + i) % 255] if gen[j] != 0 else 0
        gen = next_gen
    return [g % 256 for g in gen]

def rs_encode_message(message, ecc_length, gf_exp, gf_log):
    gen_poly = rs_generator_poly(ecc_length, gf_exp, gf_log)
    message_poly = list(message) + [0] * ecc_length

    for i in range(len(message)):
        coef = message_poly[i]
        if coef != 0:
            for j in range(len(gen_poly)):
                message_poly[i + j] ^= gf_exp[(gf_log[coef] + gf_log[gen_poly[j]]) % 255]

    return message_poly[-ecc_length:]

def GenerateECCs(ListNumbsECC,ecc_length,Len_Blocks1,Len_Blocks2):
    gf_exp, gf_log = generate_galois_field()
    ecc_list = []

    for i in range(Len_Blocks1):
        message_group_1 = ListNumbsECC[i]
        ecc_codewords_1 = rs_encode_message(message_group_1, ecc_length, gf_exp, gf_log)
        ecc_list.append(ecc_codewords_1)
    for i in range(Len_Blocks2):
        message_group_2 = ListNumbsECC[i+G1_Blocks]
        ecc_codewords_2 = rs_encode_message(message_group_2, ecc_length, gf_exp, gf_log)
        ecc_list.append(ecc_codewords_2)

    ecc_list_bin = []
    for item in ecc_list:
        BinList = []
        for var in item:
            BinVar = BinTra(var)
            BinVar = Fill8(BinVar, 1)
            BinList.append(BinVar)
        ecc_list_bin.append(BinList)
    return(ecc_list_bin)

ECCs = GenerateECCs(ListNumbersECC,ECC_length,G1_Blocks,G2_Blocks)

def Organize(ECCs, Blocks, Len_Blocks1, G1_Blocks, G2_Blocks, ECC_length):
    DataL = ""
    ECCL = ""
    for i in range(Len_Blocks1):
        for j in range(G1_Blocks + G2_Blocks):
            Block = Blocks[j]
            IntStr = Block[:8]
            Block = Block[8:]
            Blocks[j] = Block
            DataL += IntStr
    if G2_Blocks != 0:
        for i in range(G2_Blocks):
            Block = Blocks[i+G1_Blocks]
            IntStr = Block[:8]
            Block = Block[8:]
            Blocks[i+G1_Blocks] = Block
            DataL += IntStr
    for k in range(ECC_length):
        for l in range(G1_Blocks + G2_Blocks):
            item = ECCs[l]
            ECCL += item[k]
    return(DataL,ECCL)

DataLong, ECCf = Organize(ECCs, Blocks, Len_Blocks1, G1_Blocks, G2_Blocks, ECC_length)
FINALDATA = DataLong + ECCf + Remaind*"0"

if not NoPatern:
    NubPat = len(CoorPaterns[Version-2]) - 1
    BetPat1 = (CoorPaterns[Version-2])[0] - 11
    if NubPat >= 2:
        BetPat2 = (CoorPaterns[Version-2])[1] - (CoorPaterns[Version-2])[0] - 5
    else:
        BetPat2 = BetPat1

def UP(FINALDATA,DataF,height,xstart,ystart):
    for i in range(height):
        ActuStr = DataF[ystart-i]
        ActuStr = ActuStr[:xstart] + FINALDATA[1] + FINALDATA[0] + ActuStr[xstart+2:]
        FINALDATA = FINALDATA[2:]
        DataF[ystart-i] = ActuStr
    return(DataF, FINALDATA)

def DO(FINALDATA,DataF,height,xstart,ystart):
    for i in range(height):
        ActuStr = DataF[ystart+i]
        ActuStr = ActuStr[:xstart] + FINALDATA[1] + FINALDATA[0] + ActuStr[xstart+2:]
        FINALDATA = FINALDATA[2:]
        DataF[ystart+i] = ActuStr
    return(DataF, FINALDATA)

def LOUNGE(FINALDATA,DataF,height,xstart,ystart,orientation):
    if orientation:
        for i in range(height):
            ActuStr = DataF[ystart-i]
            ActuStr = ActuStr[:xstart] + FINALDATA[0] + ActuStr[xstart+1:]
            FINALDATA = FINALDATA[1:]
            DataF[ystart-i] = ActuStr
    else:
        for i in range(height):
            ActuStr = DataF[ystart+i]
            ActuStr = ActuStr[:xstart] + FINALDATA[0] + ActuStr[xstart+1:]
            FINALDATA = FINALDATA[1:]
            DataF[ystart+i] = ActuStr
    return(DataF, FINALDATA)

def OVERPAT(Times,BetPat2,DataF,FINALDATA,orientation,xstart,ystart,pixonst):
    if orientation:
        DataF,FINALDATA = UP(FINALDATA,DataF,pixonst,xstart,ystart)
        for i in range(Times):
            DataF,FINALDATA = UP(FINALDATA,DataF,BetPat2,xstart,ystart-pixonst-5*(i+1)-BetPat2*i)
    else:
        DataF,FINALDATA = DO(FINALDATA,DataF,pixonst,xstart,ystart)
        for i in range(Times):
            DataF,FINALDATA = DO(FINALDATA,DataF,BetPat2,xstart,ystart+pixonst+5*(i+1)+BetPat2*i)
    return(DataF,FINALDATA)

def LONGLOUNGE(Times,BetPat1,BetPat2,orientation,DataF,FINALDATA,xstart,ystart):
    if orientation:
        DataF,FINALDATA = UP(FINALDATA,DataF,4,xstart,ystart)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,5,xstart,ystart-4,True)
        for i in range(Times):
            DataF,FINALDATA = UP(FINALDATA,DataF,BetPat2,xstart,ystart-4-5*(i+1)-BetPat2*i)
            DataF,FINALDATA = LOUNGE(FINALDATA,DataF,5,xstart,ystart-4-(i+1)*(5+BetPat2),True)
        DataF,FINALDATA = UP(FINALDATA,DataF,BetPat1,xstart,8+BetPat1)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,2,xstart,8,True)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,2,xstart,5,True)
        DataF,FINALDATA = UP(FINALDATA,DataF,4,xstart,3)
    else:
        DataF,FINALDATA = DO(FINALDATA,DataF,4,xstart,0)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,2,xstart,4,False)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,2,xstart,7,False)
        DataF,FINALDATA = DO(FINALDATA,DataF,BetPat1,xstart,9)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,5,xstart,9+BetPat1,False)
        for i in range(Times):
            DataF,FINALDATA = DO(FINALDATA,DataF,BetPat2,xstart,BetPat1+9+5*(i+1)+BetPat2*i)
            DataF,FINALDATA = LOUNGE(FINALDATA,DataF,5,xstart,BetPat1+9+(i+1)*(5+BetPat2),False)
        DataF,FINALDATA = DO(FINALDATA,DataF,4,xstart,ystart-3)
    return(DataF,FINALDATA)

def MEDLOUNGE(Times,BetPat1,BetPat2,DataF,FINALDATA,xstart,ystart):
    DataF,FINALDATA = UP(FINALDATA,DataF,4,xstart,ystart)
    DataF,FINALDATA = LOUNGE(FINALDATA,DataF,5,xstart,ystart-4,True)
    for i in range(Times):
        DataF,FINALDATA = UP(FINALDATA,DataF,BetPat2,xstart,ystart-4-5*(i+1)-BetPat2*i)
        DataF,FINALDATA = LOUNGE(FINALDATA,DataF,5,xstart,ystart-4-(i+1)*(5+BetPat2),True)
    DataF,FINALDATA = UP(FINALDATA,DataF,BetPat1+2,xstart,8+BetPat1)
    return(DataF,FINALDATA)

def LONG(DataF,FINALDATA,xstart,ystart,orientation):
    if orientation:
        DataF,FINALDATA = UP(FINALDATA,DataF,ystart-6,xstart,ystart)
        DataF,FINALDATA = UP(FINALDATA,DataF,6,xstart,5)
    else:
        DataF,FINALDATA = DO(FINALDATA,DataF,6,xstart,0)
        DataF,FINALDATA = DO(FINALDATA,DataF,ystart-6,xstart,7)
    return(DataF,FINALDATA)

def REPAT(DataF,FINALDATA,NubPat,xstart,Rows,orientation):
    if orientation:
        DataF, FINALDATA = OVERPAT(NubPat,BetPat2,DataF,FINALDATA,True,xstart,Rows-1,4)
        DataF, FINALDATA = UP(FINALDATA,DataF,BetPat1,xstart,8+BetPat1)
        DataF, FINALDATA = UP(FINALDATA,DataF,4,xstart,3)
        DataF, FINALDATA = DO(FINALDATA,DataF,4,xstart-2,0)
        DataF, FINALDATA = OVERPAT(NubPat,BetPat2,DataF,FINALDATA,False,xstart-2,9,BetPat1)
        DataF, FINALDATA = DO(FINALDATA,DataF,4,xstart-2,Rows-4)
        DataF, FINALDATA = LONGLOUNGE(NubPat,BetPat1,BetPat2,True,DataF,FINALDATA,xstart-4,Rows-1)
    else:
        DataF, FINALDATA = DO(FINALDATA,DataF,4,xstart,0)
        DataF, FINALDATA = OVERPAT(NubPat,BetPat2,DataF,FINALDATA,False,xstart,9,BetPat1)
        DataF, FINALDATA = DO(FINALDATA,DataF,4,xstart,Rows-4)
        DataF, FINALDATA = OVERPAT(NubPat,BetPat2,DataF,FINALDATA,True,xstart-2,Rows-1,4)
        DataF, FINALDATA = UP(FINALDATA,DataF,BetPat1,xstart-2,8+BetPat1)
        DataF, FINALDATA = UP(FINALDATA,DataF,4,xstart-2,3)
        DataF, FINALDATA = LONGLOUNGE(NubPat,BetPat1,BetPat2,False,DataF,FINALDATA,xstart-4,Rows-1)
    return(DataF,FINALDATA)

def FillQR(FINALDATA, DataF, NubPat, BetPat1, BetPat2, Version, Cols, Rows):
    DataF, FINALDATA = UP(FINALDATA,DataF,Rows-9,Cols-2,Rows-1)
    DataF, FINALDATA = DO(FINALDATA,DataF,Rows-9,Cols-4,9)
    DataF, FINALDATA = OVERPAT(NubPat,BetPat2,DataF,FINALDATA,True,Cols-6,Rows-1,4)
    DataF, FINALDATA = UP(FINALDATA,DataF,BetPat1,Cols-6,8+BetPat1)
    DataF, FINALDATA = OVERPAT(NubPat,BetPat2,DataF,FINALDATA,False,Cols-8,9,BetPat1)
    DataF, FINALDATA = DO(FINALDATA,DataF,4,Cols-8,Rows-4)
    DataF, FINALDATA = MEDLOUNGE(NubPat,BetPat1,BetPat2,DataF,FINALDATA,Cols-10,Rows-1)
    SavesPoss = int((BetPat2-1)//4)
    Rest = False
    orientationprev = True
    invorientationprev = False
    if (BetPat2-1)%4 == 2:
        Rest = True
    if Version < 7:
        DataF,FINALDATA = UP(FINALDATA,DataF,6,Cols-10,5)
        for i in range(SavesPoss):
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-12-4*i,Rows-1,False)
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-14-4*i,Rows-1,True)
        if Rest:
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-9-BetPat1,Rows-1,False)
    else:
        DataF, FINALDATA = LOUNGE(FINALDATA,DataF,6,Cols-12,0,False)
        DataF, FINALDATA = DO(FINALDATA,DataF,Rows-7,Cols-12,7)
        Times = SavesPoss
        if not Rest:
            Times -= 1
        for i in range(Times):
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-14-4*i,Rows-1,True)
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-16-4*i,Rows-1,False)
        if not Rest:
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-9-BetPat2,Rows-1,True)
            DataF, FINALDATA = REPAT(DataF,FINALDATA,NubPat,Cols-11-BetPat2,Rows,False)
        else:
            DataF, FINALDATA = REPAT(DataF,FINALDATA,NubPat,Cols-11-BetPat2,Rows,True)
    for NP in range(NubPat-1):
        if not Rest:
            for i in range(SavesPoss):
                DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-17-BetPat2*(NP+1)-4*i-5*NP,Rows-1,orientationprev)
                DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-19-BetPat2*(NP+1)-4*i-5*NP,Rows-1,invorientationprev)
            DataF, FINALDATA = REPAT(DataF,FINALDATA,NubPat,Cols-17-BetPat2*(NP+1)-4*SavesPoss-5*NP,Rows,orientationprev)
            interm = orientationprev
            orientationprev = invorientationprev
            invorientationprev = interm
            lastori = orientationprev
        else:
            for i in range(SavesPoss):
                DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-17-BetPat2*(NP+1)-4*i-5*NP,Rows-1,False)
                DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-19-BetPat2*(NP+1)-4*i-5*NP,Rows-1,True)
            DataF, FINALDATA = LONG(DataF,FINALDATA,Cols-17-BetPat2*(NP+1)-4*SavesPoss-5*NP,Rows-1,False)
            DataF, FINALDATA = REPAT(DataF,FINALDATA,NubPat,Cols-19-BetPat2*(NP+1)-4*SavesPoss-5*NP,Rows,True)
        SavesPoss = int((BetPat2-1)//4)
    if Version >= 7:
        orient = False
        if not Rest and NubPat>1:
            if not lastori:
                orient = True
        invorient = True
        if orient:
            invorient = False
        SavesPoss2 = int((BetPat1-1)//4)
        Rest2 = False
        if (BetPat1-1)%4 == 2:
            Rest2 = True
        for i in range(SavesPoss2):
            DataF, FINALDATA = LONG(DataF,FINALDATA,6+BetPat1-4*i,Rows-1,orient)
            DataF, FINALDATA = LONG(DataF,FINALDATA,4+BetPat1-4*i,Rows-1,invorient)
        if Rest2:
            DataF, FINALDATA = LONG(DataF,FINALDATA,9,Rows-1,orient)
    if Version >= 7:
        DataF, FINALDATA = OVERPAT(NubPat-1,BetPat2,DataF,FINALDATA,True,7,Rows-9,BetPat2+1)
        DataF, FINALDATA = UP(FINALDATA,DataF,BetPat1,7,8+BetPat1)
        DataF, FINALDATA = OVERPAT(NubPat-1,BetPat2,DataF,FINALDATA,False,4,9,BetPat1)
        DataF, FINALDATA = DO(FINALDATA,DataF,BetPat2-2,4,Rows-9-BetPat2)
        DataF, FINALDATA = UP(FINALDATA,DataF,Rows-20,2,Rows-12)
        DataF, FINALDATA = DO(FINALDATA,DataF,Rows-20,0,9)
    else:
        DataF, FINALDATA = UP(FINALDATA,DataF,BetPat1+1,7,Rows-9)
        DataF, FINALDATA = DO(FINALDATA,DataF,BetPat1+1,4,9)
        DataF, FINALDATA = UP(FINALDATA,DataF,Rows-17,2,Rows-9)
        DataF, FINALDATA = DO(FINALDATA,DataF,Rows-17,0,9)
    return(DataF)

def FillQRV1(DataF, FINALDATA):
    for i in range(2):
        DataF, FINALDATA = UP(FINALDATA,DataF,12,19-4*i,20)
        DataF, FINALDATA = DO(FINALDATA,DataF,12,17-4*i,9)
    DataF, FINALDATA = UP(FINALDATA,DataF,14,11,20)
    DataF, FINALDATA = UP(FINALDATA,DataF,6,11,5)
    DataF, FINALDATA = DO(FINALDATA,DataF,6,9,0)
    DataF, FINALDATA = DO(FINALDATA,DataF,14,9,7)
    DataF, FINALDATA = UP(FINALDATA,DataF,4,7,12)
    DataF, FINALDATA = DO(FINALDATA,DataF,4,4,9)
    DataF, FINALDATA = UP(FINALDATA,DataF,4,2,12)
    DataF, FINALDATA = DO(FINALDATA,DataF,4,0,9)
    return(DataF)

if NoPatern:
    DataFINAL = FillQRV1(DataF,FINALDATA)
else:
    DataFINAL = FillQR(FINALDATA, DataF, NubPat, BetPat1, BetPat2, Version, Cols, Rows)

LevMaskList = [["111011111000100","111001011110011","111110110101010","111100010011101","110011000101111","110001100011000","110110001000001","110100101110110"],
                ["101010000010010","101000100100101","101111001111100","101101101001011","100010111111001","100000011001110","100111110010111","100101010100000"],
                ["011010101011111","011000001101000","011111100110001","011101000000110","010010010110100","010000110000011","010111011011010","010101111101101"],
                ["001011010001001","001001110111110","001110011100111","001100111010000","000011101100010","000001001010101","000110100001100","000100000111011"]]

IntList = LevMaskList[LevECC]

def Formula0(Col,Row):
    if (Col+Row)%2 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula1(Row):
    if Row%2 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula2(Col):
    if Col%3 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula3(Col,Row):
    if (Col+Row)%3 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula4(Col,Row):
    if (floor(Row/2)+floor(Col/3))%2 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula5(Col,Row):
    if ((Row*Col)%2)+((Row*Col)%3) == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula6(Col,Row):
    if (((Row*Col)%2)+((Row*Col)%3))%2 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Formula7(Col,Row):
    if (((Row+Col)%2)+((Row*Col)%3))%2 == 0:
        Value = True
    else:
        Value = False
    return(Value)

def Affect(Col,Row,DataF,formN):
    if formN == 0:
        Value = Formula0(Col,Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 1:
        Value = Formula1(Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 2:
        Value = Formula2(Col)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 3:
        Value = Formula3(Col,Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 4:
        Value = Formula4(Col,Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 5:
        Value = Formula5(Col,Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 6:
        Value = Formula6(Col,Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 7:
        Value = Formula7(Col,Row)
        if Value:
            if (DataF[Row])[Col] == "1":
                DataF[Row] = (DataF[Row])[:Col] + "0" + (DataF[Row])[Col+1:]
            else:
                DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    if formN == 8:
        if (DataF[Row])[Col] == "1":
            DataF[Row] = (DataF[Row])[:Col] + "2" + (DataF[Row])[Col+1:]
        else:
            DataF[Row] = (DataF[Row])[:Col] + "1" + (DataF[Row])[Col+1:]
    return(DataF)

def Rule1(DataF,Cols,Rows):
    Score = 0
    for Row in range(Rows):
        Sum = 0
        while Sum <= Cols-1:
            if (DataF[Row])[Sum:Sum+5] == "11111":
                Score += 3
                ind = 0
                while Sum+5+ind <= Cols-1 and (DataF[Row])[Sum+5+ind] == "1":
                    Score += 1
                    ind += 1
                Sum += 5+ind
            elif (DataF[Row])[Sum:Sum+5] == "00000":
                Score += 3
                ind = 0
                while Sum+5+ind <= Cols-1 and (DataF[Row])[Sum+5+ind] == "0":
                    Score += 1
                    ind += 1
                Sum += 5+ind
            else:
                Sum += 1
    Sc = 0
    for Col in range(Cols):
        Sum = 0
        while Sum <= Rows-1:
            linesum = ""
            if Rows-Sum >= 5:
                for Row in range(5):
                    linesum += (DataF[Row+Sum])[Col]
                if linesum == "11111":
                    Score += 3
                    Sc += 3
                    ind = 0
                    while Sum+ind+5 <= Rows-1 and (DataF[Sum+ind+5])[Col] == "1":
                        Score += 1
                        Sc += 1
                        ind += 1
                    Sum += 5+ind
                elif linesum == "00000":
                    Score += 3
                    Sc += 3
                    ind = 0
                    while Sum+ind+5 <= Rows-1 and (DataF[Sum+ind+5])[Col] == "0":
                        Score += 1
                        Sc += 1
                        ind += 1
                    Sum += 5+ind
                else:
                    Sum += 1
            else:
                Sum = Cols
    return(Score)

def Rule2(DataF,Cols,Rows):
    Score = 0
    for Row in range(Rows-1):
        for Col in range(Cols-1):
            Square = ""
            Square = (DataF[Row])[Col:Col+2]
            Square += (DataF[Row+1])[Col:Col+2]
            if Square == "1111" or Square == "0000":
                Score += 3
    return(Score)

def Rule3(DataF,Cols,Rows):
    Score = 0
    for Row in range(Rows):
        for Col in range(Cols-10):
            if (DataF[Row])[Col:Col+11] == "10111010000" or (DataF[Row])[Col:Col+11] == "00001011101":
                Score += 40
    for Row in range(Rows-11):
        for Col in range(Cols):
            linesum = ""
            for i in range(11):
                linesum += (DataF[Row+i])[Col]
            if linesum == "10111010000" or linesum == "00001011101":
                Score += 40
    return(Score)

def Rule4(DataF,Cols,Rows):
    Total = Rows*Cols
    bdots = 0
    for Row in range(Rows):
        for Col in range(Cols):
            if (DataF[Row])[Col] == "1":
                bdots += 1
    Percentage = bdots/Total*100
    infnumb = (Percentage//5)*5
    supnumb = infnumb+5
    if infnumb-50 < 0:
        infnumb = 50-infnumb
    else:
        infnumb -= 50
    if supnumb-50 < 0:
        supnumb = 50-supnumb
    else:
        supnumb -= 50
    infnumb /= 5
    supnumb /= 5
    if infnumb < supnumb:
        Score = 10*infnumb
    else:
        Score = 10*supnumb
    return(Score)

def InsMLECC(IntList,Mask,DataF):
    DataF[8] = (IntList[Mask])[:6] + "1" + (IntList[Mask])[6:8] + (DataF[8])[9:Cols-8] + (IntList[Mask])[7:]
    DataF[7] = (DataF[7])[:8] + (IntList[Mask])[8] + (DataF[7])[9:]
    for Row in range(6):
        DataF[5-Row] = (DataF[5-Row])[:8] + (IntList[Mask])[9+Row] + (DataF[5-Row])[9:]
    for Row in range(7):
        DataF[Rows-Row-1] = (DataF[Rows-Row-1])[:8] + (IntList[Mask])[Row] + (DataF[Rows-Row-1])[9:]
    return(DataF)

def MASKBLOCK(DataF,xlen,ylen,xstart,ystart,Nfor):
    for Row in range(ylen):
        for Col in range(xlen):
            DataF = Affect(Col+xstart,Row+ystart,DataF,Nfor)
    return(DataF)

def ApplyMask1(DataF,Nfor):
    DataF = MASKBLOCK(DataF,4,6,9,0,Nfor)
    DataF = MASKBLOCK(DataF,4,2,9,7,Nfor)
    DataF = MASKBLOCK(DataF,6,4,0,9,Nfor)
    DataF = MASKBLOCK(DataF,14,4,7,9,Nfor)
    DataF = MASKBLOCK(DataF,12,8,9,13,Nfor)
    return(DataF)

def ApplyMask(DataF,Nfor,NubPat,BetPat1,BetPat2,Cols,Rows):
    if NubPat >= 1:
        DataF = MASKBLOCK(DataF,BetPat1+5*NubPat+(NubPat-1)*BetPat2+BetPat2-2,4,9,0,Nfor)
        DataF = MASKBLOCK(DataF,BetPat1,2,9,4,Nfor)
        for i in range(NubPat-1):
            DataF = MASKBLOCK(DataF,BetPat2,2,9+BetPat1+5*(i+1)+BetPat2*i,4,Nfor)
        DataF = MASKBLOCK(DataF,BetPat2-2,2,9+BetPat1+5*NubPat+BetPat2*(NubPat-1),4,Nfor)
        DataF = MASKBLOCK(DataF,BetPat1,2,9,7,Nfor)
        for i in range(NubPat-1):
            DataF = MASKBLOCK(DataF,BetPat2,2,9+BetPat1+5*(i+1)+BetPat2*i,7,Nfor)
        DataF = MASKBLOCK(DataF,BetPat2+1,2,9+BetPat1+5*NubPat+BetPat2*(NubPat-1),7,Nfor)
        DataF = MASKBLOCK(DataF,4,BetPat1+5*NubPat+(NubPat-1)*BetPat2+BetPat2-2,0,9,Nfor)
        DataF = MASKBLOCK(DataF,2,BetPat1,4,9,Nfor)
        for i in range(NubPat-1):
            DataF = MASKBLOCK(DataF,2,BetPat2,4,9+BetPat1+5*(i+1)+BetPat2*i,Nfor)
        DataF = MASKBLOCK(DataF,2,BetPat2-2,4,9+BetPat1+5*NubPat+BetPat2*(NubPat-1),Nfor)
        DataF = MASKBLOCK(DataF,2,BetPat1,7,9,Nfor)
        for i in range(NubPat-1):
            DataF = MASKBLOCK(DataF,2,BetPat2,7,9+BetPat1+5*(i+1)+BetPat2*i,Nfor)
        DataF = MASKBLOCK(DataF,2,BetPat2+1,7,9+BetPat1+5*NubPat+BetPat2*(NubPat-1),Nfor)
        DataF = MASKBLOCK(DataF,Cols-9,BetPat1,9,9,Nfor)
        for i in range(NubPat):
            DataF = MASKBLOCK(DataF,Cols-9,BetPat2,9,9+BetPat1+5*(i+1)+BetPat2*i,Nfor)
        for i in range(NubPat+1):
            DataF = MASKBLOCK(DataF,BetPat1,5,9,9+BetPat1+i*(5+BetPat2),Nfor)
            for j in range(NubPat):
                DataF = MASKBLOCK(DataF,BetPat2,5,9+BetPat1+5*(j+1)+BetPat2*j,9+BetPat1+i*(5+BetPat2),Nfor)
            DataF = MASKBLOCK(DataF,4,5,Cols-4,9+BetPat1+i*(5+BetPat2),Nfor)
        DataF = MASKBLOCK(DataF,Cols-9,4,9,Rows-4,Nfor)
    else:
        DataF = MASKBLOCK(DataF,BetPat1+1,6,9,0,Nfor)
        DataF = MASKBLOCK(DataF,BetPat1+1,2,9,7,Nfor)
        DataF = MASKBLOCK(DataF,6,BetPat1+1,0,9,Nfor)
        DataF = MASKBLOCK(DataF,2,BetPat1+1,7,9,Nfor)
        DataF = MASKBLOCK(DataF,Cols-9,BetPat1,9,9,Nfor)
        DataF = MASKBLOCK(DataF,BetPat1,5,9,Rows-9,Nfor)
        DataF = MASKBLOCK(DataF,4,5,Cols-4,Rows-9,Nfor)
        DataF = MASKBLOCK(DataF,Cols-9,4,9,Rows-4,Nfor)
    return(DataF)

def PenalScore(DataF,Rows,Cols):
    FScore = Rule1(DataF,Cols,Rows)
    FScore += Rule2(DataF,Cols,Rows)
    FScore += Rule3(DataF,Cols,Rows)
    FScore += Rule4(DataF,Cols,Rows)
    return(FScore)

def ChPattern(NoPatern,DataF,Rows,Cols,IntList):
    Scores = []
    AltData = []
    for item in DataF:
        AltData.append(item)
    for Mask in range(8):
        if NoPatern:
            DataF = []
            for item in AltData:
                DataF.append(item)
            DataF2 = ApplyMask1(DataF,Mask)
            DataF2 = InsMLECC(IntList,Mask,DataF2)
            Scores.append(PenalScore(DataF2,Rows,Cols))
        else:
            DataF = []
            for item in AltData:
                DataF.append(item)
            DataF2 = ApplyMask(DataF,Mask,NubPat,BetPat1,BetPat2,Cols,Rows)
            DataF2 = InsMLECC(IntList,Mask,DataF2)
            Scores.append(PenalScore(DataF2,Rows,Cols))
    Mini = Scores[0]
    Mask = 0
    DataF = []
    for item in AltData:
        DataF.append(item)
    for i in range(7):
        if Scores[i+1] < Mini:
            Mini = Scores[i+1]
            Mask = i+1
    if NoPatern:
        DataFINAL = ApplyMask1(DataF,Mask)
    else:
        DataFINAL = ApplyMask(DataF,Mask,NubPat,BetPat1,BetPat2,Cols,Rows)
    DataFINAL = InsMLECC(IntList,Mask,DataFINAL)
    return(DataFINAL)

DataFINAL = ChPattern(NoPatern,DataFINAL,Rows,Cols,IntList)

def Gener(Data,Cols):
    trl.penup()
    trl.goto(-Cols*2,Cols*2)
    for y in Data:
        for x in range(Cols):
            if y[x] == "0":
                trl.pencolor(1,1,1)
                trl.pendown()
                trl.goto(trl.xcor()+4,trl.ycor())
            else:
                trl.pencolor(0,0,0)
                trl.pendown()
                for i in range(2):
                    trl.goto(trl.xcor(),trl.ycor()-3)
                    trl.goto(trl.xcor()+1,trl.ycor())
                    trl.goto(trl.xcor(),trl.ycor()+3)
                    trl.goto(trl.xcor()+1,trl.ycor())
        trl.penup()
        trl.goto(-Cols*2, trl.ycor()-4)
    trl.done()

if ImgRep == "1":
    Resol = int(input("Nombre de pixels par bit : "))
    ImName = str(input("Nom du fichier : "))
    Im = Image.new('RGB',(Resol*(Cols+8),Resol*(Rows+8)))
    for x in range(Resol*(Cols+8)):
        for y in range(Resol*(Rows+8)):
            Im.putpixel((x,y),(255,255,255))
    for y in range(Rows):
        for x in range(Cols):
            if (DataFINAL[y])[x] == "0":
                rgb = (255,255,255)
            else:
                rgb = (0,0,0)
            for i in range(Resol):
                for j in range(Resol):
                    Im.putpixel(((x+4)*Resol+i,(y+4)*Resol+j),rgb)
    Im.save(ImName + '.png')
    print("")
    print("L'image a été générée avec succès !")

trl.tracer(0,0)
Gener(DataFINAL,Cols)
trl.update()