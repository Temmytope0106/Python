import java.util.Scanner;
public class EqualString{
	public static boolean decider(String word1, String word2){

		if(word1.length() == word2.length() && word1.equalsIgnoreCase(word2)) return true;
		

		else return false;


			}

	public static void main(String...args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a word: ");
	String word1 = input.nextLine();

	System.out.print("Enter a word: ");
	String word2 = input.nextLine();

	boolean result = decider(word1, word2);
	System.out.print(result);
	}



}