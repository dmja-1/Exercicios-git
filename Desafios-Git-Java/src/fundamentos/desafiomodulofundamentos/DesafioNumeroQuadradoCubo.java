package fundamentos.desafiomodulofundamentos;

import java.util.Scanner;

public class DesafioNumeroQuadradoCubo {
	
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite um número: ");
		double num = entrada.nextDouble();
		
		double quadrado = Math.pow(num, 2);
		double cubo = Math.pow(num, 3);
		
		System.out.printf("Ao quadrado: %.2f | Ao cubo: %.2f", quadrado, cubo);
		
		entrada.close();
	}
}