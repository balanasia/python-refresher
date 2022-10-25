# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements and repeats the process until q value remains
#
# reduce(function, iterable)
import functools 


# letters = list("HELLO")
# word = functools.reduce(lambda x, y:x+y ,letters)
# print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y:x*y, factorial)
print(result)