class vector(object):
    def __init__(self,list1,list2):
        self.diff = (list2[0]-list1[0],list2[1]-list1[1])
        print (self.diff)

a = (20.0,25.0)
b = (40.0,55.0)

thing = vector(a,b)
