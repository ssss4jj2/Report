# Testing CppExt_Array and MyPyPackage (1)
import sys
sys.path.append("C:/Users/승준/Source/Repos")
import PyCppExt_Array as CppExt

sys.path.append("C:/")
from MyPyPackage import myModules
from array import *

import numpy as np
import random
import time

("CppExt.probe() : ", CppExt.probe("test command"))

while True:
    arr_Size = int(input("\ninput array size (0 to quit) = "))
    if arr_Size <= 0:
        break
    
    A = np.arange(arr_Size)
    CppExt.ShuffleArray(A)
    myModules.MyArray.printArraySample(A, arr_Size, 10, 2)
    print("Invoke PyCppExt.quickSort(A) ...")
    
    t_before = time.time()
    CppExt.quickSort(A)
    t_after = time.time()
    t_elapse_ms = (t_after - t_before) * 1000
    print("CppExt.sort() for array of {} integers took {} [msec]".format(arr_Size, t_elapse_ms))
    
    print("After sorting :")
    myModules.MyArray.printArraySample(A, arr_Size, 10, 2)
    
    print("\nShuffling Array :")
    CppExt.shuffleArray(A)
    myModules.MyArray.printArraySample(A, arr_Size, 10, 2)
    print("Invoke myModules.MySort.quickSort(A) ...")
    
    t_before = time.time()
    myModules.MySortings.quickSort(A)
    t_after = time.time()
    t_elapse_ms = (t_after - t_before) * 1000
    print("myModules.MySort.quickSort() for array of {} integers took {} [msec]".format(arr_Size, t_elapse_ms)) 
    print("After sorting :")
    
    myModules.MyArray.printArraySample(A, arr_Size, 10, 2)
    print("\nShuffling Array :")
    CppExt.shuffleArray(A)
    myModules.MyArray.printArraySample(A, arr_Size, 10, 2)
    print("Invoke myModules.MySort.mergeSort(A) ...")
    
    t_before = time.time()
    myModules.MySortings.mergeSort(A)
    t_after = time.time()
    t_elapse_ms = (t_after - t_before) * 1000
    print("myModules.MySort.mergeSort() for array of {} integers took {} [msec]".format(arr_Size, t_elapse_ms)) 
    print("After sorting :")
    myModules.MyArray.printArraySample(A, arr_Size, 10, 2)