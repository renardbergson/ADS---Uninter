/*  
    ENUMERADOR
        Não é um tema diretamente ligado ao conceito de polimorfismo, mas é pertinente a esta aula.
        
        - É um tipo especial de classe
        - Para implementá-lo, usa-se a palavra "enum"
        - Serve para representar constantes enumeradas
        - É um conceito existente em diversas linguagens
        - Ajuda a deixar o código mais legível e organizado
        - Ajuda a evitar erros de digitação
*/

public class App {
    public static void main(String[] args)  {
        /*  ❌
            Roupa roupa = new Roupa("Camisa", 3, 3);
            roupa.mensagem(); 
        */

        Roupa roupa = new Roupa("Camisa", 3, Estacao.outono);
        roupa.mensagem();
    }
}
