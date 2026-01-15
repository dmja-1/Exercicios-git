package fundamentos.desafiomodulofundamentos;

import java.util.Scanner;

public class DesafioCelsiusParaFahrenheit {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite a temperatura em Celsius: ");
		double celsius = entrada.nextDouble();
		
		double fahrenheit = (1.8 * celsius) + 32;
		
		System.out.printf("A temperatura em Fahrenheit é de %.1f.", fahrenheit);
		
		entrada.close();
	}
}
