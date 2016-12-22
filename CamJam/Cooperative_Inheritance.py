class A(object):
    def __init__(self):
        print "entering A"
        super(A, self).__init__()
        print "leaving A"


class B(object):
    def __init__(self):
        print "entering B"
        super(B, self).__init__()
        print "leaving B"


class C(object):
    def __init__(self):
        print "entering C"
        super(C, self).__init__()
        print "leaving C"


class D(A, B, C):
    def __init__(self):
        print "entering D"
        super(D, self).__init__()
        print "leaving D"

test = D()
