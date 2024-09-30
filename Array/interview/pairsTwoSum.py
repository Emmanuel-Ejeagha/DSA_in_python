# Leetcode Pairs two sum

def findpairs(nums, target):
    for x in range(len(nums)):
        for y in  range(x+1, len(nums)):
            if nums[x] == nums[y]:
                continue
            if nums[x] + nums[y] == target:
                print(f"{mylist}\n[{x},{y}]")
                print(f"Because nums[{x}] + nums[{y}] == {target}, we return [{x}, {y}].")

mylist = [2, 3,4,5,9]
findpairs(mylist, 6)