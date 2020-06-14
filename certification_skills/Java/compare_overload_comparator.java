// create a class comparator with 3 overloading methods which have int ,strings and arrays as inputs in 3 diff methods
import Java.util.Arrays;
class Comparator{
//creating for int overloading method
boolean compare(int a,int b)
{
return (a==b);
}

//creating for String overloading method
boolean compare(String a,String b)
{
return (a.equals(b));
}

//creating for Arrays overlaoding method

boolean compare(int[] a,int[] b)
{
return (Arrays.equals(a,b));
}

}
