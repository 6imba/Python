# # Accessing array using While_loop :
# Here comess the concept of accumulator_variable

# # 3.9
# # Without Index : Using array_identifier
from array import array
numbers = array('i',[1,2,3,4,5,6,7,8,9,0])
arr_len = len(numbers)

accum = 0
while accum < arr_len:
    print(numbers[accum])
    accum += 1

# Here, accum is accumulator_variable as it keeps changing as iteration keeps on going in loop


