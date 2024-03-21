class get_dictionary:
    
    def __int__(self,a,b):
        self.a = a
        self.b = b 
    
    def get_output(self,a,b):
        result_dict = dict()
        for i in range(a,b+1):
            result_dict[i] = i**2
        return result_dict    

a = int(input())
b = int(input())

Dictionary = get_dictionary()    
print(Dictionary.get_output(a,b))    
