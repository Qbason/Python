#string formating

nums = [4,5,6]

#msg = "Numbers: {2} {1} {2}".format(nums[0],nums[1],nums[2])
#msg = "Numbers: {} {} {}".format(nums[0],nums[1],nums[2])
msg = "Numbers: {x} {y}".format(x=5, y=12)

print(msg)