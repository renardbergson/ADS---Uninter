public class Funcionario implements Imprimivel {
    String nome;
    String cpf;

    public Funcionario (String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    @Override
    public void imprimir () {
        System.out.println("Nome do Funcionário: " + nome);
        System.out.println("CPF do Funcionário: " + cpf);
        System.out.println();
    }
}
