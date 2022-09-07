
def square(a): #square function defined
    ans = a * a #ans is local variable that hold square answer
    return ans

def add(a,b,c): #here a,b,c is a parameter of function
    x = square(a) #square function call
    y = square(b)
    z = square(c)
    return x+y+z
    #here x,y,z is a local variable of function_add()

print(square(7))
ans = add(2,3,5) # ans is global_variable # add()_function call
print(ans)





