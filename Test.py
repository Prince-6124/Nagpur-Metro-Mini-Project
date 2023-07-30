from datetime import time

t1 = time(6,40,00)
t2 = time(6,43,19)

print("{} > {} -> {}".format(t1,t2,t1>t2))
print("{} < {} -> {}".format(t1,t2,t1<t2))
print("{} == {} -> {}".format(t1,t2,t1==t2))
print("{} != {} -> {}".format(t1,t2,t1!=t2))
# print("{} + {} -> {}".format(t1,t2,t1+t2))
# print("{} - {} -> {}".format(t1,t2,t1-t2))
 
# ! Important for the project

#!###############################

tm = "6:10:45"
t = list(map(int, tm.split(':')))
print(time(t[0],t[1],t[2]))

#!###############################
lf = []
for i in range(1,51):
    lf.append(i)

print(lf)

line = 1
l = []
while True:
    if lf == []: break
    x = lf.pop(0)
    l.append(x)
    if line == 10:
        print(l)
        print("lf =",lf)
        line = 1
        l.clear()
        continue
    line += 1




