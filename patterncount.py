
# coding: utf-8


#Funções para descobrir padrões em DNA circular
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

