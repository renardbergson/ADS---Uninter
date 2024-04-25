public class Conta {
    int numero;
    String titular;
    double saldo;
    double limiteSaque;

    Conta (int numero, String titular, double saldo, double limiteSaque) {
        this.numero = numero;
        this.titular = titular; 
        this.saldo = saldo;
        this.limiteSaque = limiteSaque;
    }

    boolean sacar (double valor) {
        if (valor > saldo || valor > limiteSaque || valor <= 0) {
            System.out.println("SAQUE NÃO AUTORIZADO!");
            System.out.println("Verifique seu saldo, seu limite diário ou o valor inserido.");
            System.out.println();
            return false;
        }
        
        System.out.println("OPERAÇÃO DE SAQUE REALIZADA COM SUCESSO");
        System.out.println("Valor retirado: " + valor);
        System.out.println();
        saldo -= valor; // saldo = saldo - valor
        limiteSaque -= valor; // limiteSaque = limiteSaque - valor
        return true;
    }

    // EXERCÍCIO 4
    boolean depositar (double valor) {
        if (valor <= 0) {
            System.out.println("DEPÓSITO NÃO AUTORIZADO!");
            System.out.println("Verifique o valor inserido.");
            System.out.println();
            return false;
        }
        
        System.out.println("OPERAÇÃO DE DEPÓSITO REALIZADA COM SUCESSO");
        System.out.println("Valor inserido: " + valor);
        System.out.println();
        saldo += valor; // saldo = saldo - valor
        return true;
    }

    boolean transferir (Conta cliente, double valor) {
        if (valor <= 0 || valor > saldo) {
            System.out.println("TRANSFERÊNCIA NÃO AUTORIZADA!");
            System.out.println("Saldo insuficiente ou conta destino inválida.");
            System.out.println();
            return false;
        }

        cliente.saldo += valor; // conta destino
        this.saldo -= valor; // conta origem
        
        System.out.println("OPERAÇÃO DE TRANSFERÊNCIA REALIZADA COM SUCESSO");
        System.out.println("    Origem:");
        System.out.println("    Nome: " + this.titular);
        System.out.println("    Número da Conta: " + this.numero);
        System.out.println("    Valor transferido: R$ " + valor);
        
        System.out.println();

        System.out.println("    Destino:");
        System.out.println("    Nome: " + cliente.titular);
        System.out.println("    Número da Conta: " + cliente.numero);

        System.out.println();

        return true;
    }

    void info () {
        System.out.println("EXTRATO:");
        System.out.println("    Nome do cliente: " + titular);
        System.out.println("    Número da conta: " + numero);
        System.out.println("    Saldo: R$ " + saldo);
        System.out.println("    Limite de saque para hoje: R$ " + limiteSaque);
        System.out.println();
    }
}
