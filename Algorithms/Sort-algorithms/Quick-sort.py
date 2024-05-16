import random


class QuickSort():
    ''' Algorithm of quick sort'''
    def quick_sort(self, arr):
        ''' Method quick sort'''
        if len(arr) <= 1:
            return arr
        else:
            random_avg = arr[random.randint(0, len(arr)-1)]
            low = [i for i in arr if i < random_avg]
            high = [i for i in arr if i > random_avg]
            equivalent = [i for i in arr if i == random_avg]
            return self.quick_sort(low) + equivalent + self.quick_sort(high)


array = [1, 3, 5, 10, 4, 11, 2, 7, 9, 8, 6]
test = QuickSort()
print(test.quick_sort(array))
