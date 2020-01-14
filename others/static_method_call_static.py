class A(object):
    @staticmethod
    def f1(x):
        return x+1
    @staticmethod
    def f2(x):
        return A.f1(x)+2
    
    
print( A.f1(2),A.f2(2) )
