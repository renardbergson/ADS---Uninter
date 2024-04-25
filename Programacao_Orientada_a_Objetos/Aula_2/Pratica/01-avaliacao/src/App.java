/*  
    Cria uma classe AVALIACAO, com 3 atributos chamados nota1, nota2, nota3, e crie dois métodos para calcular e retornar diferentes tipos de média:

    I - Média aritmética (a soma de N numeros dividido pela quantidade de N)
    II - Média ponderada (cada N multiplicado pelo seu peso, depois a soma de N multiplicado pela soma dos pesos.) 
        Nota1 = peso 2
        Nota2 = peso 3
        Nota3 = peso 4
*/

public class App {
    public static void main(String[] args) throws Exception {
        Avaliacao renard = new Avaliacao(7.5, 8.2, 6);

        System.out.printf("A média aritmética de Renard foi: %.2f \n", renard.mediaAritmetica());
        System.out.printf("A média ponderada de Renard foi: %.2f", renard.mediaPonderada());
    }
}
