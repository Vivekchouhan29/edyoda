x = int(input("enter value of x;"))
n = int(input("enter value of n :"))


class power:
    
    def nth_powr(self,x,n):
        return x**n

obj = power()
data = obj.nth_powr(x,n)
print(data)
