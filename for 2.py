name=input("이름:")

print("-*"*30)
print("\t\t%s's 구구단 PROGRAM 2"%(name))
print("-*"*30)


for i in range(1,10):
    print("---------%d단----------"%(i))
    
    for j in range(1,10):
        
        print("%d x %d = %d"%(i,j,i*j))
    print("\n")
        
