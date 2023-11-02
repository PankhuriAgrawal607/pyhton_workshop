#object are real life intities,it is a instance of a class
# _init_ method --- specific instance
# self -------------- for 

class bank:
    def __init__(self,bank_acc,balance):
        self._bank_acc=bank_acc
        self.__balance=balance
        
    def get_balance(self):
        return self.__balance        
    
# encapsulation
# private-----------  __variable
# protected---------  _variable    
    
    
b1=bank(123456789,20000)
print(b1.get_balance())  #---accessing a private member
print(b1._bank_acc)      #---accessing a protected member