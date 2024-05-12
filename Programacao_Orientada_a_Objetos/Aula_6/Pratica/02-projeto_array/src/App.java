/*  
    EXERCÍCIO 2
    
    Escreva um método que: 
    - Receba um inteiro "n" por parâmetro 
    - Retorne uma instância para um vetor (Array) de "n" posições de inteiros
    - Trate a exceção "NegativeArraySizeException" (quando "n" for um valor negativo)
*/

import javax.management.RuntimeErrorException;

public class App {
    public static int[] instanciaArray (int n) {
        return new int[n]; // retorne um novo array de inteiros de tamanho N
    }
    
    public static void main(String[] args) {
        int arr[]; // ou "int arr[] = null;" (ponteiro vazio) - Caso o loop esteja fora do try! 
        int tamanho;
        
        // TESTE 1 (exceção pedida no exercício)
        tamanho = -5;

        // TESTE 2 (exceção criada / aprimorada por nós)
        // tamanho = 0;

        // TESTE 3 (tudo certo)
        // tamanho = 10;

        try {
            if (tamanho != 0) {
                arr = instanciaArray(tamanho);
    
                for (int i = 0; i < arr.length; i++) { // ou < tamanho
                    System.out.println(arr[i]);
                }
                
                return;
            }

            throw new RuntimeErrorException(null);
        } 
        catch (NegativeArraySizeException e) {
            System.out.println("❌ Não é possível criar um array de posições negativas!");
        }
        catch (Exception e) { // trata todas as demais exceções não especificadas
            System.out.println("❌ O tamanho deve ser diferente de zero!");
        }
    }
}