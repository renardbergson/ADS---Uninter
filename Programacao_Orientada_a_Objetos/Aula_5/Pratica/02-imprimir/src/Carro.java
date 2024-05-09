public class Carro implements Imprimivel {
    String marca;
    String modelo;
    String cor;
    int numPortas;

    public Carro (String marca,  String modelo, String cor, int numPortas) {
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.numPortas = numPortas;
    }

    @Override
    public void imprimir () {
        System.out.println("Marca do Carro: " + marca);
        System.out.println("Modelo do Carro: " + modelo);
        System.out.println("Cor do Carro: " + cor);
        System.out.println("Número de portas do Carro: " + numPortas);
        System.out.println();
    } 
}
