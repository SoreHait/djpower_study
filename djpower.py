def diff_coeff(diff: int, is_sc: bool):
    if is_sc:
        if diff <= 8:
            return diff + 22
        else:
            return (diff - 8) * 2 + 30
    else:
        return diff * 2

def dj_power(diff: int, is_sc: bool):
    print(diff_coeff(diff, is_sc))
    return diff_coeff(diff, is_sc) * 2.22 + 2.31

print(dj_power(4, True))
