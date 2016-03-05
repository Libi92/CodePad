import java.io.*;

class Displaynumber {
    public static void main(String[] args) {
    // Type your code here
       try{
       System.out.println("Enter a string");
       BufferedReader br=new BufferedReader (new InputStreamReader(System.in));
       String str=br.readLine();
      System.out.println("name is"+ str);
}
catch(Exception e)
{

}

    }
}