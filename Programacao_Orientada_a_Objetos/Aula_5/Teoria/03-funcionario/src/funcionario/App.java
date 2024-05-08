/*  
                                                    ********************
                                                    *    Assalariado   *
                ----------------------------------- ********************
                |                                   *  salario: Float  *
                |                                   ********************
                |
                ▽
    ********************                            ********************                          
    *    Funcionario   *                            *   Comissionado   *
    ********************                            ********************
    *   nome: String   *  ◁------------------------ *  comissao: float *
    *    pagamento()   *                            *   vendas: float  *
    ********************                            ********************
                △
                |
                |                                   ********************
                |                                   *     Horista      *
                ----------------------------------- ********************
                                                    *  totalHoras: int *
                                                    * valorHora: float *
                                                    ********************

    De forma genérica, todo funcionário vai ter um Nome e uma Forma de Pagamento
    - O Funcionário recebe seu salário
    - O Comissionaro calcula o valor da comissão vezes o total de vendas
    - O Horista calcula o total de horas trabalhadas pelo valor da hora
*/

package funcionario;

public class App {
    public static void main(String[] args) throws Exception {
        // veja que é possível instanciar "Funcionário" também com suas classes filhas
        // desta forma, é como se as classes filhas fossem parte da superclasse

        // EXEMPLO 1
        Funcionario f1 = new Assalariado("Funcionário Assalariado", 3800);
        System.out.println("Nome: " + f1.nome);
        System.out.println("Salário: " + f1.pagamento());
        System.out.println();

        f1 = new Horista("Funcionário Horista", 40, 25);
        System.out.println("Nome: " + f1.nome);
        System.out.println("Salário: " + f1.pagamento());
        System.out.println();
        /*  
            perceba que a variável "f1" hora é uma instância de "Assalariado", hora é uma instância de "Horista", hora é uma instância de "Comissionado", esse é o conceito de múltiplas formas, polimorfismo
        */


        // EXEMPLO 2
        Funcionario funcionarios[] = {
            new Assalariado("Renard", 3800),
            new Horista("Esdras", 40, 35.50f),
            new Comissionado("Asriel", 62, 15)
        };

        float total = 0;
        for (int i = 0; i < funcionarios.length; i++) {
            System.out.println("Nome: " + funcionarios[i].nome);
            System.out.println("Salário: " + funcionarios[i].pagamento());
            
            total += funcionarios[i].pagamento();
            
            System.out.println();
        }
        System.out.println("Total da folha de pagamentos: " + total);

        /*  
            Perceba que, através de uma só instância da superclasse "Funcionário" estamos conseguindo inserir objetos de diferentes, através das suas classes-filhas, dentro de um mesmo array e acessá-los da mesma maneira.
        */
    }
}
