#Checking prime number

'''import math

def isPrime(n):
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n%2 == 0 or n%3==0:
        return False
    
    i = 5
    while i <= math.sqrt(n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        
        i += 6
        
    return True

if __name__ == '__main__':
    n = 7
    if(isPrime(n)):
        print('true')
    else:
        print('false')'''
        
        
#Sieve of Eratosthenes

'''def sieve(n):
    prime = [True] * (n+1)
    p = 2
    
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
        
    res = []
    for p in range(2,n+1):
        if prime[p]:
            res.append(p)
            
    return res

if __name__ == "__main__":
    n = 35
    res = sieve(n)
    for ele in res:
        print(ele, end = ' ')'''
        
#Binary Exponentiation

'''def powMod(x, n, M):
    res = 1
    
    while n >= 1:
        if n%2 == 1:
            res = (res*x) % M

            n -= 1
        else:
            x = (x*x)%M
            n //= 2
    return res

if __name__ == '__main__':
    x, n, M =3, 2, 4
    print(powMod(x, n, M))'''

#Even or odd 

#NAIVE approach 

'''def isEven(n):
    return n%2 == 0

if __name__ == '__main__':
    n = 15
    if isEven(15):
        print('true')
    else:
        print('false')'''
        

#Bitwise operation
'''def isEven(n):
    return n&1 == 0

if __name__ == '__main__':
    n = 15
    if isEven(n):
        print('true')
    else:
        print('False')'''


#Floor and Ceil integer Division
'''def floorDiv(a,b):
    return a//b

def ceilDiv(a,b):
    return -(-a//b)

def divFloorCeil(a,b):
    res = []
    res.append(floorDiv(a,b))
    res.append(ceilDiv(a,b))
    return res

if __name__ == '__main__':
    a, b = -7, 2
    res = divFloorCeil(a,b)
    print(res[0], res[1])'''
    
    
#Floor and Ceil integer (Built-in)
'''import math
def divFloorCeil(a,b):
    floor_val = math.floor(a/b)
    ceil_val = math.ceil(a/b)
    return [floor_val, ceil_val]

if __name__ == "__main__":
    a,b = -7, 2
    res = divFloorCeil(a,b)
    print(res[0], res[1])'''
    

#Decimal To binary

#Approach 1
'''def decToBinary(n):
    binArr = []
    
    while n>0:
        bit = n%2
        binArr.append(str(bit))
        n //= 2
    
    binArr.reverse()
    return "".join(binArr)

if __name__ == "__main__":
    n = 12
    print(decToBinary(n))'''
    

#Approach 2
'''def decToBinaryrec(n, binArr):
    if n == 0:
        return 
    decToBinaryrec(n//2, binArr)

    binArr.append(str(n%2))
    
def decToBinary(n):
    if n==0:
        return "0"
    binArr = []
    decToBinaryrec(n,binArr)
    return "".join(binArr)


if __name__ == '__main__':
    n = 12
    print(decToBinary(n))'''
    
    
#Approach 3 
'''def decToBinary(n):
    bin = ""

    while n > 0:
        bit = n & 1
        bin += str(bit)
        
        n = n>>1
    return bin[::-1]

if __name__ == '__main__':
    n = 12
    print(decToBinary(n))'''


#Approach 4
'''def decToBinary(n):
    return bin(n)[2::]

if __name__ == '__main__':
    n = 12
    print(decToBinary(n))'''
    

#Finding GCD/HCF

#Approach-1
'''def gcd(a,b):
    if a == 0 or b == 0:
        return max(a,b)
    
    result = min(a,b)
    
    while result > 0:
        if a%result == 0 and b%result == 0:
            break
        result -= 1
        
    return result

if __name__ == '__main__':
    a = 36
    b = 60
    print(gcd(a,b))'''
    

#Approach-2

'''def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return b
    
    if a==b:
        return a
    
    if a>b:
        return gcd(a - b,b)
    
    return gcd(a,b - a)

if __name__ == '__main__':
    a = 36
    b = 60
    print(gcd(a,b))'''
    

#Approach-3    

'''def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a 
    
    if a == b:
        return a 
    
    if a>b:
        if a%b == 0:
            return b
        return gcd(a-b, b)
    
    if b>a:
        if b%a == 0:
            return a 
        return gcd(a, b-a)

if __name__ == '__main__':
    a = 36
    b = 60
    print(gcd(a,b))'''
 
    
#Approach-4

'''def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

if __name__ == '__main__':
    a = 36
    b = 60
    print(gcd(a,b))'''


#Approach - 5
'''import math
def gcd(a, b):
    return math.gcd(a,b)

if __name__ == '__main__':
    a = 36
    b = 60
    print(gcd(a,b))'''

#LCM

#Approach 1

'''def lcm(a,b):
    g = max(a,b)
    s = min(a,b)
    
    for i in range(g, a*b+1, g):
        if i%s == 0:
            return i
    return a*b

if __name__ == "__main__":
    a = 10
    b = 5
    print(lcm(a,b))'''
    
    
#Approach 2

'''def gcd(a,b):
    return a if b==0 else gcd(b, a%b)

def lcm(a,b):
    return (a*b//gcd(a,b))

if __name__ == '__main__':
    a = 10
    b = 5
    print(lcm(a,b))'''
    
# Divisible by 13

#Approach 1
'''def divBy13(s):
    num = int(s)
    
    return num%13 == 0

if __name__ == '__main__':
    s = "2911285"
    isDivisible = divBy13(s)
    if isDivisible:
        print('True')
    else:
        print('False')'''
        
        
#Approach - 2
'''def divBy13(s):
    length = len(s)
    if length == 1 and s[0] == '0':
        return True
    
    if length%3 == 1:
        s += "00"
        length += 2
    elif length%3 == 2:
        s += "0"
        length += 1
    
    sum_ = 0
    p = 1
    
    i = length-1
    
    while i >= 0:
        group = 0
        group += int(s[i])
        i -= 1
        group += int(s[i])*10
        i -= 1
        group += int(s[i])*100
        i -= 1
        
        sum_ += group*p
        p *= -1  #reverses the sign of each group after an iteration. For example in 1st iteration p = 1 then in next p becomes -1 and group changes to -group
    
    sum_ = abs(sum_)
    return sum_%13 == 0

if __name__ == '__main__':
    s = "2911285"
    isDivisible = divBy13(s)
    
    if isDivisible:
        print('true')
    else:
        print('false')'''



#Approach 3
'''def divBy13(s):
    rem = 0
    
    for ch in s:
        rem = (rem*10 + int(ch))%13
    
    return rem == 0

if __name__ == '__main__':
    s = "2911285"
    if divBy13(s):
        print("true")
    else:
        print("false")'''



#Square root of integer

#Naive Approach 
'''def floorSqrt(n):
    res = 1
    while res*res <= n:
        res += 1
    return res - 1

if __name__ == '__main__':
    n = 11
    print(floorSqrt(n))'''
    

#Binary Search Approach 

'''def floorSqrt(n):
    
    lo = 1
    hi = 1
    res = 1
    
    while lo <= hi:
        mid = lo + (hi-lo)//2
        
        if mid*mid <= n:
            res = mid
            lo = mid + 1
        
        else:
            hi = mid + 1
    return res

if __name__ == '__main__':
    n = 11
    print(floorSqrt(n))'''
    

# Built in function
'''import math
def floorSqrt(n):
    res = int(math.sqrt(n))
    return res

if __name__ == '__main__':
    n = 11
    print(floorSqrt(n))'''
    


# Pocket Calculators 
'''import math
def floorSqrt(n):
    res = int(math.exp(0.5*math.log(n)))
    
    if (res + 1 )**2 <= n:
        res += 1
    return res

if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))'''
    


#All Divisors of a number

#Naive Approach 

'''def getDivisors(n):
    divisors =[]
    
    for i in range(1, n+1):
        if n%i == 0 :
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    number = 10
    divisors = getDivisors(number)
    for div in divisors:
        print(div, end = ' ')'''
        

#Expected Approach - Finding factors in pairs
import math

def getDivisors(n):
    res = []
    large = []
    num = 1

    while num * num <= n:
        if n % num == 0:
            if num == n // num:
                res.append(num)
            else:
                res.append(num)
                large.append(n // num)
        num += 1

    # add large divisors in reverse
    for i in range(len(large) - 1, -1, -1):
        res.append(large[i])

    return res

if __name__ == "__main__":
    number = 10
    divisors = getDivisors(number)

    for div in divisors:
        print(div, end=" ")
        