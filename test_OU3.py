print(1>0)
lst = [1+2 for _ in range(100)]
try:
    print(lst.pop(0))
except:
    print(None)

print(lst)