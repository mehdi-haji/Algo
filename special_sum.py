
class SpecialSum:
    largestNumberOfOddNumbers = 0
    listWithLargestNumberOfOddNumbers = None

    def __init__(self):
        self.largestNumberOfOddNumbers = 0
        self.listWithLargestNumberOfOddNumbers = list()

    def sumWithLargestNumberOfOddNumbers(self, N):
        self.sumWithLargestNumberOfOddNumbers_core(N, N, [])
        #print(self.listWithLargestNumberOfOddNumbers)
        return self.largestNumberOfOddNumbers

    def sumWithLargestNumberOfOddNumbers_core(self, N, n, L):
        if n < 0:
            return

        if n == 0:
            numOfOddNumbers = len([x for x in L if x%2 == 1])
            if numOfOddNumbers > self.largestNumberOfOddNumbers:
                self.largestNumberOfOddNumbers = numOfOddNumbers
                self.listWithLargestNumberOfOddNumbers = list(L)
            return

        startNumber = 1
        if len(L) > 0:
            startNumber = L[-1] + 1

        if startNumber > n:
            return

        for i in range(startNumber, N):
            L.append(i)
            self.sumWithLargestNumberOfOddNumbers_core(N, n - i, L)
            L.pop()


def main():
    specialSum = SpecialSum()
    res = specialSum.sumWithLargestNumberOfOddNumbers(91)
    print(res)
    
main()
