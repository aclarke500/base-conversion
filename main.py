import base_conversion
import math


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

print(len(sign))
print(len(exp))
print(len(mantissa))

print(sign)
print(exp)
print(mantissa)

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


print(mantissa_to_decimal(mantissa, 1))
print(22/7)
print(math.pi)
print(223/71)
