#3 модуль 2 урок
a='ABCAAC1C'
'''print(a.count('A'))'''
'''def strcounter(a): #O(N*M)
    for char in set(a):      # set-множества , единственый экземпляр символа
        counter=0
        for sub_char in a:
            if char==sub_char:
                counter+=1
        print(char,counter)
strcounter(a)'''

'''def strcounter2(a):  # O(N**2)
    for char in (a):
        counter=0
        for sub_char in a:
            if char==sub_char:
                counter+=1
        print(char,counter)
strcounter2(a)'''

def strcounter3(a):  #O(N)
    syms_counter={}
    for char in a:
        syms_counter[char]=syms_counter.get(char, 0) + 1
    print(syms_counter)
strcounter3(a)

# пишу новый код аплапллп
