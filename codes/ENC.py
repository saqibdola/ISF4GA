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


LEUAA= [0]*6
PHEAA = [0]*2
SERAA= [0]*6
TYRAA = [0]*2
STOPAA = [0]*3
CYSAA  = [0]*2
PROAA = [0]*4
HISAA= [0]*2
GLNAA = [0]*2
ARGAA = [0]*6
LLEAA = [0]*3
THRAA = [0]*4
ASNAA = [0]*2
LYSAA = [0]*2
VALAA = [0]*4
ALAAA = [0]*4
ASPAA = [0]*2
GLUAA = [0]*2
GLYAA = [0]*4
TRPAA = [0]*1
METAA = [0]*1




n = 3
i = 0
cc = 0
codons = 0
array=[0]*21
syncod=[0]*64
#enc1 = [0]*64
cc = 0
enc2=[0]*21
enc3=[0]*21
enc4=[0]*21


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
                if asdf in LEU:
                    array[0] += 1
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
                    LEUAA[0]= (syncod[0]/array[0])*(syncod[0]/array[0])
                    LEUAA[1] = (syncod[1]/array[0])*(syncod[1]/array[0])
                    LEUAA[2] = (syncod[2]/array[0])*(syncod[2]/array[0])
                    LEUAA[3] = (syncod[3]/array[0])*(syncod[3]/array[0])
                    LEUAA[4] = (syncod[4]/array[0])*(syncod[4]/array[0])
                    LEUAA[5] = (syncod[5]/array[0])*(syncod[5]/array[0])
                    enc2[0] = sum(LEUAA)
                    enc3[0] = (array[0] * enc2[0]) - 1 / array[0] - 1
                    enc4[0] = 1 / enc3[0]
            elif asdf in PHE:
                    PHEAA[0]= (syncod[6]/array[1])*(syncod[6]/array[1])
                    PHEAA[1] = (syncod[7]/array[1])*(syncod[6]/array[1])
                    enc2[1] = sum(PHEAA)
                    enc3[1] = (array[1] * enc2[1]) - 1 / array[1] - 1
                    enc4[1] = 1 / enc3[1]
            elif asdf in SER:
                SERAA[0] = (syncod[8] / array[2]) * (syncod[8] / array[2])
                SERAA[1] = (syncod[9] / array[2]) * (syncod[9] / array[2])
                SERAA[2] = (syncod[10] / array[2]) * (syncod[10] / array[2])
                SERAA[3] = (syncod[11] / array[2]) * (syncod[11] / array[2])
                SERAA[4] = (syncod[12] / array[2]) * (syncod[12] / array[2])
                SERAA[5] = (syncod[13] / array[2]) * (syncod[13] / array[2])
                enc2[2] = sum(SERAA)
                enc3[2] = (array[2] * enc2[2]) - 1 / array[2] - 1
                enc4[2] = 1 / enc3[2]
            elif asdf in TYR:
                    TYRAA[0]= (syncod[14]/array[3])*(syncod[14]/array[3])
                    TYRAA[1] = (syncod[15]/array[3])*(syncod[15]/array[3])
                    enc2[3] = sum(TYRAA)
                    enc3[3] = (array[3] * enc2[3]) - 1 / array[3] - 1
                    enc4[3] = 1 / enc3[3]
            elif asdf in STOP:
                    STOPAA[0]= (syncod[16]/array[4])*(syncod[16]/array[4])
                    STOPAA[1] = (syncod[17]/array[4])*(syncod[17]/array[4])
                    STOPAA[2] = (syncod[18]/array[4])*(syncod[18]/array[4])
                    enc2[4] = sum(STOPAA)
                    enc3[4] = (array[4] * enc2[4]) - 1 / array[4] - 1
                    enc4[4] = 1 / enc3[4]
            elif asdf in CYS:
                    CYSAA[0]= (syncod[19]/array[5])*(syncod[19]/array[5])
                    CYSAA[1] = (syncod[20]/array[5])*(syncod[20]/array[5])
                    enc2[5] = sum(CYSAA)
                    enc3[5] = (array[5] * enc2[5]) - 1 / array[5] - 1
                    enc4[5] = 1 / enc3[5]
            if asdf in PRO:
                    PROAA[0]= (syncod[21]/array[6])*(syncod[21]/array[6])
                    PROAA[1] = (syncod[22]/array[6])*(syncod[22]/array[6])
                    PROAA[2] = (syncod[23]/array[6])*(syncod[23]/array[6])
                    PROAA[3] = (syncod[24]/array[6])*(syncod[24]/array[6])
                    enc2[6] = sum(PROAA)
                    enc3[6] = (array[6] * enc2[6]) - 1 / array[6] - 1
                    enc4[6] = 1 / enc3[6]
            elif asdf in HIS:
                    HISAA[0]= (syncod[25]/array[7])*(syncod[25]/array[7])
                    HISAA[1] = (syncod[26]/array[7])*(syncod[26]/array[7])
                    enc2[7] = sum(HISAA)
                    enc3[7] = (array[7] * enc2[7]) - 1 / array[7] - 1
                    enc4[7] = 1 / enc3[7]
            elif asdf in GLN:
                    GLNAA[0]= (syncod[27]/array[8])*(syncod[27]/array[8])
                    GLNAA[1] = (syncod[28]/array[8])*(syncod[28]/array[8])
                    enc2[8] = sum(GLNAA)
                    enc3[8] = (array[8] * enc2[8]) - 1 / array[8] - 1
                    enc4[8] = 1 / enc3[8]
            if asdf in ARG:
                    ARGAA[0]= (syncod[29]/array[9])*(syncod[29]/array[9])
                    ARGAA[1] = (syncod[30]/array[9])*(syncod[30]/array[9])
                    ARGAA[2] = (syncod[31]/array[9])*(syncod[31]/array[9])
                    ARGAA[3] = (syncod[32]/array[9])*(syncod[32]/array[9])
                    ARGAA[4] = (syncod[33]/array[9])*(syncod[33]/array[9])
                    ARGAA[5] = (syncod[34]/array[9])*(syncod[34]/array[9])
                    enc2[9] = sum(ARGAA)
                    enc3[9] = (array[9] * enc2[9]) - 1 / array[9] - 1
                    enc4[9] = 1 / enc3[9]
            elif asdf in LLE:
                    LLEAA[0]= (syncod[35]/array[10])*(syncod[35]/array[10])
                    LLEAA[1] = (syncod[36]/array[10])*(syncod[36]/array[10])
                    LLEAA[2] = (syncod[37]/array[10])*(syncod[37]/array[10])
                    enc2[10] = sum(LLEAA)
                    enc3[10] = (array[10] * enc2[10]) - 1 / array[10] - 1
                    enc4[10] = 1 / enc3[10]
            if asdf in THR:
                    THRAA[0]= (syncod[38]/array[11])*(syncod[38]/array[11])
                    THRAA[1] = (syncod[39]/array[11])*(syncod[39]/array[11])
                    THRAA[2] = (syncod[40]/array[11])*(syncod[40]/array[11])
                    THRAA[3] = (syncod[41]/array[11])*(syncod[41]/array[11])
                    enc2[11] = sum(THRAA)
                    enc3[11] = (array[11] * enc2[11]) - 1 / array[11] - 1
                    enc4[11] = 1 / enc3[11]
            elif asdf in ASN:
                    ASNAA[0]= (syncod[42]/array[12])*(syncod[42]/array[12])
                    ASNAA[1] = (syncod[43]/array[12])*(syncod[43]/array[12])
                    enc2[12] = sum(ASNAA)
                    enc3[12] = (array[12] * enc2[12]) - 1 / array[12] - 1
                    enc4[12] = 1 / enc3[12]
            elif asdf in LYS:
                    LYSAA[0]= (syncod[44]/array[13])*(syncod[44]/array[13])
                    LYSAA[1] = (syncod[45]/array[12])*(syncod[45]/array[13])
                    enc2[13] = sum(LYSAA)
                    enc3[13] = (array[13] * enc2[13]) - 1 / array[13] - 1
                    enc4[13] = 1 / enc3[13]
            if asdf in VAL:
                    VALAA[0]= (syncod[46]/array[14])*(syncod[46]/array[14])
                    VALAA[1] = (syncod[47]/array[14])*(syncod[47]/array[14])
                    VALAA[2] = (syncod[48]/array[14])*(syncod[48]/array[14])
                    VALAA[3] = (syncod[49]/array[14])*(syncod[49]/array[14])
                    enc2[14] = sum(VALAA)
                    enc3[14] = (array[14] * enc2[14]) - 1 / array[14] - 1
                    enc4[14] = 1 / enc3[14]

            if asdf in ALA:
                    ALAAA[0]= (syncod[50]/array[15])*(syncod[50]/array[15])
                    ALAAA[1] = (syncod[51]/array[15])*(syncod[51]/array[15])
                    ALAAA[2] = (syncod[52]/array[15])*(syncod[52]/array[15])
                    ALAAA[3] = (syncod[53]/array[15])*(syncod[53]/array[15])
                    enc2[15] = sum(ALAAA)
                    enc3[15] = (array[15] * enc2[15]) - 1 / array[15] - 1
                    enc4[15] = 1 / enc3[15]
            elif asdf in ASP:
                    ASPAA[0]= (syncod[54]/array[16])*(syncod[54]/array[16])
                    ASPAA[1] = (syncod[55]/array[16])*(syncod[55]/array[16])
                    enc2[16] = sum(ASPAA)
                    enc3[16] = (array[16] * enc2[16]) - 1 / array[16] - 1
                    enc4[16] = 1 / enc3[16]
            elif asdf in GLU:
                    GLUAA[0]= (syncod[56]/array[17])*(syncod[56]/array[17])
                    GLUAA[1] = (syncod[57]/array[17])*(syncod[57]/array[17])
                    enc2[17] = sum(GLUAA)
                    enc3[17] = (array[17] * enc2[17]) - 1 / array[17] - 1
                    enc4[17] = 1 / enc3[17]
            if asdf in GLY:
                    GLYAA[0]= (syncod[58]/array[18])*(syncod[58]/array[18])
                    GLYAA[1] = (syncod[59]/array[18])*(syncod[59]/array[18])
                    GLYAA[2] = (syncod[60]/array[18])*(syncod[60]/array[18])
                    GLYAA[3] = (syncod[61]/array[18])*(syncod[61]/array[18])
                    enc2[18] = sum(GLYAA)
                    enc3[18] = (array[18] * enc2[18]) - 1 / array[18] - 1
                    enc4[18] = 1 / enc3[18]
            if asdf in TRP:
                    TRPAA[0]= (syncod[62]/array[19])*(syncod[62]/array[19])
                    enc2[19] = sum(TRPAA)
                    enc3[19] = (array[19] * enc2[19]) - 1 / array[19] - 1
                    enc4[19] = 1 / enc3[19]

            if asdf in MET:
                    METAA[0]= (syncod[63]/array[20])*(syncod[63]/array[20])
                    enc2[20] = sum(METAA)
                    enc3[20] = (array[20] * enc2[20]) - 1 / array[20] - 1
                    enc4[20] = 1 / enc3[20]


    print('ghkk', syncod, 'lkj', enc2, enc3, enc4)

    SF6 = (enc4[0]+enc4[2]+enc4[9])/3
    SF2 = (enc4[1] + enc4[3] + enc4[5] + enc4[7] + enc4[8] + enc4[12] + enc4[13] + enc4[16] + enc4[17])/9
    SF3 = (enc4[10])/2
    SF4 = (enc4[6] + enc4[11] + enc4[14] + enc4[15] + enc4[18])/5
    SF = 2 + 1/SF2 + 1/SF3 + 1/SF4 + 1/SF6

    print('codons',codons)
    print(array)
    print(sum(array))
    print(syncod)
    print(sum(syncod))
    print('NEC is', SF2, SF3, SF4, SF6, SF)

    #print(array)
https://academic.oup.com/mbe/article/30/1/191/1019148
https://github.com/rhondene/Codon-Usage-in-Python/blob/master/CodonCount/__main__.py
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5581930/
https://biologydirect.biomedcentral.com/articles/10.1186/1745-6150-3-38#rightslink
https://www.genetics.org/content/genetics/172/2/1301.full.pdf
https://sci-hub.se/https://pubmed.ncbi.nlm.nih.gov/22915832/
https://sci-hub.se/https://www.sciencedirect.com/science/article/abs/pii/S0006291X04006461
https://sci-hub.se/https://pubmed.ncbi.nlm.nih.gov/2110097/
https://pubmed.ncbi.nlm.nih.gov/9385367/
http://www.veterinaryworld.org/Vol.14/June-2021/7.pdf
file:///C:/Users/Memoona/Downloads/genes-12-01169.pdf
http://www.ijbiotech.com/article_7934_2268840fb3001202e6af4b0b6b680abc.pdf
http://www.ijbiotech.com/article_7934_2268840fb3001202e6af4b0b6b680abc.pdf
https://www.tandfonline.com/doi/full/10.1080/13102818.2021.1911684
https://pubmed.ncbi.nlm.nih.gov/2110097/
https://pubmed.ncbi.nlm.nih.gov/2110097/
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528880/#B24
https://en.wikipedia.org/wiki/GC-content
https://academic.oup.com/dnaresearch/article/24/3/303/2972686#88473324
https://ss-usa.s3.amazonaws.com/c/308466541/media/17486050f6d3f192a04658415748148/cDNA%20Genetic-Code-Amino-Acid-Codon-Chart-Genomenon.pdf
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3492488/
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7086886/
covid muatates once a week https://www.bath.ac.uk/announcements/mutation-rate-of-covid19-virus-is-at-least-50-per-cent-higher-than-previously-thought/














