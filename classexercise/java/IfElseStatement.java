import java.util.Scanner;
public class IfElseStatement{
public static void main(String...args){
	Scanner input = new Scanner(System.in);
	
	System.out.print("Enter first integer: ");
	int integer1 = input.nextInt();
	
	System.out.print("Enter second integer: ");
	int integer2 = input.nextInt();

	if(integer1 == integer2) System.out.printf("%d is equals to %d", integer1, integer2);
	else if(integer1 != integer2) System.out.printf("%d is not equals to %d", integer1, integer2);

	if(integer1 > integer2) System.out.printf("\n%d is greater than %d", integer1, integer2);
	else if(integer1 < integer2) System.out.printf("\n%d is lesser than %d", integer1, integer2);

	if(integer1 >= integer2) System.out.printf("\n%d is greater than or equals to %d", integer1, integer2);
	else if(integer1 <= integer2) System.out.printf("\n%d is lesser than or equals to %d", integer1, integer2);



}
}