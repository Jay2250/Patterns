from os import system
while 1:
    print('1.\t  *\n\t ***\n\t*****\n\n2.\t*****\n\t ***\n\t  *\n\n3.\t *** \n\t  *  \n\t ***\n\n4.\t  *\n\t ***\n\t  *\n\n5.\t Quit\n')
    opt = int(input('Choice the Pattern you want to print\n'))

    if opt == 1:
        num = int(input('Enter number of layers\n'))
        i = 1
        while i<=num:
            j = 1
            while j <= num - i:
                print(' ', end='')
                j += 1
            j = 1
            while j <= 2*i-1:
                print('*',end='')
                j += 1
            print()
            i += 1

    elif opt == 2:
        num = int(input('Enter number of layers\n'))
        i = 1
        while i<=num:
            j = 1
            while j<=i-1:
                print(' ',end='')
                j += 1
            j = 1
            while j<= 2*num-(2*i-1):
                print('*',end='')
                j += 1
            print()
            i += 1

    elif opt == 3:
        num = int(input('Enter number of layers\n'))
        n = (num+1)/2
        i=1
        while i<=num:
            if i<=n:
                s = 2*n-(2*i-1)
                d = i-1
            else:
                s = 2*i-num
                d = num-i
            j = 1
            while j <= d:
                print(' ', end='')
                j += 1
            j = 1
            while j <= s:
                print('*', end='')
                j += 1
            print()
            i += 1
    elif opt == 4:
        num = int(input('Enter number of layers\n'))
        n = (num+1)/2
        i=1
        while i<=num:
            if i<=n:
                s = 2*i-1
                d = n-i
            else:
                s = num*2-(2*i-1)
                d = i-n
            j = 1
            while j <= d:
                print(' ', end='')
                j += 1
            j = 1
            while j <= s:
                print('*', end='')
                j += 1
            print()
            i += 1

    elif opt == 5:
        break

    else:
        print('Invalid Input')
        continue
    pause = input("Press 'Enter' to continue")
    system('cls')