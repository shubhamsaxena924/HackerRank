import java.util.Scanner;

public class JavaStringReverseTwo {
     public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        boolean ch = true;
        for(int i=0;i<=A.length()/2;i++) {
            if(A.charAt(i)!=A.charAt(A.length()-1-i)) {
                ch=false;
                break;
            }
        }        
        System.out.println(ch?"Yes":"No");
    }
}