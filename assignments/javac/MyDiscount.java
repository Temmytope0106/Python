import java.util.Scanner;
public class MyDiscount{

	public static double calculate(int price, int discount){

	double result = price - ((discount / 100) * price);
	
	return result;
	}

	
public static void main(String...args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a price: ");
	int price = input.nextInt();

	System.out.print("Enter a discount rate: ");
	int discount = input.nextInt();

	double total = calculate(price, discount);
	System.out.print(total);


}
}