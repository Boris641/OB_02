class User1():
    def __init__(self, ND, name):
        self._protected = ND
        self._protected = name
        self.users = {}
    def nomer(self):
        print(f"{self._protected.ND} 12345")
    def doc(self):
        print(f"{self._protected.name} Иван")
    def get_protected(self):
        return self._protected
    def set_protected(self, name):
        self._protected = name


class Admin():
    pass












