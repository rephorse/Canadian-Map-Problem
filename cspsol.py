import tkinter as tk
from tkinter import font
from graph import GraphSolutions
import networkx as nx
import matplotlib.pyplot as plt
#height and with of the window frame
HEIGHT=700 
WIDTH= 800


sol = GraphSolutions() #creates a Graph Object
listD = sol.getDomain().copy()	#stores the domain
root = tk.Tk() #creates a frame
root.title("Canadian map colouring problem")

 
#draws the graph and shows it
def drawGraph():	
	edges = sol.getNeighbors()
	colors = sol.getAllSolutions()
	nodes = []
	for x in colors[listSol.curselection()[0]]:
		nodes.append(x[:2])
	color_map = []
	#separates colors from the nodes and creates a colormap
	for x in colors[listSol.curselection()[0]]:
		if(x[-1]=="1"):
			color_map.append("#F08484")
		if(x[-1]=="2"):
			color_map.append("lightblue")
		if(x[-1]=="3"):
			color_map.append("#3DE929")
		if(x[-1]=="4"):
			color_map.append("yellow")
		if(x[-1]=="5"):
			color_map.append("#D784F0")
		if(x[-1]=="6"):
			color_map.append("grey")
	G=nx.Graph()
	G.add_nodes_from(nodes)
	G.add_edges_from(edges)
	nx.draw(G,with_labels=True, node_color=color_map, node_size=800)
	plt.show() #shows the graph
		
#adds the domain to the list in the frame
def addDomain():
	if len(entryAdd.get())!=0:
		if entryAdd.get() not in listD and (int(entryAdd.get())<7) and len(listD)<4:
			listD.append(entryAdd.get()) 
			sol.setDomain(listD)
			listDomain.insert(tk.END,entryAdd.get())
		entryAdd.delete(0,tk.END)

#removes the value from the domain
def removeDomain():
	if len(entryAdd.get())!=0: #if there is an entry in the list, perform proc.
		if entryAdd.get() in listD: #checks if entry is in the list and removes it accordingly
			listD.remove(entryAdd.get())
			popList()
			sol.setDomain(listD)
		entryAdd.delete(0,tk.END)

#populates the list with the domains
def popList():
	listDomain.delete(0,tk.END)
	for x in listD:
		listDomain.insert(tk.END,x)
	

#populates the solution list and changes it if a new solution is being computed
def popSol():
	sol.runSolution()
	listSolutions = sol.getAllSolutions()
#	listDomain.delete(0,tk.END)
	listSol.delete(0,tk.END)
	for x in listSolutions:
		listSol.insert(tk.END,x)
	listSol.select_set(0)
	labelSolFound.config(text ="Amount of Solutions found: "+ str(sol.getAmountSolutions()))
	popList()

#creates the canvas with the pixels
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

#adds a frame
frameAdd = tk.Frame(root,bg='lightgreen')
frameAdd.place(relx=0.02,rely=0.05,relwidth=0.96,relheight=0.2)

#label for the domain manipulation
label = tk.Label(frameAdd,text="Adds/Removes a color/value to the Domain. Valid values = 1-6 (no more than 4 values in the domain)",bg='grey')
label.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.2)

#lable for the domain box
labelDomain = tk.Label(frameAdd,text="Domain",bg='grey')
labelDomain.place(relx=0.05,rely=0.35,relwidth=0.3,relheight=0.1)

#box with the domains(The rest of the code creates the labels and the buttons
listDomain = tk.Listbox(frameAdd,height=5)
popList()
listDomain.place(relx=0.05,rely=0.45,relwidth=0.3,relheight=0.5)

#label for entry of values
labelEntry = tk.Label(frameAdd,text="Value to add/remove",bg='grey')
labelEntry.place(relx=0.4,rely=0.35,relwidth=0.3,relheight=0.1)

#entry to add values
entryAdd = tk.Entry(frameAdd,font = font.Font(size=15))
entryAdd.place(relx=0.4,rely=0.45,relwidth=0.3,relheight=0.5)

#button to add the domain
addDomain = tk.Button(frameAdd,text="Add",bg='lightblue',command=addDomain)
addDomain.place(relx=0.75,rely=0.35,relwidth=0.1,relheight=0.6)

#button to remove from the domain
remDomain = tk.Button(frameAdd,text="Remove",bg='lightblue',command=removeDomain)
remDomain.place(relx=0.85,rely=0.35,relwidth=0.1,relheight=0.6)

#frame for the solutions
frameSol = tk.Frame(root,bg='lightgreen')
frameSol.place(relx=0.02,rely=0.3,relwidth=0.96,relheight=0.6)

getSol = tk.Button(frameSol,text="Compute solutions",bg='lightblue',command=popSol)
getSol.place(relx=0.05,rely=0.025,relwidth=0.9,relheight=0.1)

drawGraph = tk.Button(frameSol,text="Draw Selected Graph",bg='lightblue',command=drawGraph)
drawGraph.place(relx=0.05,rely=0.15,relwidth=0.9,relheight=0.1)

#stores minimum number of colors needed. only needs to be computed at beginning
minimumValue = "Minimum number of colors are: " + str(sol.getMinSol())

labelminS = tk.Label(frameSol,text=minimumValue,bg='yellow')
labelminS.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.05)

#stores solutions found
solutionsFound =("Amount of solutions found: " + str(sol.getAmountSolutions()))
labelSolFound = tk.Label(frameSol,text=solutionsFound,bg='yellow')
labelSolFound.place(relx=0.05,rely=0.36,relwidth=0.9,relheight=0.05)

listSol = tk.Listbox(frameSol)
popSol()
listSol.place(relx=0.05,rely=0.45,relwidth=0.9,relheight=0.55)



root.mainloop()


