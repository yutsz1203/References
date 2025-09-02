package exception;

import java.io.IOException;
import exception.Processor;

// To run this, need to compile by: javac *.java
// Then go one level up, run by: java exception.Demo arg1 arg2 ...

public class Demo {
    public static void main (String[] args){
        Processor proc = new Processor();

        try{
            proc.check(args);
        } catch (Exception e){
            System.err.println(e);
            System.exit(1);
        }
    }
}
