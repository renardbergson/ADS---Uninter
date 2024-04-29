/*  
    EXERCCÍCIO 1
        Crie uma Classe "Nota"
            Dois atributos privados:
                double nota1
                double nota2
            Cinco métodos públicos:
                void setNota1(double)
                void setNota2(double)
                double getNota1()
                double getNota2()
                void resultado()

                O método "resultado" deve imprimir a média, dizendo se o aluno está aprovado, reprovado ou na final.
                Utilize GET e SET
    EXERCÍCIO 2
        Adicione um atributo "faltas". No método "resultado", imprima "reprovado por faltas", se o aluno tiver acima de 7 faltas. 
        Adicione um construtor que faça uso dos GET e SET
*/

public class App {
    public static void main(String[] args) throws Exception {
        Nota renard = new Nota();
        renard.setNota1(7.6);
        renard.setNota2(9.2);
        renard.setFaltas(3);
        renard.resultado();

        Nota esdras = new Nota(9, 6.9, 8);
        esdras.resultado();
    }
}
