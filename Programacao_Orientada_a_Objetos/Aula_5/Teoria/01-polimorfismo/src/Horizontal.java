// Exemplo de polimorfismo horizontal

public class Horizontal {
    public void fazAlgo () {
        System.out.println("Este é o método da superclasse");
    }

    public void fazAlgo (String mensagem) { // classe com mesmo nome, mas que recebe atributos
        System.out.println(mensagem);
    }
}
