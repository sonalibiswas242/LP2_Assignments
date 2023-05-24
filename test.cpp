// STL implementation of Prim's algorithm for MST
#include<iostream>
#include <vector>
#include <queue>
#include <list>
using namespace std;
# define INF 0x3f3f3f3f

// iPair ==> Integer Pair
typedef pair<int, int> iPair;

// This class represents a directed graph using
// adjacency list representation
class Graph
{
	int V; // No. of vertices

	// In a weighted graph, we need to store vertex
	// and weight pair for every edge
	list< pair<int, int> > *adj;

public:
	Graph(int V); // Constructor

	// function to add an edge to graph
	void addEdge(int u, int v, int w);

	// Print MST using Prim's algorithm
	void primMST();
};

// Allocates memory for adjacency list
Graph::Graph(int V)
{
	this->V = V;
	adj = new list<iPair> [V];
}

void Graph::addEdge(int u, int v, int w)
{
	adj[u].push_back(make_pair(v, w));
	adj[v].push_back(make_pair(u, w));
}

// Prints shortest paths from src to all other vertices
void Graph::primMST()
{
	// Create a priority queue to store vertices that
	// are being primMST. This is weird syntax in C++.
	// Refer below link for details of this syntax
	// https://www.geeksforgeeks.org/implement-min-heap-using-stl/
	priority_queue< iPair, vector <iPair> , greater<iPair> > pq;

	int src = 0; // Taking vertex 0 as source

	// Create a vector for keys and initialize all
	// keys as infinite (INF)
	vector<int> key(V, INF);

	// To store parent array which in turn store MST
	vector<int> parent(V, -1);

	// To keep track of vertices included in MST
	vector<bool> inMST(V, false);

	// Insert source itself in priority queue and initialize
	// its key as 0.
	pq.push(make_pair(0, src));
	key[src] = 0;
    int sum = 0;

	/* Looping till priority queue becomes empty */
	while (!pq.empty())
	{
		// The first vertex in pair is the minimum key
		// vertex, extract it from priority queue.
		// vertex label is stored in second of pair (it
		// has to be done this way to keep the vertices
		// sorted key (key must be first item
		// in pair)
		int u = pq.top().second;
		pq.pop();
		
		//Different key values for same vertex may exist in the priority queue.
		//The one with the least key value is always processed first.
		//Therefore, ignore the rest.
		if(inMST[u] == true){
			continue;
		}
	
		inMST[u] = true; // Include vertex in MST

		// 'i' is used to get all adjacent vertices of a vertex
		list< pair<int, int> >::iterator i;
		for (i = adj[u].begin(); i != adj[u].end(); ++i)
		{
			// Get vertex label and weight of current adjacent
			// of u.
			int v = (*i).first;
			int weight = (*i).second;

			// If v is not in MST and weight of (u,v) is smaller
			// than current key of v
			if (inMST[v] == false && key[v] > weight)
			{
				// Updating key of v
				key[v] = weight;
				pq.push(make_pair(key[v], v));
				parent[v] = u;
			}
		}
	}

	// Print edges of MST using parent array
    cout<<"Vertices of minimum spanning tree are: ";
	for (int i = 1; i < V; ++i)
    {
        sum += key[i];
        cout<<parent[i] + 1<<" - "<< i + 1 <<endl;
    }
    cout << "Minimum Spanning Tree Weight: " << sum << endl;
    
}

// Driver program to test methods of graph class
int main()
{
	// create the graph given in above figure
	int V,E;
    cout<<"Enter number of vertices: ";
    cin>>V;
	Graph g(V);

    cout<<"Enter numver of edges: ";
    cin>>E;

    cout<<"Enter vertices and weights ( v1 , v2 , weight ): "<<endl;
    for(int i = 0; i < E ; i ++)
    {
        int u,v,wt;
        cin>>u>>v>>wt;
        g.addEdge(u-1,v-1,wt);
    }

	g.primMST();

	return 0;
}
