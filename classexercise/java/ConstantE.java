import java.util.Scanner;
public class ConstantE{
	public static void main(String []args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter the number to calculate: ");
	int number = input.nextInt();

	double factorial = 1;
	double e = 1;
	int count = 1;
	double constant = 0;
	
	for(count = 1; count <= number; count++){
		
		factorial *= count;
		e += ( 1 / factorial );
		
	}
		constant = e + 1;

	System.out.print("The constant e is ");
	System.out.print(constant);



}
}