public class Aluno {
    int matricula;
    String nome;
    String cpf;

    // usa-se "void" quando a intenção não é retornar alguma coisa
    // usa-se "void" quando a intenção é apenas alterar valores dos atributos de um objeto
    void info() {
        System.out.println("Nome: " + nome);
        System.out.println("Cpf: " + cpf);
        System.out.println("Matrícula: " + matricula);
        System.out.println();
    }
}
