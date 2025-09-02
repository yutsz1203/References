package basics;

public class Arrays {

    public static void main (String[] args){
        // one-dimensional arrays
        int[] intArray = new int[10];
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};

        for (int i = 0; i < vowels.length; i++){
            System.out.println(vowels[i]);
        }

        // multi-dimensional arrays
        int [][] matrix = new int[10][10];
        char[][] ca = { {'W', 'A', 'S', 'D'},
                        {'I', 'J', 'K', 'L'},
                        {'1', '2'}
                      };
        for (int i = 0; i < ca.length; i++){
            for (int j = 0; j < ca[i].length; j++){
                System.out.println(ca[i][j]);
            }
        }
    }
    
}
