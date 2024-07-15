public class BruteForce{
public static void main(String...args){

for(int a = 1; a <= 20; a++){
for(int b = a; b <= 20; b++){
for(int c = b; c <= 20; c++){
if((Math.pow(a, 2)) + (Math.pow(b, 2)) == (Math.pow(c, 2)))
System.out.printf("\n%d   %d    %d", a, b, c);

}}}


}
}