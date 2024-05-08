// Exemplo de polimorfismo vertical, usando "Horizontal" como superclasse

public class Vertical extends Horizontal {
    // sobrescrita do método fazAlgo da classe-mãe
    @Override
    public void fazAlgo () {
        System.out.println("Este método 'fazAlgo' foi sobrescrito");
    }
}
