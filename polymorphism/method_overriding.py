#If subclass (child class) has the same method as declared in the parent class, it is known as method overriding
# python support it

class Father():
    """ This is my father"""

    def mobile(self):
        print('samsung')

class Me(Father):
    """ This is me"""

    def mobile(self):
        print('HUAWEI')

me = Me()
me.mobile() ## it is called method overriding
