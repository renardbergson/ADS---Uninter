package atividade;

public class Dolar extends Moeda {
	public Dolar (double valor) {
        super(valor);
        this.tipo = "Dólar";
    }

    @Override
    public void info() {
        super.info();
    }

    @Override
    public double converter () {
        return this.valor * 5.13; // cotação de 14/05/2024
    }
}