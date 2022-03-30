import traceback

def getCAGR(first, last, years):
    return (last/first) ** (1/years) -1


cagr = getCAGR(65300, 2669000, 20)

print("SEC CAGR : {:.2%}".format(cagr))

# 여러 결과 값 반환.
def myFunc():
    var1 = 'a'
    var2 = [1,2,3]
    var3 = max
    return var1, var2, var3

print(myFunc())

s, l, f = myFunc()
print(s)
print(l)
print(f)


# 람다
insertComma = lambda x : format(x, ',')
print(insertComma(1234567890))