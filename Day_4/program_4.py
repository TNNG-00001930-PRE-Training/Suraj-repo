class stringMethods:
    def __init__(self):
        self.str1 = ''
    def get_string(self):
        self.str1 = input()
    def print_string(self):
        print(self.str1.upper())
def test_cases():
    test = stringMethods()
    test.get_string()
    test.print_string()
test_cases()    