import java.util.Scanner;
public class Factorial{
	public static void main(String []args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a non-negative number to calculate: ");
	int number = input.nextInt();

	int count = 1;
	double factorial = 1;

	if(number < 0 ){
	System.out.print("Sorry this is a negative number");
	
	}else{
	
	for(count = 1; count <= number; count++){
		
		factorial *= count;
	}
	
	System.out.print(number);
	System.out.print(" factorial is ");
	System.out.print(factorial);
}
}
}