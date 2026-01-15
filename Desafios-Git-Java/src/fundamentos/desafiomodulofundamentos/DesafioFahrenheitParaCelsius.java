package fundamentos.desafiomodulofundamentos;

import java.util.Scanner;

public class DesafioFahrenheitParaCelsius {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite a temperatura em Fahrenheit: ");
		double fahrenheit = entrada.nextDouble();
		
		double celsius = (fahrenheit - 32) / 1.8;
		
		System.out.printf("A temperatura em Celsius é de %.1f.", celsius);
		
		entrada.close();
	}
}
