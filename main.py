#import user class
# from Point import PointClass
# from Set import SetClass
import FileManager
import Plot
from EM import EMalgo


def main():
    s = FileManager.importSet("data/train.txt")
    # Plot.plotSet(s)
    em = EMalgo(s, 4)
    em.run()

if __name__ == '__main__':
    main()
