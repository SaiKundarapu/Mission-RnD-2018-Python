__author__='sai'

def get_hcf(first,second):
    hcf=[]
    i=0;j=0
    while(i<len(first) and j<len(second)):
        if first[i][0]==second[j][0]:
            if first[i][1]<second[j][1]:
                hcf.append(first[i])
            else:
                hcf.append(second[j])
            i+=1;j+=1
        elif first[i][0]>second[j][0]:
            j+=1
        else:
            i+=1
    return hcf

def get_lcm(first,second):
    lcm = []
    i = 0;j = 0
    while (i < len(first) and j < len(second)):
        if first[i][0] == second[j][0]:
            if first[i][1] > second[j][1]:
                lcm.append(first[i])
            else:
                lcm.append(second[j])
            i += 1;j += 1
        elif first[i][0] > second[j][0]:
            lcm.append(second[j])
            j += 1
        else:
            lcm.append(first[i])
            i += 1
    while i<len(first):
        lcm.append(first[i])
        i+=1
    while j<len(second):
        lcm.append(second[j])
        j+=1
    return lcm

def multiply(first,second):
    mul=[]
    i = 0;
    j = 0
    while (i < len(first) and j < len(second)):
        if first[i][0] == second[j][0]:
            mul.append((first[i][0],first[i][1]+second[j][1]))
            i += 1;
            j += 1
        elif first[i][0] > second[j][0]:
            mul.append(second[j])
            j += 1
        else:
            mul.append(first[i])
            i += 1
    while i < len(first):
        mul.append(first[i])
        i += 1
    while j < len(second):
        mul.append(second[j])
        j += 1
    return mul