def duplicateChar(str):
	count = 0
	prev_char = ''
	i=0
	while(str[i]!=''):
		if prev_char == str[i]:
			count += 1
			print('Repeated character is:',prev_char)
		prev_char = str[i]
		i +=1
	return count
duplicateChar('aahgfeecc')
