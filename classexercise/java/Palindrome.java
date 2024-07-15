import java.util.Scanner;
public class Palindrome{
	public static void main(String []args){
	Scanner input = new Scanner(System.in);

	System.out.print("Input a five-digit number: ");
	int number = input.nextInt();
 	
	int digit1 = number / 10000 % 10;
	int digit2 = number / 1000 % 10;
	int digit3 = number / 100 % 10;
	int digit4 = number / 10 % 10;
	int digit5 = number / 1 % 10;

	if(digit1 == digit5 && digit2 == digit4){
	System.out.print(number);
	System.out.print(" is a palindrome.");
	}else{
	System.out.print(number);
	System.out.print(" is not a palindrome.");
	}





}
}