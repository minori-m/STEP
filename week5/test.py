# -*- coding: utf-8 -*-

def combine(str1,str2):
    j=0
    k=0
    str1 = str1.decode('utf-8')
    str2 = str2.decode('utf-8')
    str = ""
    for i in range(0,len(str1) + len(str2)):
        if i<2*min(len(str1),len(str2)):
            if i%2==0:
                str+=str1[i/2]
                j += 1
            else:
                str+=str2[(i-1)/2]
                k += 1
        else:
            if j<len(str1):
                str+=str1[j]
                j += 1
            else:
                str+=str2[k]
                k +=1

    return str