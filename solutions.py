"""
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

"""

def question1(s, t):
    if (len(t)==0): return "Please input two strings"
    len_t = len(t)
    len_s = len(s)
    list_t = list(t)
    list_t.sort()     # Quick sort O(n*log(n))

    for i in range(len_s - len_t + 1):
        if check_anagram(s[i: i+len_t], list_t):
            return True
    return False

def check_anagram(part_s, list_t):
    part_s = list(part_s)
    part_s.sort()   
    return part_s == list_t


print question1("udacity", "ud")
print question1("udacity", "")
print question1("udacity", "lp")

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
"""
Question 3

Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)

"""


# A utility function to find set of an element i
# (uses path compression technique)
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that does union of two sets of x and y
# (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    #If ranks are same, then make one as root and increment
    # its rank by one
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

# The main function to construct MST using Kruskal's algorithm
def KruskalMST(graph, V, inv_dict):

    result =[] #This will store the resultant MST

    i = 0 # An index variable, used for sorted edges
    e = 0 # An index variable, used for result[]

    #Step 1:  Sort all the edges in non-decreasing order of their
    # weight.  If we are not allowed to change the given graph, we
    # can create a copy of graph
    graph =  sorted(graph,key=lambda item: item[2])
    #print self.graph

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V -1 :

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        # If including this edge does't cause cycle, include it
        # in result and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)
        # Else discard the edge

    # print the contents of result[] to display the built MST
    #print "Following are the edges in the constructed MST"
    p1 = []
    final_result = {}
    for u,v,weight  in result:
        p1 = [(inv_dict[v],weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)
        #print str(u) + " -- " + str(v) + " == " + str(weight)
        #print ("%c -- %c == %d" % (inv_dict[u],inv_dict[v],weight))

    return final_result

def question3(s1):
    n = len(s1)
    tmp_dict = {}
    inv_dict = {}
    count = 0
    u,v,w = None, None, None
    graph = []
    for i in s1:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
    #print tmp_dict

    for i in s1:
        for j in s1[i]:
            #print tmp_dict[i], tmp_dict[j[0]], j[1]
            u,v,w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u,v,w])
    #print graph

    return KruskalMST(graph, count, inv_dict)


s1 = {'A': [('B', 2)],
      'B': [('A', 4), ('C', 2)],
      'C': [('A', 2), ('B', 5)]}
print question3(s1)

"""

Question 4

Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

and the answer would be 3.

"""


def question4(T, r, n1, n2):
    n1_ps = []
    while n1 != r:
        n1 = parent(T, n1)
        n1_ps.append(n1)
    if len(n1_ps) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_ps:
            return n2
    return -1
    
    
def parent(T, n):
	#return parent of n if it exists, otherwise return -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
"""
Question 5

Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    i = ll
    j = ll
    #increment i m spaces forward from the start
    for val in range(m):
        if i is None:
            return None
        i = i.next
	#when i is none, j is the ith element from the end
    while i is not None:
	i = i.next
        j = j.next
    return j.data


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)
ll.next.next.next.next.next = Node(6)
ll.next.next.next.next.next.next = Node(7)



print question5(ll, 1)
print question5(ll, 2)
print question5(ll, 3)
print question5(ll, 4)
print question5(ll, 5)
print question5(ll, 6)
print question5(ll, 7)
print question5(ll, 8)


