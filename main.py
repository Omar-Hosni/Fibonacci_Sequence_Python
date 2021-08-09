n_sequence = int(input('Enter number of sequence: '))

# default first terms
n1,n2 = 0,1
counter = 0

if n_sequence <= 0:
    print('Please enter a positive number')
elif n_sequence == 1:
    print('Fibonacci sequence is up to ' + n_sequence + ': ')
    print(n1)
else:
    print('Fibonacci sequence: ')
    while counter < n_sequence:
        print(n1)
        nth = n1 + n2
        #change values to greater
        n1 = n2
        n2 = nth
        counter += 1
