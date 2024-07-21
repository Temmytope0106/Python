import java.util.Scanner;
public class OnlyFloat{
	

	public static int decide(double number1, double number2){

	if( number1 == (float) number1 && number2 == (float) number2) return 2;
	if( number1 == (int) number1 && number2 == (float) number2) return 1;
	if( number1 == (float) number1 && number2 == (int) number2) return 1;
	else return 0;
	}

	

public static void main(String []args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a number: ");
	double number1 = input.nextInt();

	System.out.print("Enter a number: ");
	double number2 = input.nextInt();

	double total = decide(number1, number2);
	System.out.print(total);

}
}