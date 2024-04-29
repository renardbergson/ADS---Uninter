/*  
    Crie uma classe "Aluno", que deve conter:
        ATRIBUTOS:
            String nome;
            int matricula;
            double desconto;
            Curso curso; (outra classe)
        MÉTODOS:
            info()
            pagamento() (informa o preço que o aluno paga, considerando seu desconto e o preço do curso)
    A classe "Curso", que deve conter:
        ATRIBUTOS:
            String nome;
            double mensalidade;
        MÉTODOS:
            info()
    
*/

public class App {
    public static void main(String[] args) throws Exception {
        Aluno renard = new Aluno("Renard Bergson", 111, 10, (new Curso("ADS", 1500)));
        renard.info();
    }
}
