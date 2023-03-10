def max_subarray(array):
    maxArrSum = 0
    currentSum = 0

    for num in array:
        currentSum += num

        if currentSum > maxArrSum:
            maxArrSum = currentSum
        elif currentSum < 0:
            currentSum = 0
        
    return maxArrSum        

def two_sum(array, target):
    for idx1, num1 in enumerate(array):
        for idx2, num2 in enumerate(array):
            if num1 + num2 == target:
                #print('if dziala')
                ret = [idx1, idx2]
                return f'nums on {ret} id\'s add up to the {target}'
    return 'There are not numbers that add up to the target!'

def moveZeros(array):
    helpArr = []
    for idx, val in enumerate(array):
        if val == 0:
            helpArr.append(array.pop(idx))
    
    for i in range(len(helpArr)):
        array.append(0)

    return array

def conDupli(array):
    for idx, val in enumerate(array):
        if val in array[:idx] or val in array[idx+1:]:
            return True
    return False

def rotateArray(array, step):
    rotatedArr = [0 for i in range(len(array))]

    for idx, val in enumerate(array):
        if idx + step < len(array):
            rotatedArr[idx+step] = val
        elif idx + step >= len(array):
            rotatedArr[idx+step-len(array)] = val

    return rotatedArr

def findLowest(array):
    for num in array:
        for num2 in array:
            if 2*num <= num2:
                pass

if __name__ == '__main__':
    # Two Sum 
    '''array = list(map(float, input('array: ').split()))
    target = float(input('target: '))
    print(two_sum(array=array, target=target))'''

    # Maximum subarray
    '''array = list(map(int, input('array: ').split()))
    print(max_subarray(array=array))  '''

    # Move zeros
    '''array = list(map(int, input('array: ').split()))
    print(moveZeros(array=array))'''

    # Contains duplicate
    '''array = list(map(int, input('array: ').split()))
    print(conDupli(array=array))'''

    # Rotate array
    '''array = list(map(int, input('array: ').split()))
    k = int(input('k: '))
    print(rotateArray(array=array, step=k))'''

    # 2576. Find the Maximum Number of Marked Indices
    array = list(map(int,input('array: ').split()))
    print(findLowest(array=array))
