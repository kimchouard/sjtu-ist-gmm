#import user class
from Point import PointClass
from Set import SetClass


def main():
    p1 = PointClass(1.023982, -0.871344, 1)
    p2 = PointClass(0.669370, -0.492466, 2)
    s = SetClass()
    s.add(p1)
    s.add(p2)
    s.describe()

if __name__ == '__main__':
    main()
