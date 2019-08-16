time = input()

for i in range(int(time)):
    bwt_str = input()
    bwt_index = input()
    length = len(bwt_str)
    contig_bwt = list(bwt_str)
    contig = list(bwt_str)
    contig.sort()

    for i in range(int(length)-1):
        for j in range(int(length)):
            contig[j] = contig_bwt[j]+contig[j]
        contig.sort()
    print(contig[int(bwt_index)-1])