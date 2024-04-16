/* 
    Obtenha a entrada padrão Peso (int), a altura (double) e imprima o IMC (Índice de Massa Corporal)
 
    IMC = peso em quilogramas dividido pela altura em metros, elevada ao quadrado
*/

import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        int peso;
        double altura;

        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite o seu peso. Ex: 81 (número inteiro): ");
        peso = teclado.nextInt();

        System.out.println("Digite a sua altura. Ex: 1,70: ");
        altura = teclado.nextDouble();
        teclado.close();

        double imc = peso / (altura * altura);
        System.out.printf("Seu índice de massa corporal é: %.2f", imc);
    }
}