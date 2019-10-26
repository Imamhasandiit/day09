class calculator:
    def __init__(self) :
       #print("This is a constructor")
       pass

    def show(self,s):
        return "hello" + s

   
    def add(self,x,y):
        return (x+y)

    def sub(self,x,y):
        return (x-y)

    def mult(self,x,y):
        return (x*y)

    def div(self,x,y):
        return (x/y)
c= calculator()
print (c.add(5,10))
#print (c.sub(5,10))
#print (c.mult(5,10))
#print (c.sub(5,10))