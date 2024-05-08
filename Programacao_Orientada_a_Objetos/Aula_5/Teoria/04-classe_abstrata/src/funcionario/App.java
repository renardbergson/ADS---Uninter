/*  
    CLASSE ABSTRATA
    - É uma classe que não desejamos instanciar
    - Permite métodos abstratos que não desejamos implementar
    - Útil para utilização em superclasses

    Usando esse conceito, como podemos melhorar a implementação da superclasse "Funcionário", do mesmo exemplo anterior? 
    Por exemplo, qual o sentido em ter o pagamento() de um "Funcionário" sem especificar qual tipo de funcionário? 
    O método pagamento() em "Funcionário" deve estar presente apenas para fazer uma marcação de que há pagamento, mas a implementação desse método deve ser feita através das classes filhas.
*/

package funcionario;

public class App {
    public static void main(String[] args) {
    /*          
        Classes abstratas NÃO podem ser instanciadas por si só!

        ❌ Funcionario f1 = new Funcionario("Funcionário Padrão");
        ❌ System.out.println("Nome: " + f1.nome);
        ❌ System.out.println("Salário: " + f1.pagamento()); 
    */

    Funcionario f1 = new Assalariado("Funcionário Assalariado", 3500);
    System.out.println(f1.nome);
    System.out.println(f1.pagamento());
    }
}
