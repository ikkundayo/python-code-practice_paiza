# フィボナッチ数列生成関数
def fibonacci_list(n):
    fib = [1, 1]
    if n == 1:
        fib = [1] 
    else:
        for k in range(2, n):
            fib.append(fib[k-1]+fib[k-2])
    return fib

# 10番目のフィボナッチ数を生成
fib = fibonacci_list(10)

print(fib[8])


# トリボナッチ数列生成関数
def tribonacci_list(n, t0, t1, t2):
    tri = [t0, t1, t2]
    if n == 1:
        tri = [t0]
    elif n == 2:
        tri = [t0, t1]
    else:
        for k in range(3, n):
            tri.append(tri[k-1]+tri[k-2]+tri[k-3])
    return tri

# 1,1,2から始まる10項のトリボナッチ数列を生成
tri = tribonacci_list(32, 1, 0, 5)

print(tri)

# 100までのピタゴラス数
count=0
for c in range(1,100):
   for b in range(1,c):
       for a in range(1,b):
           if a*a+b*b==c*c:
               check=1
               for i in range(2,a):
                   if a%i==0 and b%i==0 and c%i==0:
                       check=0
               if check==1:
                   count=count+1
                   print(count,'   ',a,b,c)
print('fin')