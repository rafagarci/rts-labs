def counter(arr: list, val: float) -> list:
    '''
    Computes the number of elements in an array
    that are above and below a specific value

        Parameters
            arr(list):      Input array
            val(float):     Value to compare array's values to

        Return
            result(list):   List containing the number of elements in arr
                            below and above val
    '''

    below = 0
    above = 0

    # Main execution loop
    for i in arr:
        if i < val:
            below += 1
        elif i > val:
            above += 1
    
    return [below, above]

def main():
    while True:
        arr = input('Type array numbers separated by commas, only type numbers, commas, and spaces: ')
        arr = arr.split(',')
        arr = list(map(lambda x: x.strip(), arr))
        arr = list(filter(None, arr))
        arr = list(map(lambda x: float(x), arr))
        val = input('Type a number: ')
        val = float(val)
        result = counter(arr,val)
        print('Above: ' + str(result[0]) + ', Below: ' + str(result[1]))

if __name__ == '__main__':
    main()