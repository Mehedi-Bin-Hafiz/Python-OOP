#If subclass (child class) has the same method as declared in the parent class, it is known as method overriding
# python support it

class Father():

    def mobile(self):
        print('samsung')

class Me(Father):

    def mobile(self):
        print('HUAWEI')

me = Me()
me.mobile() ## it is called method overriding
