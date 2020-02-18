class GraphSolutions:
#constructor for the graph class. Initializes the dict holding the map, the domain with some default values
	def __init__(self):
		self.neighbors = {
		"BC" :["AB","NT","YU"],
		"AB" :["BC","NT","SA"],
		"ON" :["MA","QB"],
		"QB":["ON","NL","NB"],
		"NS":["PE","NB"],
		"NB":["NS","QB"],
		"MA":["SA","NU","ON"],
		"PE":["NS"],
		"SA":["MA","NT","AB"],
		"NL":["QB"], 
		"NT":["YU","NU","BC","AB","SA"],
		"YU":["BC","NT"],
		"NU":["NT","MA"]
		}
		self.neighbors1 = {
		"A": ["B","C"],
		"B": ["A"],
		"C": ["A"]
		}
		#default values for the domain
		self.domain = ["1","2","3"]
		self.possibleDomainSol = {} #to store solutions
		self.visited=[] #nodes marked as visited
		self.pathSol=[] #paths to solutions
		self.solutions=[] #list containing the paths
		self.minSol = 0	#number of colors necesary, default 0
		self.nodes = []

#returns the domain
	def getDomain(self):
		return self.domain

#sets the domain to the desired values
	def setDomain(self,listOfDomains):
		self.domain=listOfDomains

#recursive function to generate all solutions
	def exSearch(self, current, next):
		if self.checkAssigned(current, next):
			self.visited.append(current)
			
			if len(self.nodes)==0:
				self.pathSol.append(current+next)
				self.solutions.append(self.pathSol.copy())
				self.pathSol.pop()
			else:
				self.pathSol.append(current+next)
				for x in self.domain:
					self.exSearch(self.nodes.pop(),x)
				self.pathSol.pop()
#			print(self.nodes)
			self.nodes.append(self.visited.pop())
		else:
			self.nodes.append(current)

#checks to see if all the nodes have been visited
	def checkLeaf(self, node, assignment):
		for x in self.neighbors:
			if x not in self.visited:
				return False
		else:
			return True

#checks to see if any of the neighbors of the node passed has been assigned a color and returns false if the assignment has been made
	def checkAssigned(self,node,assignment):	
		for x in self.neighbors[node]:
			if x+assignment in self.pathSol:
				return	False
		else:
			return True

#runs the recursive algorithm and stores the solution
	def runSolution(self):
		self.possibleDomainSol={}
		self.visited = []
		self.pathSol = []
		self.solutions = []
		self.nodes=[]
		for n in self.neighbors:
			self.nodes.append(n)
		for x in self.domain:
			self.exSearch(self.nodes.pop(),x)

#gets the neighbors as a list of tuples
	def getNeighbors(self):
		neig=[]
		for x in self.neighbors:
			for y in self.neighbors[x]:
				neig.append((x,y))
		return neig

#gets all the nodes in the graph
	def getNodes(self):
		nod=[]
		for x in self.neighbors:
			nod.append(x)
		return nod

#puts all solutions in a big list and returns it
	def getAllSolutions(self):
		return self.solutions.copy()

#returns the minimum number of colors
	def getMinSol(self):
		return 3

#amount of solutions found
	def getAmountSolutions(self):
		amount = 0
		so = self.getAllSolutions()
		amount = len(so)
		return amount
