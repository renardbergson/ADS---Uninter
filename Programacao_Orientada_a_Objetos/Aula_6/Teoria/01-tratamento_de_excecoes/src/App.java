/*  
    ERROS x EXCEÇÕES

    Erro
        - problema que ocorre em tempo real de execução
        - geralmente associado ao sistema operacional
        - são situações em que comumente não há muito o que fazer, além de fechar o programa
        Ex: tentar instanciar um objeto (alocar memória) e não ter mais memória disponível. Esse cenário geraria um erro do tipo "java.lang.OutOfMemoryError". 
    EXCEÇÃO
        - geralmente é um comportamento imprevisível apenas
        - são situações comumente contornáveis
        - erros que não precisam necessariamente de encerrar o programa
        Ex: tentar escrever uma mensagem dentro de um arquivo de texto e, na hora de escrever, por algum motivo, o arquivo não existe.
        Ex: "Arquivo não existe...", "Tente novamente..."

*/

public class App {
    public static void main(String[] args) throws Exception {
        int[] numeros = {1, 2, 3};
        
        // System.out.println(numeros[10]);
        // a linha de código anterior, por sí só, gera o erro de exceção: java.lang.ArrayIndexOutOfBoundsException
        // o tratamento a seguir impede que o programa encerre sozinho

        /*         
            try {
                System.out.println(numeros[10]);
            } catch (Exception e) { 
                System.out.println("Ops, ocorreu um erro: " + e.getMessage());
            } 

            assim, tratamos qualquer tipo de exceção
        */

        // ou...
        
        try {
            numeros[0] = numeros[0] / 0; // exceção por erro aritmético (dividir 0 por 0)
        }
        catch (ArithmeticException e) { // exceção 1
            System.out.println();
            System.out.println("Não é possível dividir por zero!");
            System.out.println();
        }

        try {
            System.out.println(numeros[10]); // exceção por erro de posição
        } 
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Ops, posição digitada fora do limite.");
            System.out.println();
        }

        catch (Exception e) { // qualquer tipo de exceção
            System.out.println("Ocorreu um problema desconhecido.");
            System.out.println();
        }
        finally { // código que sempre será executado
            System.out.println("Finalizando o programa...");
            System.out.println();
        }
    }
}