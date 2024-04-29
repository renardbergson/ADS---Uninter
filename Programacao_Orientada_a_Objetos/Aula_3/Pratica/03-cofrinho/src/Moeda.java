public class Moeda {
    private String nome;
    private double valor;

    Moeda (String nome, double valor) {
        setNome(nome, valor);
    }

    public void setNome (String nome, double valor) {
        if (nome != "Dólar" && nome != "Euro" && nome != "Real") {
            System.out.println("Valor para a moeda" + " " + "'" + nome + "'" + " " + "não inserido!");
            System.out.println("Insira moedas do tipo: Dólar, Euro ou Real");
            System.out.println();
            return;
        }

        this.nome = nome;
        setValor(valor);
    }

    public void setValor (double valor) {
        this.valor = valor;
    }

    public String getNome () {
        return nome;
    }

    public double getValor () {
        return valor;
    }
}
