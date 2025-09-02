package nested_class;

public class Computer {
    CPU intel, amd;
    RAM ram;

    // Static nested class. They are compiled into a separate .class file.
    public static class CPU{
        
    }

    public static class RAM{

    }
    // Non-static class
    class InnerComputer{

    }
}
