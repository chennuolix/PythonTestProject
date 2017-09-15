class MixInA(object):
    def parse(self):
        print(self._mixInA)


class MixInB(object):
    def make(self):
        print(self._mixInB)


class MixInC(MixInA, MixInB):


    def printAll(self):
        print(self._mixInA, self._mixInB)


mixInC = MixInC()
mixInC._mixInA = "aaaaa"
mixInC.parse()
