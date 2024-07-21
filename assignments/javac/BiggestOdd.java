import java.util.Scanner;
public class BiggestOdd{
	
	public static int decider(int number){
	int reverseNumber = 0;	
	int largest = 2;
	int num = 0;

	while(number > 0){

	reverseNumber = (reverseNumber * 10) + (number % 10);
	num = number % 10;
	if(num > largest && num % 2 != 0) largest = num;
	number = number / 10;
	
		}
	return largest;
	}

public static void main(String...args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int number = input.nextInt();
	int result = decider(number);
	System.out.print(result);
	}





}
				
				