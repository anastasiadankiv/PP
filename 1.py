def part1(num1,num2) :

    booll = True
    if(num1 < 0 or num2 <0):
        raise Exception('Number must be positive')
    if (num1 % num2 != 0):
        booll = False
    return booll

def part2(s, e):
    arr = []
    if(s <0 or e <0):
        raise Exception('Number must be positive')
    for i in range (s, e+1):
        test=True
        for j in range (2, i):
            if (part1(i,j)):
                test=False
            if(test):
                arr.append(i)

        if len(arr) == 0:
             raise Exception('NoSimpleDigits')
        return arr

arr2=['a',['c',1,3],['f',7,[4,['4']]],[{'la':111}]]
arr3 = []
def part3(l):
    for i in range(0, len(1)):
        if(isinstance(l[i], list)):
            part3(l[i])
        else:
            arr3.append(l[i])
    return arr3
            
