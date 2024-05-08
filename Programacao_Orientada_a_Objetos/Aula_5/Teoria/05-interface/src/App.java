/*  
    INTERFACE
        De modo geral, uma subclasse só pode ter UMA superclasse, ou seja, não é possível uma classe ter várias heranças. Para resolver essa demanda, existe o conceito de Interface, que é bem semelhante ao de uma Classe Abstrata.

        - As superclasses são estendidas (extends)
        - As interfaces são implementadas (implements)
        - Uma classe pode implementar mais de uma interface
        - Numa Interface os MÉTODOS são ABSTRATOS e os ATRIBUTOS são ESTÁTICOS

*/

public class App {
    public static void main(String[] args) {
        Animal animal = new Gato();
        Animal gato = new Gato();
        // ambas as formas são permitidas
        
        animal.dormir();
        animal.emitirSom();

        System.out.println();

        gato.dormir();
        gato.emitirSom();
    }
}