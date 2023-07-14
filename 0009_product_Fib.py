def productFib(prod):
    fn = 0
    fn1 = 1
    for i in range(prod+1):
        print(fn, fn1)
        if fn*fn1 == prod:
            return [fn, fn1, True]
        elif fn*fn1 > prod:
            return [fn,fn1,False]
        a = fn1
        fn1 = fn+fn1
        fn = a
print(productFib(0))


#0,1,1,2,3,5,8,13,21,34,55,89,144,233
