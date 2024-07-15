import java.util.Scanner;
public class LargestNumber{
public static void main(String []args){
Scanner input = new Scanner(System.in);

System.out.print("Enter the number of integers to input: ");
int num = input.nextInt();

int largest = 0;
int integer;

	int sum = 0;
	int product = 1;
	int integerdefault = 2;
	largest = integerdefault;
	
	for(int count = 1; count <= num; count++){
	
	System.out.printf("Enter integer %d : ", count);
	integer = input.nextInt();
	sum += integer;
	product *= integer;
	
	if(integer > largest) largest = integer;
	
	}
	
	double average = sum / num ;	

	System.out.println("The largest number of all is " +largest);
	System.out.println("The total sum is " +sum);
	System.out.println("The product is " +product);
	System.out.println("The average is " +average);



}
}