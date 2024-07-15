import java.util.Scanner;
public class GasMileage{
	public static void main(String []args){
	Scanner input = new Scanner(System.in);
	
	
	System.out.print("Input number of miles driven or -1 to quit: ");
	int milesDriven = input.nextInt();

	System.out.print("Input number of gallons used or -1 to quit: ");
	int gallonsUsed = input.nextInt();

	float milePerGallon = 0;
	float sum = 0;	
	
	
	while( milesDriven != -1){ 

	milePerGallon = ( milesDriven / gallonsUsed );

	sum += milePerGallon;
	System.out.print("The mile per gallon for this trip is: ");
	System.out.println(sum);

	
	System.out.print("Input number of miles driven or -1 to quit: ");
	milesDriven = input.nextInt();

	System.out.print("Input number of gallons used or -1 to quit: ");
	gallonsUsed = input.nextInt();

	}
	
	System.out.print("The total mile per gallon for all the trips is: ");
	System.out.print(sum);

}
}