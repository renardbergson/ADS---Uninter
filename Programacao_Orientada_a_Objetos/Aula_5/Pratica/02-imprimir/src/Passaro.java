public class Passaro implements Imprimivel {
    String especie; // beija-flor
    String cor; // azul esverdeado

    public Passaro (String especie, String cor) {
        this.especie = especie;
        this.cor = cor;
    }

    public void imprimir () {
        System.out.println("Espécie do Pássaro: " + especie);
        System.out.println("Cor do Pássaro: " + cor);
        System.out.println();
    }
}
