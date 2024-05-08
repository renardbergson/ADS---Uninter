package funcionario;

// Esta classe é o nosso ponto de partida genérico
public class Funcionario {
    String nome;

    public Funcionario (String nome) {
        this.nome = nome;
    }

    public float pagamento () {
        System.out.println("Processando pagamento...");
        return 0.0f;
    }

    // perceba que não faz muito sentido ter um método pagamento retornando zero
}
