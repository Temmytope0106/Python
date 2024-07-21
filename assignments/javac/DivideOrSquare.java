import java.util.Scanner;
public class DivideOrSquare{

	public static double divide(int number){

	if(number % 5 == 0) return Math.pow(number, 0.5);

	else return number % 5;
	}
	

public static void main(String...args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int number = input.nextInt();

	double total = divide(number);
	System.out.print(total);




}





}