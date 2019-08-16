time = input()

for i in range(int(time)):
    bwt_str = input()
    bwt_data = input().split(" ")
    length = len(bwt_str)
    contig_bwt = list(bwt_str)
    contig = list(bwt_str)
    contig.sort()
    #sorted(contig)

    for i in range(int(length)-1):
        for j in range(int(length)):
            contig[j] = contig_bwt[j]+contig[j]
        #sorted(contig)
        contig.sort()
        #print(contig)

    ans = ""

    for i in range(int(bwt_data[0])):
        index = int(bwt_data[i+2])-1
        ans = ans + contig[index][i*int(bwt_data[1]):i*int(bwt_data[1])+int(bwt_data[1])]
        #print(ans)
    #print(contig)
    print(ans)