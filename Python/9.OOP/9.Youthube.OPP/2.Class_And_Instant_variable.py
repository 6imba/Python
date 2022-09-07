# # 1
# class Person :
#     def __init__(self,i_d,name,year):#parameters
#         self.i_d=i_d
#         self.name=name
#         self.year=year
#         # instant_variable {self.i_d,self.name,self.year}
#     def show(self):
#         print(' Id {} is {}.Fall {}'.format(self.i_d,self.name,self.year))

# person1=Person(1,'Aliya',2018)#arguments
# person2=Person(2,'Kunka',2018)

# person1.show()
# person2.show()







# # 2
# class Person1 :
#     i_d=0
#     year=2018
#     #class_variable {i_d,year}

#     def __init__(self,name):
#         self.name=name # instant_variable {self.name}
#         Person1.i_d +=1 #class_variable {i_d,year}

#     def show(self):
#         print(' Id {} is {}.Fall {}'.format(Person1.i_d,self.name,Person1.year)) # calling instant_variable {self.name} and class_variable {Person1.i_d,Person1.year}

# per1=Person1('Aliya')
# per1.show()

# per2=Person1('Kunka')
# per2.show()

# per3=Person1('Hema')
# per3.show()





# # 3
# class Person2 :
#     i_d=0
#     year=2018
#     #class_variable {i_d,year}

#     def __init__(self,name):
#         self.name=name # instant_variable {self.name}
#         Person2.i_d +=1 #class_variable {i_d,year}

#     def show2(self):
#         print(' Id {} is {}.Fall {}'.format(Person2.i_d,self.name,Person2.year))

# per1_2=Person2('Aliya')
# per1_2.show2()

# print(per1_2.__dict__) # shows what an instant holds
# print(Person2.__dict__)  # shows what an class holds





# # 4
# class Person3 :
#     i_d=0
#     year=2018  
    
#     def __init__(self,name):
#         self.name=name # instant_variable {self.name}
#         Person3.i_d +=1 #class_variable {i_d,year}
        

#     def show3(self): 
#         print(' Id {} is {}.Fall {}'.format(self.i_d,self.name,self.year)) # self looks for variable(i_d,year) if present in that particular_instant and if not then it will futher looks toward the class of that particular_instant
        
# per1_2=Person3('Aliya')
# per1_2.show3()

# per1_2=Person3('SimbA')
# per1_2.show3()




# # 5
# class Person4 :
#     i_d=0
#     year=2018

#     def __init__(self,name):
#         self.name=name
#         Person4.i_d +=1

#     def show4(self):
#         print(' Id {} is {}.Fall {}'.format(Person4.i_d,self.name,Person4.year))

# per1=Person4('Aliya')
# per1.show4()

# per2=Person4('Kunka')
# per2.show4()

# per3=Person4('Hema')
# per3.show4()






# # 6
# class Person5 :
#     i_d=0
#     year=2018  
    
#     def __init__(self,name):
#         self.name=name 
#         Person5.i_d +=1 # id increment
#         print(Person5.i_d)
        
#     def show5(self): 
#         print(' Id {} is {}.Fall {}'.format(Person5.i_d,self.name,Person5.year))
        
# per1=Person5('Aliya')
# per2=Person5('Kunka')
# per3=Person5('Hema')

# per1.show5()
# per2.show5()
# per3.show5()





# # 7
# class Person6 :
#     i_d=1
#     year=2018

#     def __init__(self,name):
#         self.name=name
#         self.show6() # call show_method for current instant # calling method inside method of same class
#         Person6.i_d +=1 # id increment
#         print('Id increment : ',Person6.i_d)

#     def show6(self):
#         print('Id {} is {}.Fall {}'.format(Person6.i_d,self.name,Person6.year))

# per1=Person6('Aliya')
# per2=Person6('Kunka')
# per3=Person6('Hema')

