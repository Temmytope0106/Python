import java.util.Scanner;
public class Investment{
public static void main(String...args){

	int totalAmount = 0;
	int originalAmount = 1000;
	int annualRate = 7 / 100;
	for(int year = 1; year <= 30; year++){
	double principalOfTheYear = originalAmount * (Math.pow((1 + annualRate), year));
	totalAmount += principalOfTheYear;
	System.out.printf("\nThe amount for year %d is %d", year, totalAmount);
	}
	System.out.printf("\nThe total amount for 30years", totalAmount);


}
}