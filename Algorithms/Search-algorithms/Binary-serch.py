class BinarySearch():
    ''' Algorithm of binary search '''
    def binary_search(self, array, find):
        ''' Method for search '''
        low = 0
        high = len(array)-1
        while low <= high:
            mid = (low + high)//2
            guess = array[mid]
            if guess == find:
                return mid
            if guess > find:
                high = mid - 1
            else:
                low = mid + 1
        return mid

array = [1, 3, 5, 7, 9, 12, 13, 15, 19, 22]
test = BinarySearch()
print(test.binary_search(array, 13))
