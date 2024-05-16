class BubbleSort():
    ''' Algorithm of bubble sort '''
    def bubble_sort(self, arr):
        ''' Method bubble sort '''
        lenght_arr = len(arr)
        for all_nums in range(lenght_arr-1):
            for num in range(lenght_arr-all_nums-1):
                if arr[num] > arr[num+1]:
                    arr[num], arr[num+1] = arr[num+1], arr[num]
        return arr


array = [1, 9, 5, 4, 2, 7]
test = BubbleSort()
print(test.bubble_sort(array))
