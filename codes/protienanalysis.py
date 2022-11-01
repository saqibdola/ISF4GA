y= 0
ws= 1
gn= 0
gene=[]
with open('MT750051.fasta') as f1, open('MT750059.fasta') as f2:
    for lineno, (line1, line2) in enumerate(zip(f1, f2), 1):
        for i in range(min(len(line1), len(line2))):
            if line2[0] == '>':
                gene = line2
                gn = gn + 1  # int(line2[0])
                ws = ws + 1

                # print('ASDF', gn)
                break
            if line1[i] == line2[i]:
                ws = ws + 1
            else:
                if line1[i] == 'X' or line2[i] == 'X': # any amino acid
                    ws = ws + 1
                elif line1[i] == 'B' or line2[i] == 'B': # B can be either N or D
                    ws = ws + 1
                elif line1[i] == 'J' or line2[i] == 'J': # J can be either I or L
                    ws = ws + 1
                #elif line1[i] == 'O' or line2[i] == 'O':
                #    ws = ws + 1
                #elif line1[i] == 'U' or line2[i] == 'U':
                 #   ws = ws + 1
                elif line1[i] == 'Z' or line2[i] == 'Z': # Z can be either Q or E
                    ws = ws + 1
                elif line1[i] == '\n' or line2[i] == '\n':
                    ws = ws + 1
                    pass
                else:
                    y = y+1
                    ws=ws+1
                    print('mismatch in line no:', lineno, ', location in line:', i + 1,
                          'overall location', int(ws)-lineno, line1[i], line2[i], gene)

                    print('Y',y)

                    lineeee = lineno

    print(ws, lineno)
    taa = ((ws-lineno)-1)
    print(taa)
    MR = (y/taa)*100
    print('Mutation Rate:', MR)