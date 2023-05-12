


class measurement:
    def __init__(self, name):
        self.__title = name
        self.__mtop = None
        self.__uncertStat = None
        self.__uncertModel = None
        self.__uncertExp = None
        self.__uncertTheory = None
        self.__uncertTotal = None
        self.__ref = None
        self.__lumi = None


    def setResult(self, mtop, totuncert):
        self.__mtop = mtop
        self.__uncertTotal = totuncert

    def setUncertainties(self, stat=0, exp=0, mod=0, theo=0):
        self.__uncertStat = stat
        self.__uncertModel = mod
        self.__uncertExp = exp
        self.__uncertTheory = theo

    def setReference(self, ref):
        self.__ref = ref

    def setLumi(self, lumi):
        self.__lumi = lumi

    def title(self):
        return self.__title

    def reference(self):
        return self.__ref

    def mtop(self):
        return self.__mtop

    def uncertStat(self):
        return self.__uncertStat

    def uncertTotal(self):
        return self.__uncertTotal

    def uncertModel(self):
        return self.__uncertModel

    def uncertExp(self):
        return self.__uncertExp

    def uncertTheory(self):
        return self.__uncertTheory
