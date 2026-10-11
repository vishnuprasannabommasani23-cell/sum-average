nums=[34,40,50,90,70]
total=sum(nums)
average=total/len(nums)
even=[]
odd=[]
print(f"average of given list of numders is {average}")
for i in range(len(nums)):
    if nums[i]%2==0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
print(f"Even numders from the list are{even}")
print(f"Odd numder from the list are{odd}")

        
