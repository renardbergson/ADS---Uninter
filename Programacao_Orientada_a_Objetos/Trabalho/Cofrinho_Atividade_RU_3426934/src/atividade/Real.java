package atividade;

public class Real extends Moeda {
	public Real (double valor) {
        super(valor);
        this.tipo = Tipo.Real;
    }

    @Override
    public void info() {
        super.info();
    }

    @Override
    public double converter () {
        return this.valor; // sem conversão
    }
}