def large_power(base,exponent):
        r = base**exponent
        if r>5000:
            return True
        else:
            return False



def divisible_by_ten(num):
    r = num%10
    if r==0:
        return True
    else:
        return False
