
## class
class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it.'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis kay -')

mfc = MyFirstClass()

print(mfc.clsVar)

print(mfc.clsMethod())


## 상속
class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's mothodB")

class C(A, B):
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overtime method")
        super().method()  # Calling A's method


c = C()
c.methodA()
c.methodB()
c.methodC()
c.method()



## 클래스 메서드
class NasdaqStock:
    """Class for NASDAQ stocks""" # 독스트링
    count = 0 # 클래스 변수
    def __init__(self, symbol, price):
        """Constructor for NasdaqStock""" # 독스트링
        self.symbol = symbol # 인스턴스 변수
        self.price = price # 인스턴스 변수
        NasdaqStock.count+= 1
        print('Calling __init__ {}, {:.2f} > count : {}'.format
              (self.symbol, self.price, NasdaqStock.count))
    def __del__(self):
        """Destructor for NasdaqStock""" # 독스트림
        print('Calling __del__ ({})'.format(self))

gg = NasdaqStock('GOOG', 1154.05)
del(gg) ## 명시적으로 인스턴스 제거한다.

ms = NasdaqStock('MSFT', 102.44)
del(ms)

amz = NasdaqStock('AMZN', 1746.00)
del(amz)

