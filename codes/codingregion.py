from dna import remainder
from dna1 import checking

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
gene = []
gn = 0
C= 0
ws= 0
gen = 0
PQR=['N', 'Y' , 'K' ,'M' ,'S', 'W', 'B', 'D', 'H', 'V']

with open('MZ292138CRJAN2021.fasta') as f1, open('BS001082-Feb2021.fasta') as f2:
    for lineno, (line1, line2) in enumerate(zip(f1, f2), 1):
          for i in range(min(len(line1), len(line2))): #
                if line1[0] == '>':
                    gene = line2
                    gn = gn + 1
                    gen = gen -1
                    break
                if line1[i] == line2[i]:
                    ws = ws + 1
                else:
                    if line1[i] in PQR or line2[i] in PQR:
                        ws = ws + 1
                        pass
                    elif line1[i] == '\n' or line2[i] == '\n':
                        ws = ws + 1
                        pass
                    else:
                         ws = ws + 1
                         C = C + 1
                         print ('mismatch', C, 'in line no:', lineno, ', location in line:', i+1, ', '
                                'overall location', int(ws)-(lineno-1)-gen, line1[i], line2[i], gene) # lineno, ws, gen)#int(g)+1, line1[i], line2[i], gene)
                         asdf, asdfg  = remainder(i, line1, line2)
                         print('The codon', asdf, 'is changed to', asdfg)
                         checking(asdf, asdfg)
                         print('C',C)

    taa = ((ws - lineno)+gn)
    tnb= (lineno-gn)*60
    print('taa',taa)
    MR = (C/taa)*100
    print('Mutation Rate:', MR)
