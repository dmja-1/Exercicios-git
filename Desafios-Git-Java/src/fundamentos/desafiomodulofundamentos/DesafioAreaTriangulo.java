package fundamentos.desafiomodulofundamentos;

import java.util.Scanner;

public class DesafioAreaTriangulo {

	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite a base do triângulo: ");
		double base = entrada.nextDouble();
		System.out.println("Digite a altura do triângulo: ");
		double altura = entrada.nextDouble();
		
		double area = (base * altura) / 2;
		
		System.out.printf("O triângulo de base %.1f e de altura %.1f tem uma área total de %.1f.", base, altura, area);
		
		entrada.close();
	}
}
