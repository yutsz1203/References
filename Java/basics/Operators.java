package basics;

public class Operators {
    /*
     * instanceof: compares an object to a specified type (for classes)
     * type.class.isInstance(var): check if var is type
     * ~: Unary bitwise complement
     * <<: signed left shift
     * >>: signed right shift
     * >>>: unsigned right shift
     * &: bitwise and
     * ^: bitwise exlusive or (XOR)
     * | bitwise inclusive or
     */
    public static void main(String[] args){
        int x = 1;
        System.out.println(Integer.class.isInstance(x));
    }
}
