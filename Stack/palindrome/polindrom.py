import time
from Stack.linkedstack import LinkedStack
from pathlib import Path


class PolindromADT(object):
    def __init__(self):
        self.words = []
        self.palidroms = []

    def read(self, path, format=lambda x: x.strip()):
        f = open(path, encoding="utf-8")
        self.words = list(map(format, f.readlines()))
        # self.words = [word.strip() for word in f.readlines()]

    @staticmethod
    def __is_polindrom(word):
        word = word.lower()
        stk = LinkedStack()
        for i, c in enumerate(word):
            if i < len(word) // 2:
                stk.push(c)
            elif i >= (len(word) - 1) // 2 + 1:
                if c != stk.pop():
                    return False
        return True

    def process(self):
        self.palidroms = list(filter(PolindromADT.__is_polindrom, self.words))

    def write(self, path):
        path = Path(path)
        path.parent.mkdir(exist_ok=True)
        new_words = list(map(lambda x: x + "\n", self.palidroms))
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_words)


if __name__ == "__main__":
    pl = PolindromADT()
    pl.read("../data/in/words.txt")
    pl.process()
    pl.write("../data/out/palindrome_en.txt")

    pl.read("../data/in/base.lst", format=lambda x: x.strip().split(" ")[0])
    pl.process()
    pl.write("../data/out/palindrome_uk.txt")
