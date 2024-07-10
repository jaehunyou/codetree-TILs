import java.util.Scanner;

public class Main {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        // 추가 코드 작성

        double a = sc.nextDouble();
        double b = sc.nextDouble();

        double sum = a + b;

        System.out.printf("%.2f", sum);

    }
}