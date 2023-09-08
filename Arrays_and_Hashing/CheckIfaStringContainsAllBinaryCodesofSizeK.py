def check_if_string_contains_all_bny_codes(s,k):
    codeset = set()
    for i in range(len(s)-k+1):
        codeset.add(s[i:i+k])

    return len(codeset)==2**k


if __name__ == '__main__':
    s = "00110110"
    k = 2
    val = check_if_string_contains_all_bny_codes(s, k)
    print(val)