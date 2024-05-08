package formas;
import java.util.Scanner;


public class Quadrado extends FormaGeometrica {
    @Override
    public double calcularArea () {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Digite a medida do lado do quadrado: ");
        double lado = teclado.nextDouble();
        area = lado * lado;
        teclado.close();
        return area;
    }
}
