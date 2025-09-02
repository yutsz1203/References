package basics;

public class Strings {
    public static void main(String[] args){
        String s1 = "Hello";
        
        // charAt(int index): returns the char value at the specified index
        System.out.println(s1.charAt(0));

        // compareTo(String anotherString): compares to strings lexicographically (return difference)
        System.out.println(s1.compareTo("A")); // 7

        // concat(String str)
        System.out.println(s1.concat("World"));

        // equals(Object anObject): Compares this string to the specified object
        System.out.println(s1.equals("Hello"));
        
        // length(): returns the length of the string
        System.out.println(s1.length());
    }
}
