def permutation(string):
	print(string)
	if len(string)<2:
		return [string]

	permute=[]

	for x in range(len(string)):
		fix=string[x]
		rest=permutation(string[:x]+string[x+1:])
		for x in rest:
			permute.append(fix+x)

	return permute




print(permutation('abc'))