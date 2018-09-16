# Funções relacionadas com motivos de proteínas

## Contar motifs

def Count(Motifs):
    k = len(Motifs[0])
    count = {symbol:[0]*k for symbol in "ACGT"}
    for row in Motifs:
        for idx, char in enumerate(row):
            count[char][idx] += 1
    return count


## Contar profiles de motifs

def Profile(Motifs):
    k = len(Motifs[0])
    profile = {'A':[0]*k,'C':[0]*k,'G':[0]*k,'T':[0]*k}
    for i in range(k):
            for j in [t[i] for t in Motifs]:
                profile[j][i] += 1/len(Motifs)
    return profile


def Profile_other(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(0)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            profile[symbol][j] += float(1)/t
    return profile


## Definir consensus de motifs

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


## Definir score de motifs

import sys
def Score(Motifs):
    score = 0
    for cid in range(len(Motifs[0])):
        dic = {Symbol:0 for Symbol in 'ACGT'}
        for row in Motifs:
            dic[row[cid]] += 1
        frequentSymbol = sorted(dic, key=lambda k:dic[k], reverse=True)
        for row in Motifs:
            if row[cid] != frequentSymbol[0]:
                score += 1
    return score


def Score_best(Motifs):
    count = 0
    consensus = Consensus(Motifs)
    for i in range(len(Motifs)):
        count += HammingDistance(Motifs[i], consensus)
    return count

