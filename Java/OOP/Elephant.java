package OOP;

public class Elephant {

    private String name;
    private int ranking;
    
    // Constructor
    public Elephant(String name, int ranking){
        this.name = name;
        this.ranking = ranking;
    }

    public Elephant clone(){
        Elephant copy = new Elephant(this.name, this.ranking);
        return copy;
    }

    public void getName(){
        System.out.println(this.name);
    }

    // For copying

    public static void main (String[] args){
        Elephant e1 = new Elephant("Crazy", 0); // e1 is the object reference, holds the address of the object.
        e1.getName();

        // free up memory
        e1 = null;
    }
}


