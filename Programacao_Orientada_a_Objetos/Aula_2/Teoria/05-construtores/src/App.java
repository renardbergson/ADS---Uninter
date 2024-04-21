/*  
    CONSTRUTORES
        Código que executa no momento da instanciação
        Se não for criado, internamente já existe um construtor vazio
        Semelhante a um método
        Não tem valor retorno
        Não pode ser invocado ser sem durante a instanciação

    A fim de melhorar o cõdigo do pacote 04, podemos usar um Construtor na classe "Aluno".
    Desta forma, será possível adicionar um aluno na classe principal "App", usando apenas uma linha.
*/

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
        turma.alunos.add(new Aluno("Renard Bergson", "000111222-33", 1001));

        turma.alunos.add(new Aluno("Esdras Medeiros", "111222333-44", 1002));

        turma.info();
    }
}
