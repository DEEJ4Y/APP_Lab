
class Dept():
    name = ""

    def __init__(self, newName=None):
        self.name = "SCO"
        if newName is not None:
            self.name = newName


d1 = Dept()
d2 = Dept("Not SCO")

print(d1.name)
print(d2.name)
