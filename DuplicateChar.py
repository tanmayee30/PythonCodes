def duplicateChar(str_):
	count = 0
	prev_char = ''
	i=0
	length = len(str_)
	for i in range(length):
		if prev_char == str_[i]:
			count += 1
			print('Repeated character is:',prev_char)
		prev_char = str_[i]
		i +=1
	return count
duplicateChar('aahgfeecc')
