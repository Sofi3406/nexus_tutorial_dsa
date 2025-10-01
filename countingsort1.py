def countingSort(arr):
    # Initialize a frequency array of size 100 with zeros
    frequency = [0] * 100
    
    # Count occurrences of each number in the input array
    for number in arr:
        frequency[number] += 1
    
    return frequency

if __name__ == '__main__':
    import os

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()