import java.util.ArrayList;

public class Cofrinho {
    private ArrayList<Moeda> moedas = new ArrayList<Moeda>();
    // tornamos o array privado, para que não seja acessível fora do método "adicionar"

    public void adicionar (Moeda moeda) {
        moedas.add(moeda);
    }

    public double calcularTotal () {
        double total = 0;

        for (Moeda m : moedas) {
            String nomeMoeda = m.getNome();
            double valorMoeda = m.getValor();

            if (nomeMoeda == "Real") {
                System.out.println("Um depósito da moeda 'real' foi encontrado");
                total += valorMoeda;
            } 
            else if (nomeMoeda == "Euro") {
                System.out.println("Um depósito da moeda 'euro' foi encontrado");
                total += valorMoeda * 5.47;
            } 
            else if (nomeMoeda == "Dólar") {
                System.out.println("Um depósito da moeda 'dólar' foi encontrado");
                total += valorMoeda * 5.11;
            }
        }

        return total;
    }
}
