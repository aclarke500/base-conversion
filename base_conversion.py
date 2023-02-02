def hex_to_dec(hex_string):
    # first we must reverse the string
    hex_string=hex_string[::-1]
    # we will iterate over the string, summing the values at each char
    # like how 128 is 100 + 020 + 8
    sum = 0 
    for i in range (len(hex_string)):

        if convert_char_to_hex_number(hex_string[i]) != None:
            sum += convert_char_to_hex_number(hex_string[i])*(16**i)
        else:
            print("invalid input at index ", len(hex_string)-i, "character: ", hex_string[i])
            return None

    return sum



def convert_char_to_hex_number(hex_char):
    # return 0-9 right away
    if hex_char.isnumeric():
        return  int(hex_char)

    valid_hex_chars = 'ABCDEF'
    value_of_hex_char = 10

    value_of_hex_char = 10

    for i in range(len(valid_hex_chars)):

        if hex_char == valid_hex_chars[i]:

            return value_of_hex_char
        # a is 10, b is 11, keep this value aligned with index    
        value_of_hex_char+=1

    # same thing but for lowercase numbers
    valid_hex_chars = 'abcdef'
    value_of_hex_char = 10

    for i in range(len(valid_hex_chars)):

        if hex_char == valid_hex_chars[i]:

            return value_of_hex_char
        # a is 10, b is 11, keep this value aligned with index    
        value_of_hex_char+=1

    return None



def dec_to_bi(dec_string):
    # assume string
    dec_string = str(dec_string)

    dec_number = int(dec_string)
    val = 0
    power = 0
    while val <= dec_number:
        val = 2**power
        power += 1
    power -= 1

    list_of_indexes_that_are_one = []

    for i in reversed(range(power)):
        if 2**i <= dec_number:
            list_of_indexes_that_are_one.append(i)
            dec_number -= 2**i


    binary_number =''
    for i in reversed(range(power)):
        if list_of_indexes_that_are_one.count(i):
            binary_number+='1'
        else:
            binary_number+='0'


    return(binary_number)

def hex_to_bi(number):

    number_as_string=str(number)
    decimal_representation = hex_to_dec(number_as_string)
    binary_representation = dec_to_bi(decimal_representation)

    return binary_representation



