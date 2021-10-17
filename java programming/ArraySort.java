import java.util.*;
public class ArraySort {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		System.out.println("Enter the number of array elements");
		int num=scan.nextInt();
		int[] unsorted=new int[num];
		for(int i=0;i<num;i++) {
			System.out.println("Enter a number:");
			unsorted[i]=scan.nextInt();
		}
		
		sorted(unsorted);
	}
	public static void sorted(int unsorted[]) {
		for(int j=0;j<unsorted.length-1;j++) {
			for(int i=j+1;i<unsorted.length;i++) {
				if(unsorted[i]<unsorted[j]) {
					int temp=unsorted[i];
					unsorted[i]=unsorted[j];
					unsorted[j]=temp;
				}
			}
		}
		for(int a:unsorted) {
			System.out.println("The sorted Array"+a);
		}
		
		
	}
	

}
