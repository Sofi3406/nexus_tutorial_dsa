# Lists
# https://www.hackerrank.com/challenges/python-lists/problem



if __name__ == '__main__':
    N = int(input())
    list_exercise = []

    for _ in range(N):
        command = input().split()  
        op = command[0]             

        if op == "insert":
            i = int(command[1])
            e = int(command[2])
            list_exercise.insert(i, e)

        elif op == "print":
            print(list_exercise)

        elif op == "remove":
            e = int(command[1])
            list_exercise.remove(e)

        elif op == "append":
            e = int(command[1])
            list_exercise.append(e)

        elif op == "sort":
            list_exercise.sort()

        elif op == "pop":
            list_exercise.pop()

        elif op == "reverse":
            list_exercise.reverse()



