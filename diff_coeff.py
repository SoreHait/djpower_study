def diff_coeff(diff: int, is_sc: bool):
    if is_sc:
        if diff <= 8:
            return diff + 22
        else:
            return (diff - 8) * 2 + 30
    else:
        return diff * 2

if __name__ == '__main__':
    print(diff_coeff(14, True))
