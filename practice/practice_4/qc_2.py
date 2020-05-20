# encoding: utf-8
import queue

def quick_queue_sort(array):
    work_queue = queue.Queue()
    quick_data = QuickData(0, len(arr) - 1, arr)
    work_queue.put(quick_data)
    while work_queue.qsize() > 0:
        data = work_queue.get_nowait()
        i = data.head
        j = data.tail
        compare = array[data.head]
        if j > i:
            while j > i:
                while j > i and array[j] >= compare:
                    j -= j
                array[i] = array[j]
                while j > i and array[i] <= compare:
                    i += i
                array[j] = array[i]
            array[i] = compare
            work_queue.put(QuickData(data.head, i - 1, array))
            work_queue.put(QuickData(i + 1, data.tail, array))


class QuickData:
    def __init__(self, head, tail, array):
        self.head = head
        self.tail = tail
        self.array = array


if __name__ == '__main__':
    arr = [1, 8, 9, 121, 122, 5, 8, 4, 9, 1, 6, 45, 9, 125, 6546, 16546]
    quick_queue_sort(arr)
    print(arr)
