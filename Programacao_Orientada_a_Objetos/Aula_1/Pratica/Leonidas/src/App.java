/* 
    Leônidas é constantemente questionado sobre quantos soldados seus 300 espartanos irão enfrentar.

    Ajude Leônidas, fazendo um pequeno jogo de advinhação em que o jogador deve dar um palpite. 
    Se o palpite for abaixo ou acima do valor correto, imprima mensagens adequadas.

    Valor correto: 10.000
*/

import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner teclado = new Scanner(System.in);

        int palpite;
        int valorCorreto = 10000;
        String msg;

        System.out.println("Digite o seu palpite: ");
        palpite = teclado.nextInt();

        while (palpite != valorCorreto) {
            msg = palpite > valorCorreto ? "Um pouco menos..." : "Um pouco mais...";
            System.out.println(msg);

            /* if (palpite > valorCorreto) {
                System.out.println("Um pouco menos...");
            } else {
                System.out.println("Um pouco mais...");
            } */

            System.out.println("Digite outro palpite: ");
            palpite = teclado.nextInt();
        }

        teclado.close();
        System.out.println("Parabéns, você acertou!");
    }
}
