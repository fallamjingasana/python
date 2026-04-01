class myclass:
    _privateVar = 27;
    def __privmeth(self):
        print("im inside my class")
    def hello(self):
        print("private variable value:", myclass.__privateVar)
foo = myclass()
foo.hello()
foo.__privmeth