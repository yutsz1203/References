package generics;

// Generics are used when we want to customise the data type at compile-time.
// CustomType is the type parameter of this class.
public class Data <CustomType>{
    public CustomType data;

    public Data (CustomType d){
        data = d;
    }

    public CustomType getData(){
        return data;
    }

    public void setData( CustomType d){
        data = d;
    }
}

/*
 * Multiple type parameters are also possible
 * public class Data<CustomTypeA, CustomTypeB> {
 *      public CustomTypeA dataA;
 *      public CustomTypeB dataB;
 * }
 * 
 * Data<String, Integer> s = new Data<String, Integer>();
 * 
 */


