package atividade;

public class Euro extends Moeda {
	public Euro (double valor) {
        super(valor);
        this.tipo = "Euro";
    }

    @Override
    public void info() {
        super.info();
    }

    @Override
    public double converter () {
        return this.valor * 5.55; // cotação de 14/05/2024
    }
}