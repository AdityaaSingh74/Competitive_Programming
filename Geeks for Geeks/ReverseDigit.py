#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		n1 = str(n)
		n1 = n1[::-1]
		n = int(n1)
		return n