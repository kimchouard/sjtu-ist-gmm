#import user class
# from Point import PointClass
# from Set import SetClass
import FileManager
import Plot


def main():
    s = FileManager.importSet("data/train.txt")
    Plot.plotSet(s)

if __name__ == '__main__':
    main()
