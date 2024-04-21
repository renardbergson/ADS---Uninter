public class Carro {
    String nome;
    String modelo;
    float velocidade;

    static float minhasParaMetros(float milhas) {
        return milhas * 1600;
    }

    static final double PI = 3.1415;
    // a palavra "final" fará com que o valor de PI não possa ser alterado, caso contrário, podemos eliminá-la
}
