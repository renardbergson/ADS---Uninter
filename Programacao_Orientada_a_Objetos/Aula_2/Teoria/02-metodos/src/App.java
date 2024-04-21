public class App {
    public static void main(String[] args) throws Exception {
        // perceba a repetição de código em "classes e atributos", ao instanciar um novo objeto da classe "Aluno", o que pode ser resolvido através da criação de um método dentro dessa classe
        Aluno a = new Aluno();
        a.nome = "Renard Bergson";
        a.cpf = "000111222-33";
        a.matricula = 1001;
        a.info(); // método criado

        Aluno b = new Aluno();
        b.nome = "Esdras Medeiros";
        b.cpf = "111222333-44";
        b.matricula = 1002;
        b.info(); //método criado
    }
}
