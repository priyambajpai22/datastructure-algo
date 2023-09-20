arr=[10,20,30,40,50]
target=50

def find_element(arr,target,index=0):
	if len(arr)==1:
		return index

	mid_ind=len(arr)//2
	mid_val=arr[mid_ind]
	if mid_val<target:
		index=index+mid_ind+1
		return find_element(arr[mid_ind+1:],target,index)

	if mid_val==target:
		index=index+mid_ind
		return index


	if mid_val>target:
		return find_element(arr[:mid_ind],target,index)


print(find_element(arr,30))
