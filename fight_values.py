# Create Functions that will read and hold values
# Declare variables
class Fightvalues:
    def __init_(self, first, last, nickname, height, weight,
             reach, stance, win, lose, draw):
            self._first = first
            self._last = last
            self._nickname = nickname
            self._height = height
            self._weight = weight
            self._reach = reach
            self._stance = stance
            self._win = win
            self._lose = lose
            self._draw = draw

# Make Getters and Setters to Retrieve Values

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        self._first = value

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        self._last = value

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def reach(self):
        return self._reach

    @reach.setter
    def reach(self, value):
        self._reach = value

    @property
    def stance(self):
        return self._stance

    @stance.setter
    def stance(self, value):
        self._stance = value

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, value):
        self._win = value

    @property
    def lose(self):
        return self._lose

    @lose.setter
    def lose(self, value):
        self._lose = value

    @property
    def draw(self):
        return self._draw

    @draw.setter
    def draw(self, value):
        self._draw = value

    