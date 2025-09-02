package OOP;

public class CloneDemo {
    public static void main(String[] args){
        Elephant e1 = new Elephant("Joe", 5);
        Elephant e3;

        e3 = e1.clone();
        e3.getName();

    }
}
