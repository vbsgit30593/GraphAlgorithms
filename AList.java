import java.util.*;
class AList{
    static ArrayList<ArrayList<Integer>> head = null;
    public AList(int vert){
        head = new ArrayList<ArrayList<Integer>>(vert);
        // allocate memory for each bucket
        for (int i = 0; i < vert; i++){
            head.add(new ArrayList<Integer>());
        }
    }
    public static void addEdge(int src, int dest){
        int s = head.size();
        System.out.println("Adding an edge from src : "+ src + " to dest : " + dest);
        head.get(src).add(dest);
    }
    public static void printList(){
        int s = head.size();
        System.out.println("-- Adjacency List contents --");
        for (int i = 0; i < s; i++){
            ArrayList<Integer> curVert = head.get(i);
            System.out.println("Vertex " + i + " : "+ Arrays.toString(curVert.toArray()));
        }
        System.out.println();
    }
}