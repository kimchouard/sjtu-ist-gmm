class PointClass:
    def __init__(self, d1, d2, label):
        self.d1 = d1
        self.d2 = d2
        self.label = label

    def describe(self):
        print "Point %d at %f x %f" % (self.label, self.d1, self.d2)
