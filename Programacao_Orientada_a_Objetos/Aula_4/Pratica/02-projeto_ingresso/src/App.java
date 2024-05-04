/*  
    EXERCÍCIO 2

    Construa um código, com base no diagrama UML a seguir:

    ****************************                            ****************************
    *         Ingresso         *                            *       IngressoVip        *
    ****************************                            ****************************
    *   + nomeEvento: String   * ◁------------------------- *    + adicional: double   *
    *      + valor: double     *                            ****************************
    ****************************                            *         + info ()        *
    *         + info ()        *                            ****************************
    ****************************

    A seta fechada indica herança da classe "IngressoVip" para a classe "Ingresso"
    + Indica a existência de atributos ou métodos públicos
*/

public class App {
    public static void main(String[] args) throws Exception {
        Ingresso ig = new Ingresso("Rock in Rio", 300);
        System.out.println();
        ig.info();

        IngressoVip iv = new IngressoVip("Rock in Rio VIP", 300, 450);
        System.out.println();
        iv.info();
        System.out.println();
    }
}
