def buildOcc(str, dict):
    Occ_table = [[] for i in range(len(dict))]
    j=0
    for i in dict:
        Occ_table[j].append(i)
        j+=1

    for k in str[1:]:
        for i in range(len(Occ_table)):
            if k == Occ_table[i][0]:
                if len(Occ_table[i]) == 1:
                    Occ_table[i].append(1)
                else:
                    Occ_table[i].append(Occ_table[i][len(Occ_table[i])-1] + 1)
            else:
                if len(Occ_table[i]) == 1:
                    Occ_table[i].append(0)
                else:
                    Occ_table[i].append(Occ_table[i][len(Occ_table[i])-1])
    return Occ_table


def buildC(str):
    chr = str[0]
    C_dict = {str[0]:0}
    for i in range(len(str)):
        if chr != str[i]:
            chr = str[i]
            C_dict.setdefault(chr, i)
    return C_dict

def buildBWT(str):
    length = len(str)
    contig_bwt = list(str)
    contig = list(str)
    contig.sort()
    for i in range(int(length)-1):
        for j in range(int(length)):
            contig[j] = contig_bwt[j]+contig[j]
        contig.sort()
    return contig

time = input()
for i in range(int(time)):
    bwt_str = input()
    bwt_index = input()
    LF= buildBWT(bwt_str)

    L = "L"
    F = "F"
    for i in range(len(LF)):
        L += LF[i][-1]
        F += LF[i][0]

    C = buildC(F[1:])
    Occ = buildOcc(L, buildC(F[1:]))
    index = int(bwt_index)
    ans = ""
    for i in range(len(bwt_str)):
        ans = L[index]+ans
        Occ_index=0
        for j in range(1, len(Occ)):
            if L[index] == Occ[j][0]:
                Occ_index = j

        test1 = C[str(L[index])]
        test2 = Occ[Occ_index][index]
        index = C[str(L[index])] + Occ[Occ_index][index]

    print(ans)