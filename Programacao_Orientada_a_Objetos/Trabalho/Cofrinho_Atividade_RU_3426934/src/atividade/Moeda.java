package atividade;

import java.text.NumberFormat;
import java.util.Locale;

public abstract class Moeda {
	String tipo;
    double valor;

    public Moeda (double valor) {
        this.valor = valor;
    }

    public void info () {
        System.out.println();

        @SuppressWarnings("deprecation")
        Locale localBrasil = new Locale("pt", "BR");
        String valorEmReal = NumberFormat.getCurrencyInstance(localBrasil).format(this.valor);
        
        Locale localUsa = Locale.US;
        String valorEmDolar = NumberFormat.getCurrencyInstance(localUsa).format(this.valor);                
        
        Locale localEuropa = Locale.FRANCE;
        String valorEmEuro = NumberFormat.getCurrencyInstance(localEuropa).format(this.valor);                

        switch (this.tipo) {
            case "Real":
                System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'" + valorEmReal + "'" + " inserido no cofrinho");
                break;
            case "Dólar":
                System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'" + valorEmDolar + "'" + " inserido no cofrinho");
                break;
            case "Euro":
                System.out.println("+ Depósito da moeda " + "'" + this.tipo + "'" + ", de valor " + "'" + valorEmEuro + "'" + " inserido no cofrinho");
                break;
            default:
                break;
        }

        System.out.println();
    }

    public abstract double converter();
}