class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        print(self.pos_x)
        
        if ((x_2 >= self.pos_x) and (x_1 <= self.pos_x)) and ((y_2 >= self.pos_y) and (y_1 <= self.pos_y)):
            return True
        else:
            return False
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_hit = []
        # center (2,3) , fire range 3 , ranges: bl: (0,-1) (5,6)
        x_1 = x - self.__fire_range # 0
        print(x_1)
        y_1 = y - self.__fire_range  # -1
        print(y_1)
        x_2 = x + self.__fire_range # 5
        print(x_2)
        y_2 = y + self.__fire_range  # 6
        print(y_2)
        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                units_hit.append(unit)
        return units_hit
        pass
