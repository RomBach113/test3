# Напишите программу, 
# которая определит позицию второго вхождения строки 
# в списке либо сообщит, что её нет.

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

sp=["qwe", "asd", "zxc","qwe", "ertqwe" ]
find = "qwe"

def position (lst,el):
    l=[]
    isExist=False
    for i in range(len(lst)):
        if lst[i]==el:
            isExist = True
            l.append(i)
    if isExist == False:
        return False
    return l[1]


# def nonpos (lst,el):
#     l=[]
#     for i in range(len(lst)):
#         if lst[i]!=el:
#             l='nine'
#     return l

# def prnt ():

    

print(position(sp,find)) 