import classes
from classes import Point


class UiControl:
    def draw(self):
        return "Draw method Ui control"

class ApiControl:
    def draw(self):
        return "Draw method Api control"

ui_control = UiControl()
api_control = ApiControl()
controls = [ui_control, api_control]

def lops(lists):
    for list in lists:
        print(list.draw())

lops(controls)

import_class = Point(2, 3)
print(import_class.first_func())