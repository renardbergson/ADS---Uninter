/*
    neste exemplo, usaremos polimorfismo para aplicar o conceito de que quairamos calcular a área de determinadas figuras geométricas, sabendo que cada figura tem um cálculo diferente
*/

package formas;

public class App {
    public static void main (String[] args) {
        FormaGeometrica quadrado = new Quadrado();
        System.out.println("A área do quadrado é igual a: " + quadrado.calcularArea());
    }
}
