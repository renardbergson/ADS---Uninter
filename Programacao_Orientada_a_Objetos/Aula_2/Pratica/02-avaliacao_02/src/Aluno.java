public class Aluno {
    String nome;
    String curso;
    Avaliacao avaliacao;

    Aluno (String nome, String curso, Avaliacao notas) {
        this.nome = nome;
        this.curso = curso;
        this.avaliacao = notas;
    }

    void info () {
        System.out.println("Nome do aluno: " + nome);
        System.out.println("Curso do aluno: " + curso);
        System.out.printf("Média aritmética do aluno: %.1f \n", avaliacao.mediaAritmetica());
        System.out.printf("Média ponderada do aluno: %.1f \n", avaliacao.mediaPonderada());
        System.out.println();
    }
}
