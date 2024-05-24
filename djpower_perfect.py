from diff_coeff import diff_coeff


def djpower_pp(diff: int, is_sc: bool):
    return diff_coeff(diff, is_sc) * 2.22 + 2.31

if __name__ == '__main__':
    diff = 14
    is_sc = True
    print(diff_coeff(diff, is_sc))
    print(djpower_pp(diff, is_sc))
