stack = []
for i in range(5):
    stack.append(i)

print("stack =>", stack)
numAtTop = stack.pop()
print("stack.pop() => ",numAtTop)

print("current stack =>", stack)
# Get The Number of the top without removing it 
print("stack.peep =>", stack[-1])
# Current Stack
print("Current stack => ", stack)
