
class PyCharm:

    def execute(self):
        print('run')
        print('spell check')

class MyEditor:

    def execute(self):
        print('run')
        print('check validation')
        print('spell check')
class IDE:

    def code(self, obj):
        obj.execute() # if there is object has method execute that it , it never mind which class object it is
        # this concept is known as duck typing.

obj1 = MyEditor()
obj2 = PyCharm()

obj3 = IDE()

print('my editor versions:')
my_editor = obj3.code(obj1)
print('pycharm  versions:',)
py_charm =obj3.code(obj2)






