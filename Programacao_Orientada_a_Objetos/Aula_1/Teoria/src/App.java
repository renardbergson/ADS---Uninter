import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        System.out.println("This is my first project in Java");

        int age = 10;
        age = age + 1;

        int year = 2024;
        double weight = 86;

        System.out.println("The test age is equal to: " + age);
        System.out.printf("The year is %d \n", year);
        System.out.println("My weight today is likely equal to: " + weight);

        Scanner teclado = new Scanner(System.in);
        // Scanner é uma classe, teclado é a variável que a representa, com new instanciamos o Scanner
        
        System.out.println("Digite um nome para mostrar: ");
        String novoNome = teclado.next();

        System.out.println("Digite uma idade para mostrar: ");
        int novaIdade = teclado.nextInt();
        
        System.out.println("Por fim, digite um peso para mostrar: ");
        double novoPeso = teclado.nextDouble();


        System.out.println("Nome: " + novoNome);
        System.out.println("Idade: " + novaIdade);
        System.out.println("Peso: " + novoPeso);

        if (novaIdade < 18) {
            System.out.println("Acesso bloqueado");
        } else if (novaIdade < 65) {
            System.out.println("Um adulto acessou");
        } else {
            System.out.println("Um idoso acessou");
        }

        System.out.println("Contagem de 1 a 10 usando laço FOR");
        for (int i = 1; i < 11; i++) {
            System.out.println(i);
        }

        int arrNumInt[] = {10, 20, 30, 40, 50}; // array de números inteiros
        arrNumInt[0] = 5; // substituindo valores

        int arrNumIntVaz[] = new int[50]; // array de números inteiros, vazio, com 50 elementos
        arrNumIntVaz[50] = 22; // substituindo valores
    }
}
