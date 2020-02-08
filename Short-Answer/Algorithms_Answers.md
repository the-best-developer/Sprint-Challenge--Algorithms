#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n!) because the loop conditions directly relate to the input value, the larger the value, the longer the loop runs.
val * val * val exponetially increases runtime.


b) O(n^c) because for each loop, another loop is done every iteration, multiplying runtime by ^c.


c) O(1) because no extra work is being done for each recursion, it is simply multiplying input by 2

## Exercise II


The best solution would be a binary search. Take the number of floors and find the middle. Drop an egg at that height and determine if it broke or not. If not, split the number of floors again.

floors = 12

current_length = length(floors) / 2

if drop_egg(current_length) == cracked:
    current_length = current_length / 2
else
    print('Egg is safe)