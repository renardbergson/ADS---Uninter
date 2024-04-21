/*  
    Padrões de Nomenclatura no JAVA:
        Pacotes: são escritos inteiramente em letra minúscula
        Classes: inicia com letra maiúscula e segue o camel case
        Métodos, Atributos e Variáveis: inicia com letra minúscula e segue o camel case
        Constantes: inteiramente com letras maiúsculas, separadas por underline

    Usar o comando STATIC
        I - Antes de um método:
            O método pode ser executado sem ser necessário instanciar o objeto de origem
        II - Antes de um atributo:
            O atributo vira uma espécie de variável global, podendo ser acessada por todas as instâncias
*/

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("10 milhas em metros equivale a " + Carro.minhasParaMetros(10) + "metros");

        System.out.println();

        System.out.println("O valor de PI equivale a: " + Carro.PI);
        // não foi necessário instanciar a classe "Carro" para acessar o método e a variável acima
    }
}
