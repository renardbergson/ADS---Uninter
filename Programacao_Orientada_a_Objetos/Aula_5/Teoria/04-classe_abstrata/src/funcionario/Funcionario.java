package funcionario;

// Esta classe é o nosso ponto de partida genérico
// Tornamos ela  e seus atributos abstratos, através da palavra "abstract"
// Métodos abstratos não necessitam ter um corpo

public abstract class Funcionario {
    String nome;

    public Funcionario (String nome) {
        this.nome = nome;
    }

    public abstract float pagamento();
    // agora não precisamos mais inventar uma implementação sem sentido, só para que exista o método pagamento
}
