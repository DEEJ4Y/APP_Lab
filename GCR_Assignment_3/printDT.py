

class PrintDT():

    def python_data_tuple(self, tpl: tuple):
        print(tpl)

    def python_data_list(self, lst: list):
        print(lst)

    def python_data_string(self, strn: str):
        print(strn)


prnter = PrintDT()
arr = [1, 2, 3, 4]
t = (1, 2, 3, 4)
prnter.python_data_list(arr)
prnter.python_data_tuple(t)
prnter.python_data_string("aksdjfasjdhf")
