import java.util.Scanner;
public class BankAccount{
public static void main(String []args){
	Scanner input = new Scanner(System.in);

	int totalAmount = 0;
	int totalWithdraw = 0;
	int balance = 0;
	

	System.out.print("Enter 1 to deposit or 2 to withdraw or 3 to check Balance or -1 to quit: ");
	int decision = input.nextInt();
	

	while(decision != -1){
	
	if(decision == 1){ 
	System.out.print("Enter amount to deposit: ");
	int amount = input.nextInt();
	totalAmount += amount;
	
	}else if(decision == 2){
	System.out.print("Enter amount to withdraw: ");
	int withdraw = input.nextInt();
	if(withdraw > totalAmount) System.out.println("Invalid number");
	else totalAmount -= withdraw;
	
	}else if(decision == 3){
	System.out.println("Your balance is " +totalAmount);
	}else break;
	
	System.out.print("Enter 1 to deposit or 2 to withdraw or 3 to check Balance or -1 to quit: ");
	decision = input.nextInt();

	}

	
	


}
}