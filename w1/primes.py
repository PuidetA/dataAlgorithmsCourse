def primes(N):
    if N<2:
        return 0
    elif N==2:
        return 1
    
    primeCount=0
    for i in range(2,N+1):
        prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=False
                break
        if prime==True:
            primeCount+=1
    return primeCount

if __name__ == "__main__":
    print(primes(7))
    print(primes(15))
    print(primes(50))