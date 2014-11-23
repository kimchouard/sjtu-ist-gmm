#import user class
# from Point import PointClass
# from Set import SetClass
import FileManager


def main():
    s = FileManager.importSet("data/train.txt")
    s.describe(True)

if __name__ == '__main__':
    main()
