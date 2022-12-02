
class Recursion:

    def __init__(self, value: int = 100):
        self.value = value

    def iterativeSum(self) -> int:
        sum: int = 0
        for i in range(self.value + 1):
            sum += i
        return sum
    
    
    def recursiveSum(self, num: int = None) -> int:
        if not num and num != None:
            return 0
        if num is None:
            num = self.value
        return num + self.recursiveSum(num - 1)


if __name__ == "__main__":

    recursion = Recursion(17)

    iterativeSum = recursion.iterativeSum()
    recursiveSum = recursion.recursiveSum()

    print('Iterative Sum = ', iterativeSum)
    print('Recursive Sum = ', recursiveSum)
