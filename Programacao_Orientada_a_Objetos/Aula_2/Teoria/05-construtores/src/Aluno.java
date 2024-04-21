public class Aluno {
    int matricula;
    String nome;
    String cpf;

    Aluno (String nome, String cpf, int matricula) {
        this.nome = nome;
        this.cpf = cpf;
        this.matricula = matricula;
        // a palavra THIS serve para fazer referência explícita à classe "Aluno"
    }

    void info() {
        System.out.println("Matrícula: " + matricula);
        System.out.println("Nome: " + nome);
        System.out.println("Cpf: " + cpf);  
        System.out.println();  
    }
}
