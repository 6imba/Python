# employee = []
# file = open('./demo.txt')
# for line in file:
#     # print(line)
#     # print(line.strip())
#     # print(line.strip().split())
#     # print(line.strip().split(","))
#     name = line.strip().split(",")[0]
#     # print(name)
#     employee.append(name)
# print(employee)


# employee = []
# file = open('./demo.txt')
# for iteration,line in enumerate(file):
#     # print(iteration)
#     if iteration==0:continue
#     # print(line)
#     # print(line.strip())
#     # print(line.strip().split())
#     # print(line.strip().split(","))
#     name = line.strip().split(",")[0]
#     # print(name)
#     employee.append(name)
# print(employee)


employee = []
file = open('./demo.csv')
for iteration,line in enumerate(file):
    if iteration==0:continue
    name = line.strip().split(",")[0]
    employee.append(name)
print(employee)




