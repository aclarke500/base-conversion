import base_conversion

# part 1
numbers_for_question_1 = [49, -31, 120, -128, 128]


for num in numbers_for_question_1:
    if base_conversion.twos_complement_bi(num):
        print(base_conversion.twos_complement_bi(num))

    else:
        print("overflow occured")

print()
# part 2


val='0'+str(base_conversion.hex_to_bi('40490fdb'))
print(val)

exp =''
sign=''
mantissa=''

for i in range(len(val)):
    if i == 0:
        sign += val[i]
    elif i > 0 and i <= 8:
        exp += val[i]
    else:
        mantissa += val[i]



def mantissa_to_decimal(mantissa, exp):
    # if not str to begin with results may be wonky
    mantissa='1'+str(mantissa)
    # implied 1 is added here

    value=0
    index = 0

    while index < len(mantissa):
        value+= int(mantissa[index])*2**exp

        index+=1
        exp-=1 # decrease exponent like you would
        # if counting by hand

    return value


print(mantissa_to_decimal(mantissa, 1), "shoe")

# 2B


def fractional_binary_representation(value):

    # this could be implemented as an argument
    precision = 25
    binary_representation=''

    value=float(value)
    # find out scale of the value
    scale = 0

    while value>2**scale:
        scale+=1

    value_left_to_represent = value
    
    for i in range(precision):

        if 2**scale <= value_left_to_represent and value_left_to_represent > 0:
            value_left_to_represent-=2**scale
            binary_representation+='1'
        else:
            binary_representation+='0'

        if scale == 0:
            binary_representation+='.'
        scale-=1
    return binary_representation


c_rep_of_pi =fractional_binary_representation(mantissa_to_decimal(mantissa, 1))
frac_rep_of_pi = fractional_binary_representation(22/7)
print(c_rep_of_pi)
print(frac_rep_of_pi)

# 2C

def remove_integer_part_of_float(value):

    for i in range(len(value)):
        if value[i] == '.':
            index_of_point=i

    fractional_part_of_float =''

    for i in range(index_of_point+1, len(value)):
        fractional_part_of_float+=value[i]

    return fractional_part_of_float


def find_converging_point(val1, val2):
    # assuming strings are the same length
    # for more general case, iterate over and make sure . is at same index
    # add 0s as padding if not case

    # relevant to point
    decimal_place = 0
    for i in range(len(val1)):
        decimal_place+=1
        if val1[i] == '.' and val2[i] == '.':
            decimal_place = 0

        if val1[i] != val2[i]:
            return i+1


fractional_part_of_c_rep = remove_integer_part_of_float(c_rep_of_pi)
fractional_part_of_frac_pi = remove_integer_part_of_float(frac_rep_of_pi)

print(find_converging_point(fractional_part_of_c_rep, fractional_part_of_frac_pi))

