import java.util.Scanner;
public class Pattern{
	public static void main(String []args){
	Scanner input = new Scanner(System.in);

	System.out.print("Pattern A");
	System.out.println();

	int row = 1;
	int column = 1;
	
	
	for(row = 1; row <= 6; row++){
	
	for(column = 1; column <= row; column++)System.out.print("*");
	System.out.println();
	
	}

	System.out.println();
	System.out.print("Pattern B");
	System.out.println();

	 row = 1;
	 column = 1;
	 
	
	for(row = 1; row <= 6; row++){
	
	for(column = 1; column <= 7 - row; column++) System.out.print("*");
	System.out.println();
	
	}

	System.out.print("Pattern C");
	System.out.println();

	row = 1;
	column = 1;
	int N = 6;

	for(row = 1; row <= 6; row++){

	for(int space = 1; space <= 5 + row - N; space++) System.out.print(" ");{
	 for(column = 1; column <= N - row + 1; column++){ System.out.print("*"); }
	
	System.out.println();
	}}



}
}