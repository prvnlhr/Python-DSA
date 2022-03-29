'''
1.
   class bitwise_operator
    {
        public static void main(String args[])
        {
            int var1 = 42;
            int var2 = !var1;
            System.out.print(var1 + " " + var2);
        }
    }
1. 42 -42
2. 42 43
3. 42 -43
4. 0   0
_________________________________________________________________________



2.
   class bitwise_operator
    {
        public static void main(String args[])
        {
             int a = 3;
             int b = 6;
     	     int c = a | b;
             int d = a & b;
             System.out.println(c + " "  + d);
        }
    }


a) 7 2
b) 7 7
c) 7 5
d) 5 2
_________________________________________________________________________

3. Correct statement from below ??

A. int[] c = new int[];
B. String[] c = new int[5];
C. int[] c = new int[4];
D. String[] c = new String[20];
E. String[] c = new String[];


1. E A
2. C D
3. C A
4. B E

_________________________________________________________________________




4. class Array
    {
        public static void main(String args[])
        {

        int arr[] = new int[3];
             System.out.println("arr[0]"+ arr[2]);
        }
    }


 1. arr[2] is 3
 2. arr[0] has no value
 3. arr[2] is 0
 4. arr[0] out of index error



 5.

  class Array{
        public static void main(String args[]){

        int myList[] = [1,5,5,5,1];
        int val = myList[0];
        int indexMax = 0;
        for(int currIndex = 1; currIndex <myList.length;currIndex++){
        if (myList[currIndex] > val){
        val = mayList[currIndex];
        indexMax = currIndex;
        }
   }
   System.out.println(indexMax);
        }
    }
1. 1
2. 2
3. 3
4. 4
--------------------------------------------------------------------------

6.   public static void main(){

        int a[] = [0,2,4,1,3];

        for (int i =0; i<a.length;i++){
            a[i] = a[(a[2]+3) % a.length];
        }
}
What is the value of a[1] ??

1. 2
2. 1
3. 4
4. 5
------------------------------------------------------------------------------------------------------------------


7. class Test2 {
public
    static void main(String[] args)
    {
        String str[] = { "Geeks", "for", "Geeks" };
        for (int i = 0; i < str.length; i++)
            System.out.print(str[i]);
    }
}
A)Geeks for  Geeks
B)GeeksforGeeks
C) 0 1 2
D) 0 1

------------------------------------------------------------------------------------------------------------------

8. class Test2 {
public
    static void main(String[] args)
    {
        String str[] = { "Geeks", "for", "Geeks" };
        String srt = str[0]
        System.out.println(str.length);
        System.out.println(srt.length());
    }
}

1. 3 3
2. 4 3
3. 3 5
4. Error
------------------------------------------------------------------------------------------------------------------





9.

class Test5 {
public
    static void main(String[] args)
    {
        int arr[] = new int[5];
        int arr2[] = new int[5];
        System.out.print(arr.length + " ");
        System.out.print(arr2.length());
    }
}

A) 5 5
B) Error
C) Exception
D) None

------------------------------------------------------------------------------------------------------------------

10.

class GfG
{
    public static void main(String args[])
    {
        String s1 = new String("geeksforgeeks");
        String s2 = new String("geeksforgeeks");
        if (s1 == s2){
            System.out.println("Equal");
            }
        else{
            System.out.println("Not equal");
            }
            System.out.println("Error");

    }
}
1. Equal Error
2. Not Equal Error
3. Error , cant compare strings using == operator
4. None
------------------------------------------------------------------------------------------------------------------

11.

public class Main
{
    public static void main(String args[])
    {
         String s1 = "abc";
        String s2 = s1;
        s1 += "d";
        System.out.println(s1 + " " + s2 + " " + (s1 == s2));

        String sb1 = new String("abc");
        String sb2 = sb1;
        System.out.println(sb1 + " " + sb2 + " " + (sb1 == sb2));
    }
}
OUTPUT ??

------------------------------------------------------------------------------------------------------------------
12.


 class bitwise_operator
    {
        public static void main(String args[])
        {

            int s = 20;
            if(s == 20){
                  System.out.print("A");
                  int c = 21;
                  s = s | 21;

            }
            if(s == 21){
                  System.out.print("B");
            }
            else{
                  System.out.print("C");
            }
    }
    }


1. AC
2. AB
3. C
4. BC





'''
