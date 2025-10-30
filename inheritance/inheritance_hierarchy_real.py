class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        self.__num_arrows = num
        if num < 0:
            raise Exception("not enough arrows")
        else:
           num = num - 1
           print(num)
           return num
       
        


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)
        pass

    def triple_shot(self, target):
        arrow = self.get_num_arrows()
        self.use_arrows(self.use_arrows(self.use_arrows(self.use_arrows(arrow))))
        return f"{target.get_name()} was shot by 3 crossbow bolts"
        pass
