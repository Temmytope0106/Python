import java.util.Scanner;
public class TuringTest{
public static void main(String...args){
Scanner input = new Scanner(System.in);

	System.out.print("What is your problem?: ");
	String answer1 = input.nextLine();

	System.out.print("Have you had this problem before(True or False)?: ");
	boolean answer2 = input.nextBoolean();

	if(answer2==true) System.out.print("Well, you have it again.");
	else System.out.print("Well, you have it now.");

}
}