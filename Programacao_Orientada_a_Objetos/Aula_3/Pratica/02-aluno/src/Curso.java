public class Curso {
    String nome;
    double mensalidade;

    Curso (String nome, double mensalidade) {
        this.nome = nome;
        this.mensalidade = mensalidade;
    }

    void info () {
        System.out.println("Nome do curso: " + nome);
        System.out.printf("Mensalidade do curso: R$ %.2f \n", mensalidade);
    }
}
