import java.util.Scanner;
public class SquareCube{
	public static void main(String []args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a number from 1 to 10: ");
	int number = input.nextInt(); 
	
	System.out.println("\nNumber\tSquare\tCube");
	
	for(int num = 0; num <= number; num++){

	System.out.println(num + "\t" + Math.pow(num, 2) + "\t" + Math.pow(num, 3));
	
	}
	
	
	
	
	

	
	






}
}