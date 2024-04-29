public class Aluno {
    String nome;
    int matricula;
    double desconto;
    Curso curso;

    Aluno (String nome, int matricula, double desconto, Curso curso) {
        this.nome = nome;
        this.matricula = matricula;
        this.desconto = desconto;
        this.curso = curso;
    }

    void info () {
        System.out.println("Nome do aluno: " + nome);
        System.out.println("Matrícula do aluno: " + matricula);
        System.out.printf("Desconto do aluno: %.0f por cento \n", desconto);
        curso.info();
        System.out.printf("Total a pagar COM DESCONTO: R$ %.2f \n", pagamento());
    }
    
    double pagamento () {
        double descontar = (desconto / 100) * curso.mensalidade;
        double valorPagar = curso.mensalidade - descontar;
        return valorPagar;
    }
}
