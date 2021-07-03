import pandas as pd

file1 = pd.read_csv(r'houseelf_earlength_dna_data.csv')

columnList = ['ID', 'Ear_Size', 'GC_Content']
table1 = pd.DataFrame(columns=columnList)

smallAvgGCC = 0
largeAvgGCC = 0

for index in file1.index:
    # ID
    elfId = file1['id'][index]

    # DNA
    dnaSeq = file1['dnaseq'][index]
    dnaSeqLen = dnaSeq.__len__()
    gc = 0
    for dna in dnaSeq:
        if dna == 'G' or dna == 'C':
            gc += 1
    gcContent = gc/dnaSeqLen

    # Ear size
    earLength = file1['earlength'][index]
    if earLength <= 10:
        earSize = 'small'
        smallAvgGCC += earLength
    else:
        earSize = 'large'
        largeAvgGCC += earLength


    # table
    record = [elfId, earSize, gcContent]
    table1.loc[index] = record

print(table1)
print("Average GC-Content of small-eared elves: " + str(smallAvgGCC))
print("Average GC-Content of large-eared elves: " + str(largeAvgGCC))

table1.to_csv(r'grangers_analysis.csv')
print("The analysis is exported to csv: grangers_analysis.csv")