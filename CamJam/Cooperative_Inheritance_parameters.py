class A(object):
    def __init__(self, a, **book):
        super(A, self).__init__(**book)
        print "entering A"
        self.a = a
        print self.a
        print "leaving A"


class B(object):
    def __init__(self, b, **book):
        super(B, self).__init__(**book)
        print "entering B"
        self.b = b
        print self.b
        print "leaving B"


class C(object):
    def __init__(self, c, **book):
        super(C, self).__init__(**book)
        print "entering C"
        self.c = c
        print self.c
        print "leaving C"


class D(A, B, C):
    def __init__(self, a=0, b=0, c=0, d=0):
        super(D, self).__init__(a=a, b=b, c=c)
        print "entering D"
        self.d = d
        print self.d
        print "leaving D"

test = D(-1,-2,8)
#test2 = D(c=9)
