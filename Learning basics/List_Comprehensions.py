#power of
cubes= [i**3 for i in range(5)]

print(cubes)

# nums = [i*2 for i in range(10)]
# print(nums)


evens = [i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

""" error MemoryError """
#even = [i**2 for i in range(10**100)]

#print(even)