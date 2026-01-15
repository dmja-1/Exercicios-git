package fundamentos.desafiomodulofundamentos;

public class DesafioEquacaoSegundoGrau {

	public static void main(String[] args) {
		
		int A = 1; int B = 12; int C = -13;
		
		System.out.println("Fórmula: ax^2 + bx + c = 0");
		System.out.println("Aplicando: 1 * x^2 + 12 * x + (-13) = 0");
		
		double delta = Math.pow(B, 2) - 4 * A * C;
		double bhaskaraNegativa = (-B - Math.sqrt(delta)) / 2 * A;
		double bhaskaraPositiva = (-B + Math.sqrt(delta)) / 2 * A;
		
		System.out.printf("O resultado de X (negativo) é de: %.2f", bhaskaraNegativa);
		System.out.printf("\nO resultado de X (positivo) é de: %.2f", bhaskaraPositiva);
	}
}
