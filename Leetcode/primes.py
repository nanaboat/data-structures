class Prime:
    def isPrime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    
    def printPrimes(self, low, high):
        if low < 0 and high < 0:
            return
        if low > high:
            print(False)
            return
        results = []
        for num in range(low, high + 1):
            if num < 0:
                continue
            if self.isPrime(num):
                results.append(num)
        if results:
            print(True)
            for val in results:
                print(val)
        


if __name__ == "__main__":
    Prime().printPrimes(-5, -10)