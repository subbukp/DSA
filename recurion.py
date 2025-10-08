from typing import List
class recur:
    def countdown(self,n: int):
        if n ==1:
            print(n)
            return n
        print(n)
        countdown(n-1)

    def count(self,n:int)-> int:
        if n == 1:
            return n
        return n + self.count(n-1)
    
    def fib(self, n):
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    def fact(self,n):
        if n==1:
            return 1
        return n*self.fact(n-1)

a = recur()
print(a.fact(6))