/*  
    CRIANDO AS PRÓPRIAS EXCEÇÕES

    Veremos a seguir 3 formas de criar nossas próprias mensagens de exceção.

    I 
        a - com a palavra "throw", que significa "lançar"
        b - "throw new Exception" gera uma exceção do tipo checked, que precisa ser tratada com catch
    II 
        a - Lançando uma exceção sem tratamento
        b - throw new RuntimeException() lança uma exceção do tipo unchecked
        c - não é necessário usar try / catch
        d - neste caso, queremos mesmo encerrar o programa
    III
        a - criando uma classe específica para tratamento de exceção
        b - a classe precisa estender a superclasse "Exception"
        c - public class "nomeDaClasse" extends Exception ...
*/

import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println();
        System.out.println("Digite um número entre 0 e 10: ");
        Scanner teclado = new Scanner(System.in);
        int valor = teclado.nextInt();
        
        // CENÁRIO 1
        try {            
            if (valor < 0 || valor > 10) {
                System.out.println();
                throw new Exception("Valor digitado inválido!");
            } 
            else {
                System.out.println();
                System.out.println("O valor digitado foi: " + valor);
            }
        } 
        catch (Exception e) {
            System.out.println("Ocorreu um erro: " + e.getMessage()); // "valor digitado inválido"
            System.out.println();
        }
        finally {
            teclado.close();
        }

        // CENÁRIO 2
        /*         
            if (valor < 0 || valor > 10) {
                System.out.println();
                throw new RuntimeException("Valor digitado inválido!");
            }  
        */

        // CENÁRIO 3
        /* 
            try {            
                if (valor < 0 || valor > 10) {
                    System.out.println();
                    ValorInvalidoException erro = new ValorInvalidoException("Valor digitado inválido!");
                    throw new Exception(erro.mensagem);
                } 
                else {
                    System.out.println();
                    System.out.println("O valor digitado foi: " + valor);
                }
            } 
            catch (Exception e) {
                System.out.println("Ocorreu um erro: " + e.getMessage()); // "valor digitado inválido"
                System.out.println();
            }
            finally {
                teclado.close();
            }
         */
    }
}
