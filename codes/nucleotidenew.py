from dna import remainder
from dna1 import checking

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
y= 0
ws= 0

PQR=['N', 'Y' , 'K' ,'M' ,'S', 'W', 'B', 'D', 'H', 'V']
with open('MZ292138nucleotide.fasta') as f1, open('BS001082nucleotide.fasta') as f2:
    for lineno, (line1, line2) in enumerate(zip(f1, f2), 1):
          for i in range(min(len(line1), len(line2))): #
                if line1[0] == '>':
                    break
                if line1[i] == line2[i]:
                    ws = ws + 1
                elif line1[i] in PQR or line2[i] in PQR: #N
                     ws = ws + 1
                     pass
                elif line1[i] == '\n' or line2[i] == '\n':
                     ws = ws + 1
                     pass
                else:
                            ws = ws + 1
                            y = y + 1
                            print ('mismatch', y, 'in line no:', lineno, ', location in line:', i+1, ', '
                              'overall location', int(ws)-(lineno-1)+1, line1[i], line2[i], ws, lineno)#int(g)+1, line1[i], line2[i], gene)
                            print('Y',y) # total mutations with last one due to space skippes

    taa = ((ws - lineno)+1)
    print('taa',taa)
    MR = (y/(taa))*100 #plus 1 for extra space counted as mtation in last
    print('Mutation Rate:', MR)
