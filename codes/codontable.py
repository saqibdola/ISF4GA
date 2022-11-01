
i=0
with open('codontable.txt') as f1:
    for line in f1:
        i+=1
        #print(line, i)

LEU = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
PHE = ['TTT', 'TTC']
SER = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
TYR = ['TAT', 'TAC']
STOP = ['TAA', 'TAG', 'TGA']
CYS = ['TGT', 'TGC']
PRO = ['CCT', 'CCC', 'CCA', 'CCG']
HIS = ['CAT', 'CAC']
GLN = ['CAA', 'CAG']
ARG = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
LLE = ['ATT', 'ATC', 'ATA']
THR = ['ACT', 'ACC', 'ACA', 'ACG']
ASN = ['AAT', 'AAC']
LYS = ['AAA', 'AAG']
VAL = ['GTT', 'GTC', 'GTA', 'GTG']
ALA = ['GCT', 'GCC', 'GCA', 'GCG']
ASP = ['GAT', 'GAC']
GLU = ['GAA' 'GAG']
GLY = ['GGT', 'GGC', 'GGA', 'GGG']
TRP = ['TGG']
MET = ['ATG']


def checking(asdf, asdfg):

        if asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        elif asdf in line and asdfg in line:
            print('PNC')
        else:
            print('Protien is changed')
            if asdf in LEU and asdfg in PHE:
                print('LEU is changes to PHE')
            elif asdf in LEU and asdfg in SER:
                print('LEU is changes to SER')
            elif asdf in LEU and asdfg in TYR:
                print('LEU is changes to TYR')
            elif asdf in LEU and asdfg in STOP:
                print('LEU is changes to STOP')
            elif asdf in LEU and asdfg in CYS:
                print('LEU is changes to CYS')
            elif asdf in LEU and asdfg in PRO:
                print('LEU is changes to PRO')
            elif asdf in LEU and asdfg in HIS:
                print('LEU is changes to HIS')
            elif asdf in LEU and asdfg in GLN:
                print('LEU is changes to GLN')
            elif asdf in LEU and asdfg in ARG:
                print('LEU is changes to ARG')
            elif asdf in LEU and asdfg in LLE:
                print('LEU is changes to LLE')
            elif asdf in LEU and asdfg in THR:
                print('LEU is changes to THR')
            elif asdf in LEU and asdfg in ASN:
                print('LEU is changes to ASN')
            elif asdf in LEU and asdfg in LYS:
                print('LEU is changes to LYS')
            elif asdf in LEU and asdfg in VAL:
                print('LEU is changes to VAL')
            elif asdf in LEU and asdfg in ALA:
                print('LEU is changes to ALA')
            elif asdf in LEU and asdfg in ASP:
                print('LEU is changes to ASP')
            elif asdf in LEU and asdfg in GLU:
                print('LEU is changes to GLU')
            elif asdf in LEU and asdfg in GLY:
                print('LEU is changes to GLY')
            elif asdf in LEU and asdfg in TRP:
                print('LEU is changes to TRP')
            elif asdf in LEU and asdfg in MET:
                print('LEU is changes to MET')


            elif asdf in PHE and asdfg in LEU:
                print('PHE is changes to LEU')
            elif asdf in PHE and asdfg in SER:
                print('PHE is changes to SER')
            elif asdf in PHE and asdfg in TYR:
                print('PHE is changes to TYR')
            elif asdf in PHE and asdfg in STOP:
                print('PHE is changes to STOP')
            elif asdf in PHE and asdfg in CYS:
                print('PHE is changes to CYS')
            elif asdf in PHE and asdfg in PRO:
                print('PHE is changes to PRO')
            elif asdf in PHE and asdfg in HIS:
                print('PHE is changes to HIS')
            elif asdf in PHE and asdfg in GLN:
                print('PHE is changes to GLN')
            elif asdf in PHE and asdfg in ARG:
                print('PHE is changes to ARG')
            elif asdf in PHE and asdfg in LLE:
                print('PHE is changes to LLE')
            elif asdf in PHE and asdfg in THR:
                print('PHE is changes to THR')
            elif asdf in PHE and asdfg in ASN:
                print('PHE is changes to ASN')
            elif asdf in PHE and asdfg in LYS:
                print('PHE is changes to LYS')
            elif asdf in PHE and asdfg in VAL:
                print('PHE is changes to VAL')
            elif asdf in PHE and asdfg in ALA:
                print('PHE is changes to ALA')
            elif asdf in PHE and asdfg in ASP:
                print('PHE is changes to ASP')
            elif asdf in PHE and asdfg in GLU:
                print('PHE is changes to GLU')
            elif asdf in PHE and asdfg in GLY:
                print('PHE is changes to GLY')
            elif asdf in PHE and asdfg in TRP:
                print('PHE is changes to TRP')
            elif asdf in PHE and asdfg in MET:
                print('PHE is changes to MET')


            elif asdf in SER and asdfg in LEU:
                print('SER is changes to LEU')
            elif asdf in SER and asdfg in PHE:
                print('SER is changes to PHE')
            elif asdf in SER and asdfg in TYR:
                print('SER is changes to TYR')
            elif asdf in SER and asdfg in STOP:
                print('SER is changes to STOP')
            elif asdf in SER and asdfg in CYS:
                print('SER is changes to CYS')
            elif asdf in SER and asdfg in PRO:
                print('SER is changes to PRO')
            elif asdf in SER and asdfg in HIS:
                print('SER is changes to HIS')
            elif asdf in SER and asdfg in GLN:
                print('SER is changes to GLN')
            elif asdf in SER and asdfg in ARG:
                print('SER is changes to ARG')
            elif asdf in SER and asdfg in LLE:
                print('SER is changes to LLE')
            elif asdf in SER and asdfg in THR:
                print('SER is changes to THR')
            elif asdf in SER and asdfg in ASN:
                print('SER is changes to ASN')
            elif asdf in SER and asdfg in LYS:
                print('SER is changes to LYS')
            elif asdf in SER and asdfg in VAL:
                print('SER is changes to VAL')
            elif asdf in SER and asdfg in ALA:
                print('SER is changes to ALA')
            elif asdf in SER and asdfg in ASP:
                print('SER is changes to ASP')
            elif asdf in SER and asdfg in GLU:
                print('SER is changes to GLU')
            elif asdf in SER and asdfg in GLY:
                print('SER is changes to GLY')
            elif asdf in SER and asdfg in TRP:
                print('SER is changes to TRP')
            elif asdf in SER and asdfg in MET:
                print('SER is changes to MET')


            elif asdf in TYR and asdfg in LEU:
                print('TYR is changes to LEU')
            elif asdf in TYR and asdfg in PHE:
                print('TYR is changes to PHE')
            elif asdf in TYR and asdfg in SER:
                print('TYR is changes to SER')
            elif asdf in TYR and asdfg in STOP:
                print('TYR is changes to STOP')
            elif asdf in TYR and asdfg in CYS:
                print('TYR is changes to CYS')
            elif asdf in TYR and asdfg in PRO:
                print('TYR is changes to PRO')
            elif asdf in TYR and asdfg in HIS:
                print('TYR is changes to HIS')
            elif asdf in TYR and asdfg in GLN:
                print('TYR is changes to GLN')
            elif asdf in TYR and asdfg in ARG:
                print('TYR is changes to ARG')
            elif asdf in TYR and asdfg in LLE:
                print('TYR is changes to LLE')
            elif asdf in TYR and asdfg in THR:
                print('TYR is changes to THR')
            elif asdf in TYR and asdfg in ASN:
                print('TYR is changes to ASN')
            elif asdf in TYR and asdfg in LYS:
                print('TYR is changes to LYS')
            elif asdf in TYR and asdfg in VAL:
                print('TYR is changes to VAL')
            elif asdf in TYR and asdfg in ALA:
                print('TYR is changes to ALA')
            elif asdf in TYR and asdfg in ASP:
                print('TYR is changes to ASP')
            elif asdf in TYR and asdfg in GLU:
                print('TYR is changes to GLU')
            elif asdf in TYR and asdfg in GLY:
                print('TYR is changes to GLY')
            elif asdf in TYR and asdfg in TRP:
                print('TYR is changes to TRP')
            elif asdf in TYR and asdfg in MET:
                print('TYR is changes to MET')


            elif asdf in STOP and asdfg in LEU:
                print('STOP is changes to LEU')
            elif asdf in STOP and asdfg in PHE:
                print('STOP is changes to PHE')
            elif asdf in STOP and asdfg in SER:
                print('STOP is changes to SER')
            elif asdf in STOP and asdfg in TYR:
                print('STOP is changes to TYR')
            elif asdf in STOP and asdfg in CYS:
                print('STOP is changes to CYS')
            elif asdf in STOP and asdfg in PRO:
                print('STOP is changes to PRO')
            elif asdf in STOP and asdfg in HIS:
                print('STOP is changes to HIS')
            elif asdf in STOP and asdfg in GLN:
                print('STOP is changes to GLN')
            elif asdf in STOP and asdfg in ARG:
                print('STOP is changes to ARG')
            elif asdf in STOP and asdfg in LLE:
                print('STOP is changes to LLE')
            elif asdf in STOP and asdfg in THR:
                print('STOP is changes to THR')
            elif asdf in STOP and asdfg in ASN:
                print('STOP is changes to ASN')
            elif asdf in STOP and asdfg in LYS:
                print('STOP is changes to LYS')
            elif asdf in STOP and asdfg in VAL:
                print('STOP is changes to VAL')
            elif asdf in STOP and asdfg in ALA:
                print('STOP is changes to ALA')
            elif asdf in STOP and asdfg in ASP:
                print('STOP is changes to ASP')
            elif asdf in STOP and asdfg in GLU:
                print('STOP is changes to GLU')
            elif asdf in STOP and asdfg in GLY:
                print('STOP is changes to GLY')
            elif asdf in STOP and asdfg in TRP:
                print('STOP is changes to TRP')
            elif asdf in STOP and asdfg in MET:
                print('STOP is changes to MET')


            elif asdf in CYS and asdfg in LEU:
                print('CYS is changes to LEU')
            elif asdf in CYS and asdfg in PHE:
                print('CYS is changes to PHE1')
            elif asdf in CYS and asdfg in SER:
                print('CYS is changes to SER')
            elif asdf in CYS and asdfg in TYR:
                print('CYS is changes to TYR')
            elif asdf in CYS and asdfg in STOP:
                print('CYS is changes to STOP')
            elif asdf in CYS and asdfg in PRO:
                print('CYS is changes to PRO')
            elif asdf in CYS and asdfg in HIS:
                print('CYS is changes to HIS')
            elif asdf in CYS and asdfg in GLN:
                print('CYS is changes to GLN')
            elif asdf in CYS and asdfg in ARG:
                print('CYS is changes to ARG')
            elif asdf in CYS and asdfg in LLE:
                print('CYS is changes to LLE')
            elif asdf in CYS and asdfg in THR:
                print('CYS is changes to THR')
            elif asdf in CYS and asdfg in ASN:
                print('CYS is changes to ASN')
            elif asdf in CYS and asdfg in LYS:
                print('CYS is changes to LYS')
            elif asdf in CYS and asdfg in VAL:
                print('CYS is changes to VAL')
            elif asdf in CYS and asdfg in ALA:
                print('CYS is changes to ALA')
            elif asdf in CYS and asdfg in ASP:
                print('CYS is changes to ASP')
            elif asdf in CYS and asdfg in GLU:
                print('CYS is changes to GLU')
            elif asdf in CYS and asdfg in GLY:
                print('CYS is changes to GLY')
            elif asdf in CYS and asdfg in TRP:
                print('CYS is changes to TRP')
            elif asdf in CYS and asdfg in MET:
                print('CYS is changes to MET')


            elif asdf in PRO and asdfg in LEU:
                print('PRO is changes to LEU')
            elif asdf in PRO and asdfg in PHE:
                print('PRO is changes to PHE')
            elif asdf in PRO and asdfg in SER:
                print('PRO is changes to SER')
            elif asdf in PRO and asdfg in TYR:
                print('PRO is changes to TYR')
            elif asdf in PRO and asdfg in STOP:
                print('PRO is changes to STOP')
            elif asdf in PRO and asdfg in CYS:
                print('PRO is changes to CYS')
            elif asdf in PRO and asdfg in HIS:
                print('PRO is changes to HIS')
            elif asdf in PRO and asdfg in GLN:
                print('PRO is changes to GLN')
            elif asdf in PRO and asdfg in ARG:
                print('PRO is changes to ARG')
            elif asdf in PRO and asdfg in LLE:
                print('PRO is changes to LLE')
            elif asdf in PRO and asdfg in THR:
                print('PRO is changes to THR')
            elif asdf in PRO and asdfg in ASN:
                print('PRO is changes to ASN')
            elif asdf in PRO and asdfg in LYS:
                print('PRO is changes to LYS')
            elif asdf in PRO and asdfg in VAL:
                print('PRO is changes to VAL')
            elif asdf in PRO and asdfg in ALA:
                print('PRO is changes to ALA')
            elif asdf in PRO and asdfg in ASP:
                print('PRO is changes to ASP')
            elif asdf in PRO and asdfg in GLU:
                print('PRO is changes to GLU')
            elif asdf in PRO and asdfg in GLY:
                print('PRO is changes to GLY')
            elif asdf in PRO and asdfg in TRP:
                print('PRO is changes to TRP')
            elif asdf in PRO and asdfg in MET:
                print('PRO is changes to MET')


            elif asdf in HIS and asdfg in LEU:
                print('HIS is changes to LEU')
            elif asdf in HIS and asdfg in PHE:
                print('HIS is changes to PHE')
            elif asdf in HIS and asdfg in SER:
                print('HIS is changes to SER')
            elif asdf in HIS and asdfg in TYR:
                print('HIS is changes to TYR')
            elif asdf in HIS and asdfg in STOP:
                print('HIS is changes to STOP')
            elif asdf in HIS and asdfg in CYS:
                print('HIS is changes to CYS')
            elif asdf in HIS and asdfg in PRO:
                print('HIS is changes to PRO')
            elif asdf in HIS and asdfg in GLN:
                print('HIS is changes to GLN')
            elif asdf in HIS and asdfg in ARG:
                print('HIS is changes to ARG')
            elif asdf in HIS and asdfg in LLE:
                print('HIS is changes to LLE')
            elif asdf in HIS and asdfg in THR:
                print('HIS is changes to THR')
            elif asdf in HIS and asdfg in ASN:
                print('HIS is changes to ASN')
            elif asdf in HIS and asdfg in LYS:
                print('HIS is changes to LYS')
            elif asdf in HIS and asdfg in VAL:
                print('HIS is changes to VAL')
            elif asdf in HIS and asdfg in ALA:
                print('HIS is changes to ALA')
            elif asdf in HIS and asdfg in ASP:
                print('HIS is changes to ASP')
            elif asdf in HIS and asdfg in GLU:
                print('HIS is changes to GLU')
            elif asdf in HIS and asdfg in GLY:
                print('HIS is changes to GLY')
            elif asdf in HIS and asdfg in TRP:
                print('HIS is changes to TRP')
            elif asdf in HIS and asdfg in MET:
                print('HIS is changes to MET')


            elif asdf in GLN and asdfg in LEU:
                print('GLN is changes to LEU')
            elif asdf in GLN and asdfg in PHE:
                print('GLN is changes to PHE')
            elif asdf in GLN and asdfg in SER:
                print('GLN is changes to SER')
            elif asdf in GLN and asdfg in TYR:
                print('GLN is changes to TYR')
            elif asdf in GLN and asdfg in STOP:
                print('GLN is changes to STOP')
            elif asdf in GLN and asdfg in PRO:
                print('GLN is changes to PRO')
            elif asdf in GLN and asdfg in HIS:
                print('GLN is changes to HIS')
            elif asdf in GLN and asdfg in ASP:
                print('GLN is changes to ASP')
            elif asdf in GLN and asdfg in ARG:
                print('GLN is changes to ARG')
            elif asdf in GLN and asdfg in LLE:
                print('GLN is changes to LLE')
            elif asdf in GLN and asdfg in THR:
                print('GLN is changes to THR')
            elif asdf in GLN and asdfg in ASN:
                print('GLN is changes to ASN')
            elif asdf in GLN and asdfg in LYS:
                print('GLN is changes to LYS')
            elif asdf in GLN and asdfg in VAL:
                print('GLN is changes to VAL')
            elif asdf in GLN and asdfg in ALA:
                print('GLN is changes to ALA')
            elif asdf in GLN and asdfg in ASP:
                print('GLN is changes to ASP')
            elif asdf in GLN and asdfg in GLU:
                print('GLN is changes to GLU')
            elif asdf in GLN and asdfg in GLY:
                print('GLN is changes to GLY')
            elif asdf in GLN and asdfg in TRP:
                print('GLN is changes to TRP')
            elif asdf in GLN and asdfg in MET:
                print('GLN is changes to MET')


            elif asdf in ARG and asdfg in LEU:
                print('ARG is changes to LEU')
            elif asdf in ARG and asdfg in PHE:
                print('ARG is changes to PHE')
            elif asdf in ARG and asdfg in SER:
                print('ARG is changes to SER')
            elif asdf in ARG and asdfg in TYR:
                print('ARG is changes to TYR')
            elif asdf in ARG and asdfg in STOP:
                print('ARG is changes to STOP')
            elif asdf in ARG and asdfg in CYS:
                print('ARG is changes to CYS')
            elif asdf in ARG and asdfg in PRO:
                print('ARG is changes to PRO')
            elif asdf in ARG and asdfg in HIS:
                print('ARG is changes to HIS')
            elif asdf in ARG and asdfg in GLN:
                print('ARG is changes to GLN')
            elif asdf in ARG and asdfg in LLE:
                print('ARG is changes to LLE')
            elif asdf in ARG and asdfg in THR:
                print('ARG is changes to THR')
            elif asdf in ARG and asdfg in ASN:
                print('ARG is changes to ASN')
            elif asdf in ARG and asdfg in LYS:
                print('ARG is changes to LYS')
            elif asdf in ARG and asdfg in VAL:
                print('ARG is changes to VAL')
            elif asdf in ARG and asdfg in ALA:
                print('ARG is changes to ALA')
            elif asdf in ARG and asdfg in ASP:
                print('ARG is changes to ASP')
            elif asdf in ARG and asdfg in GLU:
                print('ARG is changes to GLU')
            elif asdf in ARG and asdfg in GLY:
                print('ARG is changes to GLY')
            elif asdf in ARG and asdfg in TRP:
                print('ARG is changes to TRP')
            elif asdf in ARG and asdfg in MET:
                print('ARG is changes to MET')


            elif asdf in LLE and asdfg in LEU:
                print('LLE is changes to LEU')
            elif asdf in LLE and asdfg in PHE:
                print('LLE is changes to PHE')
            elif asdf in LLE and asdfg in SER:
                print('LLE is changes to SER')
            elif asdf in LLE and asdfg in TYR:
                print('LLE is changes to TYR')
            elif asdf in LLE and asdfg in STOP:
                print('LLE is changes to STOP')
            elif asdf in LLE and asdfg in CYS:
                print('LLE is changes to CYS')
            elif asdf in LLE and asdfg in PRO:
                print('LLE is changes to PRO')
            elif asdf in LLE and asdfg in HIS:
                print('LLE is changes to HIS')
            elif asdf in LLE and asdfg in GLN:
                print('LLE is changes to GLN')
            elif asdf in LLE and asdfg in ARG:
                print('LLE is changes to ARG')
            elif asdf in LLE and asdfg in THR:
                print('LLE is changes to THR')
            elif asdf in LLE and asdfg in ASN:
                print('LLE is changes to ASN')
            elif asdf in LLE and asdfg in LYS:
                print('LLE is changes to LYS')
            elif asdf in LLE and asdfg in VAL:
                print('LLE is changes to VAL')
            elif asdf in LLE and asdfg in ALA:
                print('LLE is changes to ALA')
            elif asdf in LLE and asdfg in ASP:
                print('LLE is changes to ASP')
            elif asdf in LLE and asdfg in GLU:
                print('LLE is changes to GLU')
            elif asdf in LLE and asdfg in GLY:
                print('LLE is changes to GLY')
            elif asdf in LLE and asdfg in TRP:
                print('LLE is changes to TRP')
            elif asdf in LLE and asdfg in MET:
                print('LLE is changes to MET')


            elif asdf in THR and asdfg in LEU:
                print('THR is changes to LEU')
            elif asdf in THR and asdfg in PHE:
                print('THR is changes to PHE')
            elif asdf in THR and asdfg in SER:
                print('THR is changes to SER')
            elif asdf in THR and asdfg in TYR:
                print('THR is changes to TYR')
            elif asdf in THR and asdfg in STOP:
                print('THR is changes to STOP')
            elif asdf in THR and asdfg in CYS:
                print('THR is changes to CYS')
            elif asdf in THR and asdfg in PRO:
                print('THR is changes to PRO')
            elif asdf in THR and asdfg in HIS:
                print('THR is changes to HIS')
            elif asdf in THR and asdfg in GLN:
                print('THR is changes to GLN')
            elif asdf in THR and asdfg in ARG:
                print('THR is changes to ARG')
            elif asdf in THR and asdfg in LLE:
                print('THR is changes to LLE')
            elif asdf in THR and asdfg in ASN:
                print('THR is changes to ASN')
            elif asdf in THR and asdfg in LYS:
                print('THR is changes to LYS')
            elif asdf in THR and asdfg in VAL:
                print('THR is changes to VAL')
            elif asdf in THR and asdfg in ALA:
                print('THR is changes to ALA')
            elif asdf in THR and asdfg in ASP:
                print('THR is changes to ASP')
            elif asdf in THR and asdfg in GLU:
                print('THR is changes to GLU')
            elif asdf in THR and asdfg in GLY:
                print('THR is changes to GLY')
            elif asdf in THR and asdfg in TRP:
                print('THR is changes to TRP')
            elif asdf in THR and asdfg in MET:
                print('THR is changes to MET')


            elif asdf in ASN and asdfg in LEU:
                print('ASN is changes to LEU')
            elif asdf in ASN and asdfg in PHE:
                print('ASN is changes to PHE')
            elif asdf in ASN and asdfg in SER:
                print('ASN is changes to SER')
            elif asdf in ASN and asdfg in TYR:
                print('ASN is changes to TYR')
            elif asdf in ASN and asdfg in STOP:
                print('ASN is changes to STOP')
            elif asdf in ASN and asdfg in CYS:
                print('ASN is changes to CYS')
            elif asdf in ASN and asdfg in PRO:
                print('ASN is changes to PRO')
            elif asdf in ASN and asdfg in HIS:
                print('ASN is changes to HIS')
            elif asdf in ASN and asdfg in GLN:
                print('ASN is changes to GLN')
            elif asdf in ASN and asdfg in ARG:
                print('ASN is changes to ARG')
            elif asdf in ASN and asdfg in LLE:
                print('ASN is changes to LLE')
            elif asdf in ASN and asdfg in THR:
                print('ASN is changes to THR')
            elif asdf in ASN and asdfg in LYS:
                print('ASN is changes to LYS')
            elif asdf in ASN and asdfg in VAL:
                print('ASN is changes to VAL')
            elif asdf in ASN and asdfg in ALA:
                print('ASN is changes to ALA')
            elif asdf in ASN and asdfg in ASP:
                print('ASN is changes to ASP')
            elif asdf in ASN and asdfg in GLU:
                print('ASN is changes to GLU')
            elif asdf in ASN and asdfg in GLY:
                print('ASN is changes to GLY')
            elif asdf in ASN and asdfg in TRP:
                print('ASN is changes to TRP')
            elif asdf in ASN and asdfg in MET:
                print('ASN is changes to MET')

            if asdf in LYS and asdfg in PHE:
                print('LYS is changes to PHE')
            elif asdf in LYS and asdfg in SER:
                print('LYS is changes to SER')
            elif asdf in LYS and asdfg in TYR:
                print('LYS is changes to TYR')
            elif asdf in LYS and asdfg in STOP:
                print('LYS is changes to STOP')
            elif asdf in LYS and asdfg in CYS:
                print('LYS is changes to CYS')
            elif asdf in LYS and asdfg in PRO:
                print('LYS is changes to PRO')
            elif asdf in LYS and asdfg in HIS:
                print('LYS is changes to HIS')
            elif asdf in LYS and asdfg in GLN:
                print('LYS is changes to GLN')
            elif asdf in LYS and asdfg in ARG:
                print('LYS is changes to ARG')
            elif asdf in LYS and asdfg in LLE:
                print('LYS is changes to LLE')
            elif asdf in LYS and asdfg in THR:
                print('LYS is changes to THR')
            elif asdf in LYS and asdfg in ASN:
                print('LYS is changes to ASN')
            elif asdf in LYS and asdfg in LEU:
                print('LYS is changes to LEU')
            elif asdf in LYS and asdfg in VAL:
                print('LYS is changes to VAL')
            elif asdf in LYS and asdfg in ALA:
                print('LYS is changes to ALA')
            elif asdf in LYS and asdfg in ASP:
                print('LYS is changes to ASP')
            elif asdf in LYS and asdfg in GLU:
                print('LYS is changes to GLU')
            elif asdf in LYS and asdfg in GLY:
                print('LYS is changes to GLY')
            elif asdf in LYS and asdfg in TRP:
                print('LYS is changes to TRP')
            elif asdf in LYS and asdfg in MET:
                print('LYS is changes to MET')

            if asdf in VAL and asdfg in PHE:
                print('VAL is changes to PHE')
            elif asdf in VAL and asdfg in SER:
                print('VAL is changes to SER')
            elif asdf in VAL and asdfg in TYR:
                print('VAL is changes to TYR')
            elif asdf in VAL and asdfg in STOP:
                print('VAL is changes to STOP')
            elif asdf in VAL and asdfg in CYS:
                print('VAL is changes to CYS')
            elif asdf in VAL and asdfg in PRO:
                print('VAL is changes to PRO')
            elif asdf in VAL and asdfg in HIS:
                print('VAL is changes to HIS')
            elif asdf in VAL and asdfg in GLN:
                print('VAL is changes to GLN')
            elif asdf in VAL and asdfg in ARG:
                print('VAL is changes to ARG')
            elif asdf in VAL and asdfg in LLE:
                print('VAL is changes to LLE')
            elif asdf in VAL and asdfg in THR:
                print('VAL is changes to THR')
            elif asdf in VAL and asdfg in ASN:
                print('VAL is changes to ASN')
            elif asdf in VAL and asdfg in LEU:
                print('VAL is changes to LEU')
            elif asdf in VAL and asdfg in LYS:
                print('VAL is changes to LYS')
            elif asdf in VAL and asdfg in ALA:
                print('VAL is changes to ALA')
            elif asdf in VAL and asdfg in ASP:
                print('VAL is changes to ASP')
            elif asdf in VAL and asdfg in GLU:
                print('VAL is changes to GLU')
            elif asdf in VAL and asdfg in GLY:
                print('VAL is changes to GLY')
            elif asdf in VAL and asdfg in TRP:
                print('VAL is changes to TRP')
            elif asdf in VAL and asdfg in MET:
                print('VAL is changes to MET')

            if asdf in ALA and asdfg in PHE:
                print('ALA is changes to PHE')
            elif asdf in ALA and asdfg in SER:
                print('ALA is changes to SER')
            elif asdf in ALA and asdfg in TYR:
                print('ALA is changes to TYR')
            elif asdf in ALA and asdfg in STOP:
                print('ALA is changes to STOP')
            elif asdf in ALA and asdfg in CYS:
                print('ALA is changes to CYS')
            elif asdf in ALA and asdfg in PRO:
                print('ALA is changes to PRO')
            elif asdf in ALA and asdfg in HIS:
                print('ALA is changes to HIS')
            elif asdf in ALA and asdfg in GLN:
                print('ALA is changes to GLN')
            elif asdf in ALA and asdfg in ARG:
                print('ALA is changes to ARG')
            elif asdf in ALA and asdfg in LLE:
                print('ALA is changes to LLE')
            elif asdf in ALA and asdfg in THR:
                print('ALA is changes to THR')
            elif asdf in ALA and asdfg in ASN:
                print('ALA is changes to ASN')
            elif asdf in ALA and asdfg in LEU:
                print('ALA is changes to LEU')
            elif asdf in ALA and asdfg in LYS:
                print('ALA is changes to LYS')
            elif asdf in ALA and asdfg in VAL:
                print('ALA is changes to VAL')
            elif asdf in ALA and asdfg in ASP:
                print('ALA is changes to ASP')
            elif asdf in ALA and asdfg in GLU:
                print('ALA is changes to GLU')
            elif asdf in ALA and asdfg in GLY:
                print('ALA is changes to GLY')
            elif asdf in ALA and asdfg in TRP:
                print('ALA is changes to TRP')
            elif asdf in ALA and asdfg in MET:
                print('ALA is changes to MET')

            if asdf in ASP and asdfg in PHE:
                print('ASP is changes to PHE')
            elif asdf in ASP and asdfg in SER:
                print('ASP is changes to SER')
            elif asdf in ASP and asdfg in TYR:
                print('ASP is changes to TYR')
            elif asdf in ASP and asdfg in STOP:
                print('ASP is changes to STOP')
            elif asdf in ASP and asdfg in CYS:
                print('ASP is changes to CYS')
            elif asdf in ASP and asdfg in PRO:
                print('ASP is changes to PRO')
            elif asdf in ASP and asdfg in HIS:
                print('ASP is changes to HIS')
            elif asdf in ASP and asdfg in GLN:
                print('ASP is changes to GLN')
            elif asdf in ASP and asdfg in ARG:
                print('ASP is changes to ARG')
            elif asdf in ASP and asdfg in LLE:
                print('ASP is changes to LLE')
            elif asdf in ASP and asdfg in THR:
                print('ASP is changes to THR')
            elif asdf in ASP and asdfg in ASN:
                print('ASP is changes to ASN')
            elif asdf in ASP and asdfg in LEU:
                print('ASP is changes to LEU')
            elif asdf in ASP and asdfg in LYS:
                print('ASP is changes to LYS')
            elif asdf in ASP and asdfg in VAL:
                print('ASP is changes to VAL')
            elif asdf in ASP and asdfg in ALA:
                print('ASP is changes to ALA')
            elif asdf in ASP and asdfg in GLU:
                print('ASP is changes to GLU')
            elif asdf in ASP and asdfg in GLY:
                print('ASP is changes to GLY')
            elif asdf in ASP and asdfg in TRP:
                print('ASP is changes to TRP')
            elif asdf in ASP and asdfg in MET:
                print('ASP is changes to MET')

            if asdf in GLU and asdfg in PHE:
                print('GLU is changes to PHE')
            elif asdf in GLU and asdfg in SER:
                print('GLU is changes to SER')
            elif asdf in GLU and asdfg in TYR:
                print('GLU is changes to TYR')
            elif asdf in GLU and asdfg in STOP:
                print('GLU is changes to STOP')
            elif asdf in GLU and asdfg in CYS:
                print('GLU is changes to CYS')
            elif asdf in GLU and asdfg in PRO:
                print('GLU is changes to PRO')
            elif asdf in GLU and asdfg in HIS:
                print('GLU is changes to HIS')
            elif asdf in GLU and asdfg in GLN:
                print('GLU is changes to GLN')
            elif asdf in GLU and asdfg in ARG:
                print('GLU is changes to ARG')
            elif asdf in GLU and asdfg in LLE:
                print('GLU is changes to LLE')
            elif asdf in GLU and asdfg in THR:
                print('GLU is changes to THR')
            elif asdf in GLU and asdfg in ASN:
                print('GLU is changes to ASN')
            elif asdf in GLU and asdfg in LEU:
                print('GLU is changes to LEU')
            elif asdf in GLU and asdfg in LYS:
                print('GLU is changes to LYS')
            elif asdf in GLU and asdfg in VAL:
                print('GLU is changes to VAL')
            elif asdf in GLU and asdfg in ALA:
                print('GLU is changes to ALA')
            elif asdf in GLU and asdfg in ASP:
                print('GLU is changes to ASP')
            elif asdf in GLU and asdfg in GLY:
                print('GLU is changes to GLY')
            elif asdf in GLU and asdfg in TRP:
                print('GLU is changes to TRP')
            elif asdf in GLU and asdfg in MET:
                print('GLU is changes to MET')

            if asdf in GLY and asdfg in PHE:
                print('GLY is changes to PHE')
            elif asdf in GLY and asdfg in SER:
                print('GLY is changes to SER')
            elif asdf in GLY and asdfg in TYR:
                print('GLY is changes to TYR')
            elif asdf in GLY and asdfg in STOP:
                print('GLY is changes to STOP')
            elif asdf in GLY and asdfg in CYS:
                print('GLY is changes to CYS')
            elif asdf in GLY and asdfg in PRO:
                print('GLY is changes to PRO')
            elif asdf in GLY and asdfg in HIS:
                print('GLY is changes to HIS')
            elif asdf in GLY and asdfg in GLN:
                print('GLY is changes to GLN')
            elif asdf in GLY and asdfg in ARG:
                print('GLY is changes to ARG')
            elif asdf in GLY and asdfg in LLE:
                print('GLY is changes to LLE')
            elif asdf in GLY and asdfg in THR:
                print('GLY is changes to THR')
            elif asdf in GLY and asdfg in ASN:
                print('GLY is changes to ASN')
            elif asdf in GLY and asdfg in LEU:
                print('GLY is changes to LEU')
            elif asdf in GLY and asdfg in LYS:
                print('GLY is changes to LYS')
            elif asdf in GLY and asdfg in VAL:
                print('GLY is changes to VAL')
            elif asdf in GLY and asdfg in ALA:
                print('GLY is changes to ALA')
            elif asdf in GLY and asdfg in ASP:
                print('GLY is changes to ASP')
            elif asdf in GLY and asdfg in GLU:
                print('GLY is changes to GLU')
            elif asdf in GLY and asdfg in TRP:
                print('GLY is changes to TRP')
            elif asdf in GLY and asdfg in MET:
                print('GLY is changes to MET')

        if asdf in TRP and asdfg in PHE:
            print('TRP is changes to PHE')
        elif asdf in TRP and asdfg in SER:
            print('TRP is changes to SER')
        elif asdf in TRP and asdfg in TYR:
            print('TRP is changes to TYR')
        elif asdf in TRP and asdfg in STOP:
            print('TRP is changes to STOP')
        elif asdf in TRP and asdfg in CYS:
            print('TRP is changes to CYS')
        elif asdf in TRP and asdfg in PRO:
            print('TRP is changes to PRO')
        elif asdf in TRP and asdfg in HIS:
            print('TRP is changes to HIS')
        elif asdf in TRP and asdfg in GLN:
            print('TRP is changes to GLN')
        elif asdf in TRP and asdfg in ARG:
            print('TRP is changes to ARG')
        elif asdf in TRP and asdfg in LLE:
            print('TRP is changes to LLE')
        elif asdf in TRP and asdfg in THR:
            print('TRP is changes to THR')
        elif asdf in TRP and asdfg in ASN:
            print('TRP is changes to ASN')
        elif asdf in TRP and asdfg in LEU:
            print('TRP is changes to LEU')
        elif asdf in TRP and asdfg in LYS:
            print('TRP is changes to LYS')
        elif asdf in TRP and asdfg in VAL:
            print('TRP is changes to VAL')
        elif asdf in TRP and asdfg in ALA:
            print('TRP is changes to ALA')
        elif asdf in TRP and asdfg in ASP:
            print('TRP is changes to ASP')
        elif asdf in TRP and asdfg in GLU:
            print('TRP is changes to GLU')
        elif asdf in TRP and asdfg in GLY:
            print('TRP is changes to GLY')
        elif asdf in TRP and asdfg in MET:
            print('TRP is changes to MET')

        if asdf in line and asdfg in line:
            print('MET is changes to PHE')
        elif asdf in line and asdfg in line:
            print('MET is changes to SER')
        elif asdf in line and asdfg in line:
            print('MET is changes to TYR')
        elif asdf in line and asdfg in line:
            print('MET is changes to STOP')
        elif asdf in line and asdfg in line:
            print('MET is changes to CYS')
        elif asdf in line and asdfg in line:
            print('MET is changes to PRO')
        elif asdf in line and asdfg in line:
            print('MET is changes to HIS')
        elif asdf in line and asdfg in line:
            print('MET is changes to GLN')
        elif asdf in line and asdfg in line:
            print('MET is changes to ARG')
        elif asdf in line and asdfg in line:
            print('MET is changes to LLE')
        elif asdf in line and asdfg in line:
            print('MET is changes to THR')
        elif asdf in line and asdfg in line:
            print('MET is changes to ASN')
        elif asdf in line and asdfg in line:
            print('MET is changes to LEU')
        elif asdf in line and asdfg in line:
            print('MET is changes to LYS')
        elif asdf in line and asdfg in line:
            print('MET is changes to VAL')
        elif asdf in line and asdfg in line:
            print('MET is changes to ALA')
        elif asdf in line and asdfg in line:
            print('MET is changes to ASP')
        elif asdf in line and asdfg in line:
            print('MET is changes to GLU')
        elif asdf in line and asdfg in line:
            print('MET is changes to GLY')
        elif asdf in line and asdfg in line:
            print('MET is changes to TRP')