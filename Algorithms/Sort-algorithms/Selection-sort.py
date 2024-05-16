class SelectionSort():
    ''' Algorithm of selection sort '''
    def find_smallest(self, array):
        ''' This method find smallest element in array'''
        smallest = array[0]
        smallest_index = 0
        for i in range (1,len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        return smallest_index


    def selection_sort(self, array):
        ''' This method append return sorted array'''
        new_array = []
        for i in range(len(array)):
            smallest = self.find_smallest(array)
            new_array.append(array.pop(smallest))
        return new_array


array = [12, 10, 5, 7, 3, 6, 1, 90]
test = SelectionSort()
print(test.selection_sort(array))
