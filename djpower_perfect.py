from diff_coeff import diff_coeff


def dj_power(diff: int, is_sc: bool):
    print(diff_coeff(diff, is_sc))
    return diff_coeff(diff, is_sc) * 2.22 + 2.31

print(dj_power(7, False))
