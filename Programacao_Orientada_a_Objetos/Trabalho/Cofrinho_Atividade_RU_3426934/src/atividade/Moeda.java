package atividade;

enum Tipo {
	Real,
	Dólar,
	Euro,
}

public abstract class Moeda {
	Tipo tipo; // cada Moeda recebe 1 dos 3 estados possíveis do enum "Tipo", esse estado será definido por cada Classe derivada de Moeda em particular
	double valor;

	public Moeda(double valor) {
		this.valor = valor;
	}

	public void info() {
		System.out.println();

		switch (this.tipo) {
		case Real:
			System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'"
					+ Cofrinho.converter(Tipo.Real, this.valor) + "'" + " inserido no cofrinho");
			break;
		case Dólar:
			System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'"
					+ Cofrinho.converter(Tipo.Dólar, this.valor) + "'" + " inserido no cofrinho");
			break;
		case Euro:
			System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'"
					+ Cofrinho.converter(Tipo.Euro, this.valor) + "'" + " inserido no cofrinho");
			break;
		default:
			break;
		}

		System.out.println();
	}

	public abstract double converter();
}