package atividade;

public abstract class Moeda {
	String tipo;
    double valor;

    public Moeda (double valor) {
        this.valor = valor;
    }

    public void info () {
        System.out.println();              

        switch (this.tipo) {
            case "Real":
                System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'" + Cofrinho.converter("Real", this.valor) + "'" + " inserido no cofrinho");
                break;
            case "Dólar":
                System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'" + Cofrinho.converter("Dólar", this.valor) + "'" + " inserido no cofrinho");
                break;
            case "Euro":
                System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'" + Cofrinho.converter("Euro", this.valor) + "'" + " inserido no cofrinho");
                break;
            default:
                break;
        }

        System.out.println();
    }

    public abstract double converter();
}