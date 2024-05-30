import java.util.*;

class Vertex<T>{

	private int ID;
	private T element;
	
	public Vertex(T element, int ID)
	{
		this.setElement(element);
		this.setID(ID);
	}
	
	public void setElement(T element) { this.element = element; }
	public T getElement()             { return this.element;    }
	public void setID(int element)    { this.ID = ID;           }
	public int getID()                { return this.ID;         }
}

class Graph{

	private List<ArrayList<Vertex<? super Object>>> adjacencies_list;
	private boolean is_digraph;
	
	public Graph(boolean is_digraph)
	{
		this.adjacencies_list = new LinkedList<>();
		this.is_digraph = is_digraph;
	}
	
	public int get_vertex_n() { return this.adjacencies_list.size();   }
	public int get_edges_n()  { return this.adjacencies_list.size()-1; }
	
	public void set_adjacency(Vertex<? super Object> v1, Vertex<? super Object> v2)
	{
	
		if(this.adjacencies_list.get(v1.getID()) == null) this.adjacencies_list.add(v1.getID(), new ArrayList<>());
		this.adjacencies_list.get(v1.getID()).add(v1.getID(), v2);
		
		if(!this.is_digraph)
		{
			if(this.adjacencies_list.get(v2.getID()) == null) this.adjacencies_list.add(v2.getID(), new ArrayList<>());
			this.adjacencies_list.get(v2.getID()).add(v2.getID(), v1);
		}
	}
	
	public void bfs(Vertex<? super Object> origin, Vertex<? super Object> destination)
	{
		Queue<Integer> bfs_queque;
	}
}

public class Main
{
	public static void main(String[] args)
	{
		final boolean is_digraph = true;
		
		System.out.println("Graph is initializted...");

		Graph graph = new Graph(is_digraph);
		
		System.out.println("Mounting a graph...");

		graph.set_adjacency(new Vertex<>(0, 0), new Vertex<>(0, 0));
	
	}
}