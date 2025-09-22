def add(a, b):
    """This add function is for two no. only"""
    value = a + b
    return value


def hcf(a, b):
    """Here r starts from -1 to initiate loop"""
    r = -1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a


n1 = int(input("ENTER 1ST NO."))
n2 = int(input("ENTER 2ND NO."))
ans = add(n1, n2)
print("SUMMATION::", ans)
print(add.__doc__)  # USE OF DOCSTRING ALSO HOW TO PRINT
HCF = hcf(n1, n2)
print("HCF::", HCF)
print(hcf.__doc__)


