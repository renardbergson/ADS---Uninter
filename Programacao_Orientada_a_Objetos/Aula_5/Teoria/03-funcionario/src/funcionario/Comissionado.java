package funcionario;

public class Comissionado extends Funcionario {
    int vendas;
    float comissao;

    public Comissionado (String nome, int vendas, float comissao) {
        super(nome);
        this.vendas = vendas;
        this.comissao = comissao;
    }

    public float pagamento () {
        return vendas * comissao;
    }
}
