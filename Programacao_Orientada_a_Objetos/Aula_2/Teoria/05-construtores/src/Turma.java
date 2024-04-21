import java.util.ArrayList;

public class Turma {
    String nome;
    Professor professor; // o objeto "professor" faz referência à classe criada: "Professor"
    ArrayList<Aluno> alunos; // o objeto "alunos" faz referência ao ArrayList da classe criada: "Aluno"

    void info() {
        System.out.println("Nome da turma: " + nome);
        System.out.println();
        
        System.out.println("Nome do professor: " + professor.nome);
        System.out.println("Formação do professor: " + professor.formacao);
        System.out.println("Cadastro do professor: " + professor.cadastro);
        System.out.println();

        System.out.println("Alunos: ");
        for (int i = 0; i < alunos.size(); i++) {
            System.out.println(" " + alunos.get(i).nome);
            System.out.println(" " + alunos.get(i).cpf);
            System.out.println(" " + alunos.get(i).matricula);
            System.out.println();
        }
    }
}
