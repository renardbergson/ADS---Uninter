/*  
    Escreva o código, com base no diagrama UML a seguir:

    *********************************               *********************************
    *              MOEDA            *               *           COFRINHO            *
    *********************************               *********************************
    *       - valor: double         *   <---------  *  + adicionar(m: Moeda) : void *
    *       - nome: String          *               *  + calcularTotal() : double   * 
    *********************************               *********************************
    * + Moeda(v: double, n: String) *               
    *     + setNome() : String      *
    *     + setValor() : double     *
    *     + getNome() : String      *
    *     + getValor() : double     *
    *********************************

    Opcional:
        Adicione verificações e conversões para as moedas Euro, Dólar e Real

    Relembrando:
        Parte de cima = nome da classe
        Parte do meio = atributos
        Parte de baixo = construtores, métodos...
        - significa = atributo/método privados
        + significa = atributo/método públicos
*/  

import java.text.NumberFormat;
import java.util.Locale;

public class App {
    public static void main(String[] args) throws Exception {
         Cofrinho cofre = new Cofrinho();

        cofre.adicionar(new Moeda("Real", 2.50));
        cofre.adicionar(new Moeda("Euro", 25));
        cofre.adicionar(new Moeda("Dólar", 8.20));
        cofre.adicionar(new Moeda("Teste", 7.25));

        @SuppressWarnings("deprecation")
        Locale localBrasil = new Locale("pt", "BR");
        String totalEmReais = NumberFormat.getCurrencyInstance(localBrasil).format(cofre.calcularTotal());

        System.out.println();
        System.out.println("O total do cofre em reais equivale a aproximadamente: " + totalEmReais);
    }
}
