data=[5,7,7,8,8,10]
target=7

def check_occurance(nums,target,mid,ocurance):
    if nums[mid]==target:
        if mid<len(nums)-1 and nums[mid+1]==target and ocurance=="last":
            return "right"
        elif mid>0 and nums[mid-1]==target and ocurance=="first":
            return "left"
        return "found"
    elif nums[mid]<target:
        return "left"
    else:
        return "right"

class Solution():
    def searchRange(self, nums, target):
        def first_occurance(nums,target):
            low = 0
            high= len(nums)-1
            while low <= high:
                mid = (low + high)//2
                result = check_occurance(nums,target,mid,"first")
                if result=="found":
                    return mid
                elif result=="left":
                    high=mid-1
                else:
                    low=mid+1
            return -1
        def last_occurance(nums,target):
            low = 0
            high= len(nums)-1
            while low <= high:
                mid = (low + high)//2
                result = check_occurance(nums,target,mid,"last")
                if result=="found":
                    return mid
                elif result=="left":
                    high=mid-1
                else:
                    low=mid+1
            return -1
        return [first_occurance(nums,target),last_occurance(nums,target)]

k=Solution()
print(k.searchRange(data,target))