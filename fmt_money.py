def FormatMoney(money):
    x = str(money)
    if len(x) <= 3:
        return '$ ' + x
    else:
        a = x[:-3]
        b = x[-3]
    return FormatMoney(a) + '.' + b
