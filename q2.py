'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function
definition should look like question2(a), and return a string.
'''

'''
dynamic programming solution, O(N^2) time and O(1) space.
	expand around center, there are 2N-1 such centers	
'''

def question2(a):

	def check(s, c1, c2):
		l = c1
		r = c2
		n = len(s)
		while ((l >= 0)  & (r <= n-1)):
			#print s, s[l], s[r], l, r 
			if (s[l] == s[r]):
				l-=1
				r+=1
				#print 'l and r', l, r
			else:
				break
		#print 'palindrom', s[l+1:r]
		return s[l+1:r]

	n = len(a)
	if (n==0): return "No string provided"
	longest = a[0]
	for i in range(0, n-1):
		p1 = check(a, i, i)
		#print 'p1 is', p1, 'i is', i
		if (len(p1) > len(longest)):  # this is for the strings with odd letters
			longest = p1
		#	print 'p1', p1
		p2 = check(a, i, i+1)
		#print 'p2', p2, 'i is', i
		if (len(p2) > len(longest)):  # when the number is letter is even
			longest = p2
			#print 'p2', p2
	return longest


print question2('zabcy')
print question2('qabbap')
print question2('')
