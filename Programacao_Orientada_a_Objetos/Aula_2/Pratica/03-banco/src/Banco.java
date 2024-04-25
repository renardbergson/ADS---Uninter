/*  
    Crie uma classe "Conta", para administrar contas correntes de um banco. A classe deve ter as seguintes propriedades:

        int numero,
        String titular,
        double saldo,
        double limiteDiario,
    
    Crie os métodos:
        bool sacar(float)
        bool depositar(float)
        void info()

    * QUESTÃO 4
        Complemente o exercício anterior, criando um método "transferir", que receba uma conta destino e um valor
*/

public class Banco {
    public static void main(String[] args) throws Exception {
        Conta cliente1 = new Conta(111, "Renard Bergson", 2000, 500);
        cliente1.info();

        cliente1.sacar(501);
        cliente1.info();

        cliente1.sacar(500);
        cliente1.info();

        Conta cliente2 = new Conta(222, "Esdras Medeiros", 3200, 500);
        cliente2.info();

        cliente2.depositar(50);
        cliente2.info(); 

        // EXERCÍCIO 4
        cliente2.transferir(cliente1, 3200);
        cliente1.info();
        cliente2.info();
    }
}
