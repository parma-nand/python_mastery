# def train(epoch=10):
#     print(epoch)
# train(epoch=20)

def train(*,epochs=10, lr=0.01): #Only Keywrod paramter allowed that means *
    print(epochs, lr)

train(epochs=10, lr=0.01)

def add(*args):
    
    print (sum(args))
add(1,2,3,4)

def func(*args,**kwargs):
    print(args)
    print(kwargs)
func(1,2,97,89,a=20,b=30,c=90)

square=lambda x: x*x
print(square(7))