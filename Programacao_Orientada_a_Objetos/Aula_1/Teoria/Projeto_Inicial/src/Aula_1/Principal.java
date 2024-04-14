package Aula_1;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		int idade = 10;
		idade = idade + 1;
		
		int ano = 2024;
		double peso = 86.5;
		
		System.out.print("Hello World! ");
		System.out.println("Este é o meu primeiro código em Java");
		System.out.println("A idade é igual a " + idade);
		System.out.printf("O ano é %d \n", ano); 
		System.out.printf("O peso do programador hoje é de aproximadamente %.2f Kg \n", peso);
		
		Scanner teclado = new Scanner(System.in);
		// Scanner é uma classe, teclado é a variável que a representa, com new instanciamos o Scanner
		System.out.println("Digite um nome para mostrar: ");
		String novoNome = teclado.next();	
		System.out.println("Digite uma idade para mostrar: ");
		int novaIdade = teclado.nextInt();
		System.out.println("Digite um peso para mostrar: ");
		double novoPeso = teclado.nextDouble();
		
		System.out.println("Nome: " + novoNome);
		System.out.println("Idade: " + novaIdade);
		System.out.println("Peso: " + novoPeso);
		
		if (novaIdade < 18) {
			System.out.println("Acesso Bloqueado");
		} else if (novaIdade < 65) {
			System.out.println("Um adulto acessou");
		} else {
			System.out.println("Um adulto idoso acessou");
		}
		
		System.out.println("Contagem de 1 a 10 usando laço FOR");
		for (int i = 1; i < 11; i++) {
			System.out.println(i);
		}
		
		int arrNumInt[] = {10,20,30,40,50}; // array de números inteiros
		arrNumInt[0] = 5; // substituindo valores
		
		int arrNumIntVaz[] = new int[200]; // array de números inteiros, vazio, com 200 elementos
		arrNumIntVaz[60] = 55; // atribuindo valor
	}

}