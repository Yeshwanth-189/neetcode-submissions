class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        n=len(self.arr)
        if n % 2 != 0:
            mid = n // 2
            return float(self.arr[mid])

        left_mid = n // 2 - 1
        right_mid = n // 2
        return (self.arr[left_mid] + self.arr[right_mid]) / 2  
        