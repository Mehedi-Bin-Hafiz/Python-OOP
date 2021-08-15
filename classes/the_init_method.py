

class Computer():

    def __init__(self,cpu,ram): #initialize the variable # in c++,java it is constructor
        # print('funciton int')
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config is ', self.cpu, self.ram)
        # here cpu and ram is not local variable it is attribute because it belongs to self(com1) object.
        # so we need to write self.cpu, and self.ram to access it.


com1 = Computer('i5','16') # when instantiation is happened __init__ is automatically callled
# so in declare init with three parameter but we passes 2 parameter. the reason is
# object com1 is automatically passes to self


com1.config()




