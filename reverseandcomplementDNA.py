# Funções para fazer DNA complementar e inverter o sentido da leitura de DNA

## Complement DNA

MAPPING = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
def Complement (Pattern):
    return ''.join(MAPPING[c] for c in Pattern)


## Reverse DNA

def Reverse(Pattern):
    return Pattern[::-1]


## Reverse + Complement DNA

def ReverseComplement(Pattern):   
    return(Pattern[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper())

