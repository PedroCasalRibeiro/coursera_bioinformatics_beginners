# Encontrar “DnaA box” em DNA circular

## Funções para descobrir padrões em DNA circular

### Descobrir o valor do padrão de input

def PatternCount(Text, Pattern): 
    count = 0 
    for i in range(len(Text)-len(Pattern)+1): 
        if Text[i:i+len(Pattern)] == Pattern: 
            count = count+1 
    return count

def PatternCount_oneliner(Text,Pattern):
    count = 0 
    return sum([ count+1 for i in range (len(Text)-len(Pattern)+1) if Text[i:i+len(Pattern)] == Pattern])

import re
def PatternCount_best(TEXT, PATTERN):
    return len(re.findall('(?=' + PATTERN + ')', TEXT))


### Dicionário com os possíveis padrões e os seus valores

def FrequencyMap(Text, k): 
    freq = {} 
    n = len(Text) 
    for i in range(n-k+1): 
        Pattern = Text[i:i+k] 
        freq[Pattern] = 0 
    for i in range(n-k+1): 
        if Text[i:i+k] == Pattern: 
            freq[Pattern] = freq[Pattern] + 1 
    return freq


### Encontrar posição inicial dos padrões encontrados no genoma

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1): 
        if Genome[i:i+len(Pattern)] == Pattern: 
            positions.append(i)
    return positions

import re
def PatternMatching_best(Pattern, Genome):
    return [m.start() for m in re.finditer('(?='+Pattern +')', Genome)]


### Retornar lista com padrões cm valores maiores (para ser usado com função FrequencyMap)

def FrequentWords(Text, k): 
    words = []
    freq = FrequencyMap(Text, k) 
    m = max(freq.values()) 
    for key,value in freq.items(): 
        if value == m: 
            words.append(key) 
    return words


### Retornar lista com localizações dos padrões

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


### Retornar valores com diferenças entre G e C

def SkewArray(Genome):
    skew = {0:0}
    values = {'A':0, 'T':0, 'C':-1, 'G':1}
    for i in range(0, len(Genome)):
        skew[i+1] = skew[i] + values[Genome[i]]
    return skew.values()


### Retornar valores mínimos das diferenças entre G e C

def MinimumSkew(Genome):
    skew = [0]
    for i in range(len(Genome)):
        skew.append(skew[i] + {'A':0,'C':-1,'G':1,'T':0}[Genome[i]])
    m = min(skew)
    return [i for i in range(len(skew)) if skew[i] == m]


### Retornar soma das diferenças entre duas strings através do índice

def HammingDistance(p, q):
    count = 0
    for i in range (len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def HammingDistance_best(p, q):
    count = 0
    [count+1 for i in range (len(p)) if p[i] != q[i]]
    return count


### Encontrar posições iniciais de todos os padrões aproximados encontrados num texto

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # output variable
    for i in range(0, len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i+len(Pattern)],Pattern) <= d: 
            positions.append(i)
    return positions


### Contador de todos os padrões aproximados encontrados num texto

def ApproximatePatternCount(Pattern, Text, d):
    count = 0 
    for i in range(0, len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern,Text[i:i+len(Pattern)]) <= d: 
            count += 1
    return count

