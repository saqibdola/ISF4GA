LEU = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
PHE = ['TTT', 'TTC']
SER= ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
TYR = ['TAT', 'TAC']
STOP = ['TAA', 'TAG', 'TGA']
CYS = ['TGT', 'TGC']
PRO = ['CCT', 'CCC', 'CCA', 'CCG'] #
HIS = ['CAT', 'CAC']
GLN = ['CAA', 'CAG']
ARG = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA','AGG']
LLE = ['ATT', 'ATC', 'ATA']
THR =['ACT', 'ACC', 'ACA', 'ACG']
ASN = ['AAT', 'AAC']
LYS = ['AAA', 'AAG']
VAL = ['GTT', 'GTC', 'GTA', 'GTG']
ALA = ['GCT', 'GCC', 'GCA', 'GCG']
ASP = ['GAT', 'GAC']
GLU = ['GAA', 'GAG']
GLY = ['GGT', 'GGC', 'GGA', 'GGG']
TRP = ['TGG']
MET = ['ATG']

LUEAA= [0]*6
PHEAA = [0]*2
SERAA= [0]*6


n = 3
i = 0
cc = 0
codons = 0
array=[0]*21
syncod=[0]*64
#enc1 = [0]*64
cc = 0

with open('seq1.txt') as f1:
    for line in f1:
        if line[0] == '>':
            pass
        else:
            print(line)
            while i + n <= len(line):
                asdf = line[i:i + n]
                codons+= 1
                print(asdf)
                if asdf == LEU[0]:
                        syncod[0] += 1
                    elif asdf == LEU[1]:
                        syncod[1] += 1
                    elif asdf == LEU[2]:
                        syncod[2] += 1
                    elif asdf == LEU[3]:
                        syncod[3] += 1
                    elif asdf == LEU[4]:
                        syncod[4] += 1
                    elif asdf == LEU[5]:
                        syncod[5] += 1

                elif asdf in PHE:
                    array[1] += 1
                    if asdf == PHE[0]:
                        syncod[6] += 1
                    elif asdf == PHE[1]:
                        syncod[7] += 1
                elif asdf in SER:
                    array[2] += 1
                    if asdf == SER[0]:
                        syncod[8] += 1
                    elif asdf == SER[1]:
                        syncod[9] += 1
                    elif asdf == SER[2]:
                        syncod[10] += 1
                    elif asdf == SER[3]:
                        syncod[11] += 1
                    elif asdf == SER[4]:
                        syncod[12] += 1
                    elif asdf == SER[5]:
                        syncod[13] += 1

                elif asdf in TYR:
                    array[3] += 1
                    if asdf == TYR[0]:
                        syncod[14] += 1
                    elif asdf == TYR[1]:
                        syncod[15] += 1

                elif asdf in STOP:
                    array[4] += 1
                    if asdf == STOP[0]:
                        syncod[16] +=1
                    elif asdf == STOP[1]:
                        syncod[17] +=1
                    elif asdf == STOP[2]:
                        syncod[18] += 1

                elif asdf in CYS:
                    array[5] += 1
                    if asdf == CYS[0]:
                        syncod[19] += 1
                    elif asdf == CYS[1]:
                        syncod[20] += 1

                elif asdf in PRO:
                    array[6] += 1
                    if asdf == PRO[0]:
                        syncod[21] += 1
                    elif asdf == PRO[1]:
                        syncod[22] += 1
                    elif asdf == PRO[2]:
                        syncod[23] += 1
                    elif asdf == PRO[3]:
                        syncod[24] += 1

                elif asdf in HIS:
                    array[7] += 1
                    if asdf == HIS[0]:
                        syncod[25] += 1
                    elif asdf == HIS[1]:
                        syncod[26] += 1

                elif asdf in GLN:
                    array[8] += 1
                    if asdf == GLN[0]:
                        syncod[27] += 1
                    elif asdf == GLN[1]:
                        syncod[28] += 1

                elif asdf in ARG:
                    array[9] += 1
                    if asdf == ARG[0]:
                        syncod[29] += 1
                    elif asdf == ARG[1]:
                        syncod[30] += 1
                    elif asdf == ARG[2]:
                        syncod[31] += 1
                    elif asdf == ARG[3]:
                        syncod[32] += 1
                    elif asdf == ARG[4]:
                        syncod[33] += 1
                    elif asdf == ARG[5]:
                        syncod[34] += 1
                elif asdf in LLE:
                    array[10] += 1
                    if asdf == LLE[0]:
                        syncod[35] += 1
                    elif asdf == LLE[1]:
                        syncod[36] += 1
                    elif asdf == LLE[2]:
                        syncod[37] += 1

                elif asdf in THR:
                    array[11] += 1
                    if asdf == THR[0]:
                        syncod[38] += 1
                    elif asdf == THR[1]:
                        syncod[39] += 1
                    elif asdf == THR[2]:
                        syncod[40] += 1
                    elif asdf == THR[3]:
                        syncod[41] += 1

                elif asdf in ASN:
                    array[12] += 1
                    if asdf == ASN[0]:
                        syncod[42] += 1
                    elif asdf == ASN[1]:
                        syncod[43] += 1

                elif asdf in LYS:
                    array[13] += 1
                    if asdf == LYS[0]:
                        syncod[44] += 1
                    elif asdf == LYS[1]:
                        syncod[45] +=1

                elif asdf in VAL:
                    array[14] += 1
                    if asdf == VAL[0]:
                        syncod[46] += 1
                    elif asdf == VAL[1]:
                        syncod[47] += 1
                    elif asdf == VAL[2]:
                        syncod[48] += 1
                    elif asdf == VAL[3]:
                        syncod[49] += 1

                elif asdf in ALA:
                    array[15] += 1
                    if asdf == ALA[0]:
                        syncod[50] += 1
                    elif asdf == ALA[1]:
                        syncod[51] += 1
                    elif asdf == ALA[2]:
                        syncod[52] += 1
                    elif asdf == ALA[3]:
                        syncod[53] += 1

                elif asdf in ASP:
                    array[16] += 1
                    if asdf == ASP[0]:
                        syncod[54] += 1
                    elif asdf == ASP[1]:
                        syncod[55] += 1

                elif asdf in GLU:
                    array[17] += 1
                    if asdf == GLU[0]:
                        syncod[56] += 1
                    elif asdf == GLU[1]:
                        syncod[57] += 1

                elif asdf in GLY:
                    array[18] += 1
                    if asdf == GLY[0]:
                        syncod[58] += 1
                    elif asdf == GLY[1]:
                        syncod[59] += 1
                    elif asdf == GLY[2]:
                        syncod[60] += 1
                    elif asdf == GLY[3]:
                        syncod[61] += 1

                elif asdf in TRP:
                    array[19] += 1
                    if asdf == TRP[0]:
                        syncod[62] += 1

                elif asdf in MET:
                    array[20] += 1
                    if asdf == MET[0]:
                        syncod[63] += 1
                i += n
            i = 0
    #while cc <=codons:
   # while cc <= 20:
            if asdf in LEU:
                    LEU[0]= (syncod[0]/array[0])*(syncod[0]/array[0])
                    LEU[1] = (syncod[1]/array[0])*(syncod[1]/array[0])
                    LEU[2] = (syncod[2]/array[0])*(syncod[2]/array[0])
                    LEU[3] = (syncod[3]/array[0])*(syncod[3]/array[0])
                    LEU[4] = (syncod[4]/array[0])*(syncod[4]/array[0])
                    LEU[5] = (syncod[5]/array[0])*(syncod[5]/array[0])
                    enc2 = sum(LEU)
                    enc3 = (array[0] * enc2) - 1 / array[0] - 1
                    enc4 = 1 / enc3
                    #print(syncod, enc2, enc3, enc4)
    print(codons)
    print(array)
    print(sum(array))
    print(syncod)
    print(sum(syncod))

    #print(array)
















