


class SortableList(list):
    def __init__(self, iterable):
        super().__init__(iterable)


    def insertion_sort(self):
        i = 1
        while i < len(self):
            j = i
            while j > 0 and self[j-1] > self[j]:
                tmp = self[j]
                self[j] = self[j-1]
                self[j-1] = tmp
                j -= 1
            i += 1


    def selection_sort(self):
        for i in range(len(self)):
            i_smallest = i
            for j in range(i+1, len(self)):
                if self[j] < self[i_smallest]:
                    i_smallest = j
            
            tmp = self[i]
            self[i] = self[i_smallest] 
            self[i_smallest] = tmp


    def merge_sort():
        pass

    def heap_sort():
        pass

    def quick_sort():
        pass

    def bubble_sort():
        pass


if __name__ == '__main__':
    lst = SortableList([3,2,4,1,6,5])

    lst.selection_sort()

    print(lst)