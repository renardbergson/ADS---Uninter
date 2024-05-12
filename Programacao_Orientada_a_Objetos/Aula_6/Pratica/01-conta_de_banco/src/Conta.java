public class Conta {
    String nome;
    double saldo;

    public Conta (String nome, double saldo) {
        this.nome = nome;
        this.saldo = saldo;
    }

    public void depositar (double valor) throws Exception {
        // poderíamos tratar das exceções aqui dentro do método, mas não faz muito sentido
        // então, indicamos que o método "sacar" pode lançar exceção/exceções (throws exception)
        // assim, QUEM CHAMAR este método pode RELANÇAR ou trata as exceções
        // * para que funcione, é importante retirar a declaração "throws exception" da classe responsável
        // note que o método "depositar" lança EXCEÇÕES mesmo, de forma genérica
        // podemos criar uma classe para tratar da exceção e lançá-la, ao invés de generalizar

        if (valor <= 0) {
            // exceção
            System.out.println();
            System.out.println("-----------DEPÓSITO----------");    
            throw new Exception("❌ Valor inválido! (Tratado por exceção genérica)");
        }

        System.out.println();
        System.out.println("-----------DEPÓSITO----------");
        System.out.println("Conta alvo: " + nome);
        System.out.println("Valor depositado: " + valor);
        
        saldo += valor;
    }

    public void sacar (double valor) throws SaldoInsuficiente, ValorInvalido {
        if (valor > saldo) {
            // exceção
            System.out.println();
            System.out.println("-----------SAQUE----------");
            throw new SaldoInsuficiente();
            
        }
        
        if (valor <= 0) {
            // exceção
            System.out.println();
            System.out.println("-----------SAQUE----------");
            throw new ValorInvalido();
            
        }

        System.out.println();
        System.out.println("-----------SAQUE----------");
        System.out.println("Conta alvo: " + nome);
        System.out.println("Valor retirado: " + valor);
        
        saldo -= valor;
    }

    public void transferir (double valor, Conta destino) throws SaldoInsuficiente, ValorInvalido {
        /*  
            CÓDIGO IDEAL:

            - this.sacar(valor);
            - destino.depositar(valor);

            mas, neste caso, as mensagens teriam que ser administradas pela Classe Principal
        */

        if (valor > this.saldo) {
            // exceção
            System.out.println();
            System.out.println("-----------TRANSFERÊNCIA----------");
            throw new SaldoInsuficiente();
        }

        if (valor <= 0) {
            // exceção
            System.out.println();
            System.out.println("-----------TRANSFERÊNCIA----------");
            throw new ValorInvalido();
        }

        System.out.println();
        System.out.println("-----------TRANSFERÊNCIA----------");
        System.out.println("Pagador: " + this.nome);
        System.out.println("Recebedor: " + destino.nome);
        System.out.println("Valor transferido: " + valor);
        
        this.saldo -= valor;
        destino.saldo += valor;
    }

    public void info () {
        System.out.println();
        System.out.println("-----------EXTRATO----------");
        System.out.println("Titular: " + nome);
        System.out.println("Saldo: " + saldo);
    }
}
