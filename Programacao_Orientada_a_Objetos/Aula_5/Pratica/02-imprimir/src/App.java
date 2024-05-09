/*  
    EXERCÍCIO 2
    Crie uma interface chamada "Imprimivel"
    A interface deve possuir um método imprimir, que imprima todos os atributos das classes
*/

public class App {
    public static void main(String[] args) {
        // (instanciar com referência)
        Imprimivel funcionario = new Funcionario("Renard Bergson", "111222333-44");
        funcionario.imprimir();

        // ou (instanciar com classe-filha)
        Carro carro = new Carro("Fiat", "Strada", "Preto", 3);
        carro.imprimir();

        // ou (instanciar e imprimir usando ponteiro)
        Passaro passaro = new Passaro("Beija-flor", "Azul-esverdeado");
        Imprimivel _passaro = passaro;
        _passaro.imprimir();
    }
}
