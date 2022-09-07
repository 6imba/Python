# # 1
# class Parent(object):
#   pass

# obj_parent = Parent()
# print(obj_parent)



# # 2
# class Parent(object):
#   parent_class_var = 'Parent'

# obj_parent = Parent()
# print(obj_parent.parent_class_var)


# # 3
# class Parent(object):
#   parent_class_var = 'Parent'
# class Child(Parent):
#   child_class_var = 'Child'

# obj_child = Child()
# print(obj_child.child_class_var)
# print(obj_child.parent_class_var)


# # 4
# class Parent(object):
#   parent_class_var = 'Parent'

# class Child(Parent):
#   child_class_var = 'Child'

#   def par(self):
#     # print(parent_class_var)
#     # print(self.parent_class_var)
#     # print(Parent.parent_class_var)
      # print(super().parent_class_var)
#     pass

# obj_child = Child()
# obj_child.par()




# 5

global_var = "Global"
class Parent(object):
  parent_class_var = 'Parent'

class Child(Parent):
  child_class_var = 'Child'

  def par(self):
    print(global_var)

obj_child = Child()
obj_child.par()




# global variable
# class variable (parent or chhild)
# local variable

# object of child_class can call members of parent_class, outside the classes
# but in-built super() function is needed at the time when we call members of parent_class, inside the child_classes