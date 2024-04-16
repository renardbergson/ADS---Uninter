/*  
    Leia uma sequência de Strings e as imprima em ordem reversa. Utilize um método para fazer isso.
*/

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner teclado = new Scanner(System.in);

        ArrayList<String> listaNomes = new ArrayList<String>();

        System.out.println("Digite a quantidade de nomes que deseja inserir numa lista. (Ex: 10): ");
        int quantidade = teclado.nextInt();

        System.out.println();
        String nome;
        for (int i = 0; i < quantidade; i ++) {
            System.out.println("Digite o nome: ");
            nome = teclado.next();
            listaNomes.add(nome);
        }

        System.out.println();

        // o índice do último elemento de uma coleção sempre é a quantidade de elementos menos um!
        
        /* for (int i = listaNomes.size() - 1; i >= 0; i --) {
            System.out.println(listaNomes.get(i)); // num array, usa-se colchetes, num arrayList usa-se .get()
        }
        */

        System.out.println("Ordem normal:");
        System.out.println(listaNomes);

        Collections.reverse(listaNomes); // MÉTODO
        System.out.println();

        System.out.println("Ordem reversa:");
        System.out.println(listaNomes);
    }
}
