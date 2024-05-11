/*  
    IGUALDADE
        I - Operador "==
            Leva em conta o endereço de memória do que está sendo comparado
        II - Método equals()
            Leva em consideração o conteúdo dos elementos comparados
*/

public class App {
    public static void main(String[] args) throws Exception {
        // EXEMPLO 1
        String s1 = new String("Mensagem");
        String s2 = new String("Mensagem");
        String s3 = s1;

        System.out.println(s1 == s2); // false - endereço de memória diferente
        System.out.println(s3 == s1); // true - mesmo endereço de memória

        // EXEMPLO 2
        System.out.println();
        System.out.println(s1.equals(s2)); // true - mesmo conteúdo
        System.out.println(s1.equals(s3)); // true - mesmo conteúdo

        // EXEMPLO 3
        System.out.println();
        Usuario user1 = new Usuario(001, "Renard", "111222333-44");
        Usuario user2 = new Usuario(002, "Esdras", "222333444-55");
        Usuario user3 = user1;

        System.out.println(user1 == user2); // false - endereço de memória diferente
        System.out.println(user3 == user1); // true - mesmo endereço de memória

        // EXEMPLO 4 (método criado por nós)
        System.out.println();
        System.out.println(user1.equals(user2)); // false - objetos diferentes
        System.out.println(user1.equals(user3)); // true - objetos iguais 
    }
}
