package fundamentos.desafiomodulofundamentos;

import java.util.Scanner;

public class DesafioCalculadoraIMC {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite seu peso em KG: ");
		double peso = entrada.nextDouble();
		
		System.out.println("Digite sua altura em M: ");
		Double altura = entrada.nextDouble();
		
		double imc = peso / Math.pow(altura, 2);
		
		String resultado = imc < 18.5 ? resultado = "Abaixo do peso" : "";
		resultado = 18.5 <= imc && imc <= 24.99 ? resultado = "Peso Normal" : resultado;
		resultado = 25 <= imc && imc <= 29.99 ? resultado = "Sobrepeso" : resultado;
		resultado = 30 <= imc ? resultado = "Obesidade" : resultado;
		
		System.out.printf("Seu IMC é de %.2f. Status do peso: %s", imc, resultado);
		
		entrada.close();
	}
}
