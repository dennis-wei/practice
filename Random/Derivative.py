import numpy as numpy

class Node(object):
	"""
	Nodes for symolic tree
	"""

	def __init__(self, v, l=None, r=None):
		self.value = v
		self.left = l
		self.right = r

	def printTree(self):
		if self.left != None:
			(self.left).printTree()
		print self.value
		if self.right != None:
			(self.right).printTree()

def tokenize(exp):

	operators = {"+", "-", "*", "/", "^"}

	for op in operators:
		if op in exp:
			subexp = exp.rsplit(op, 1)
			print subexp
			newNode = Node(op, tokenize(subexp[0]), tokenize(subexp[1]))
			return newNode

	newNode = Node(atoi(exp))
	return newNode

def derivative(head):

	operators = {"+", "-", "*", "/", "^"}

	if head.left:
		derivative(head.left)
	if head.right: 
		derivative(head.right)

	if head.value in operators:
		if head.value == "^":
			head

expression = "3*x^3+2*x"
head = tokenize(expression)
head.printTree()