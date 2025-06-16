def recursionfactorial(n):
    if(n==1 or n==0):
        return 1;
    return n*recursionfactorial(n-1)
def dpfactorial(n):
    dp=[1]*(n+1)
    for i in range(2,n+1):
        dp[i]=i*dp[i-1]
    return dp[n]
f=int(input("Enter the number:")) 
a=recursionfactorial(f)
a=dpfactorial(f)
print(a)