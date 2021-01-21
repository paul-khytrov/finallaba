try:
    def binary_to_dec(i):
        a = int(i, 2)
        return a


    def binary_to_hex(i):
        a = hex(int(i, 2))
        return a


    def binary_to_oct(i):
        a = oct(int(i, 2))
        return a


    def dec_to_binary(i):
        a = int(i, 2)
        return a


    def dec_to_oct(i):
        a = oct(i)
        return a


    def dec_to_hex(i):
        a = hex(i)
        return a


    def oct_to_dec(i):
        a = int(i, 8)
        return a


    def oct_to_hex(i):
        a = hex(int(i, 8))
        return a


    def oct_to_binary(i):
        a = int(int(i, 8), 2)
        return a


    def hex_to_dec(i):
        a = int(i, 16)
        return a


    def hex_to_oct(i):
        a = int(int(i), 8)
        return a


    def hex_to_binary(i):
        a = int(int(i, 2), 16)
        return a



    i = input("Enter number:")
    first = input("What is this number?")
    second = input("How do you want to convert it?")


    if first == 'binary' and second == 'decimal':
        print(repr(i) + 'in decimal is ' + repr(binary_to_dec(i)))

    elif first == 'binary' and second == 'hex':
        print(repr(i) + 'in hex is ' + repr(binary_to_hex(i)))

    elif first == 'binary' and second == 'oct':
        print(repr(i) + 'in oct is ' + repr(binary_to_oct(i)))

    elif first == 'decimal' and second == 'hex':
        print(repr(i) + 'in hex is ' + repr(dec_to_hex(i)))

    elif first == 'decimal' and second == 'binary':
        print(repr(i) + 'in binary is ' + repr(dec_to_binary(i)))

    elif first == 'decimal' and second == 'oct':
        print(repr(i) + 'in oct is ' + repr(dec_to_oct(i)))

    elif first == 'oct' and second == 'hex':
        print(repr(i) + 'in hex is ' + repr(oct_to_hex(i)))

    elif first == 'oct' and second == 'binary':
        print(repr(i) + 'in binary is ' + repr(oct_to_binary(i)))

    elif first == 'oct' and second == 'decimal':
        print(repr(i) + 'in decimal is ' + repr(oct_to_dec(i)))

    elif first == 'hex' and second == 'decimal':
        print(repr(i) + 'in decimal is ' + repr(hex_to_dec(i)))

    elif first == 'hex' and second == 'binary':
        print(repr(i) + 'in binary is ' + repr(hex_to_binary(i)))

    elif first == 'hex' and second == 'oct':
        print(repr(i) + 'in oct is ' + repr(hex_to_oct(i)))
    else:
        print('Wrong!')
except ValueError:
    print('Wrong value!')
