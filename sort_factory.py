from abc import ABC, abstractmethod
import utils

class SortFactory:
    registry={}
    @classmethod
    def register(cls,name):
        def inner_wrapper(wrapped_class):
            cls.registry[name] = wrapped_class
            return wrapped_class
        return inner_wrapper
    
    @classmethod
    def get_handler(cls,name):
        return cls.registry[name]

class Sort(ABC):
    @abstractmethod
    def sort(arr):
        pass

@SortFactory.register('insertion')
class InsertionSort(Sort):
    def sort(arr):
        return utils.insertion_sort(arr)

@SortFactory.register('merge')
class MergeSort(Sort):
    def sort(arr):
        return utils.merge_sort(arr)

@SortFactory.register('quick')
class QuickSort(Sort):
    def sort(arr):
        return utils.quick_sort(arr)

@SortFactory.register('heap')
class HeapSort(Sort):
    def sort(arr):
        return utils.heap_sort(arr)