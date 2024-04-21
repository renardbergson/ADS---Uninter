import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Turma turma = new Turma();
        turma.nome = "Turma Alpha";

        turma.professor = new Professor();
        turma.professor.nome = "Girafalles";
        turma.professor.formacao = "Personagem do Chaves";
        turma.professor.cadastro = 404;

        turma.alunos = new ArrayList<Aluno>();
        turma.alunos.add(new Aluno());
        turma.alunos.get(0).nome = "Renard Bergson";
        turma.alunos.get(0).cpf = "000111222-33";
        turma.alunos.get(0).matricula = 1001;

        turma.alunos.add(new Aluno());
        turma.alunos.get(1).nome = "Esdras";
        turma.alunos.get(1).cpf = "111222333-44";
        turma.alunos.get(1).matricula = 1002;

        turma.info();
    }
}
