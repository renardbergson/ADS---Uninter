/*  
    Crie uma classe "Aluno" com atributos String "Nome" e "Curso". 
    Crie também um atributo referente à classe "Avaliacao". 
    Cada aluno deve ter uma Avaliacao asssociada. 
    Crie uma mensagem que imprima as informações completas desse aluno.
*/

public class App {
    public static void main(String[] args) throws Exception {
        Avaliacao notasRenard = new Avaliacao(7.9, 8.5, 9);
        Aluno renard = new Aluno("Renard Bergson", "ADS", notasRenard);

        // ou ...

        Aluno esdras = new Aluno("Esdras Medeiros", "ADS", new Avaliacao(7, 7.5, 8));

        renard.info();
        esdras.info();
    }
}
