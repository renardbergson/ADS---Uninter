/*  
    EXERCÍCIO 1
    Crie uma classe abstrata "Computador" com 
        I - os atributos:
            * int gbMemoria
            * int numProcessadores
        II - Método abstrato 
            * calculaValor()
    Implemente duas classes filhas:
        I - Desktop
            Atributo:
                * double precoAcessorios;
            Método:
                * calculaValor() que retorna: gbMemoria * 200 + numProcessadores * 400 + acessorios
        II - Notebook
            Atributo:
                * int polegadasTela
            Método:
                * calculaValor() que retorna: gbMemoria * 250 + numProcessadores * 500 + polegadasTela * 100
    
    Instancie e aplique corretamente os conceitos de polimorfismo visto até aqui
    Armazene numa coleção todos os computadores, Desktops e Notebooks, a fim de calcular o valor total
    
*/

import java.util.ArrayList;

public class App {
    public static void main(String[] args) {
        Desktop desktop = new Desktop(32, 4, 600);
        Notebook notebook = new Notebook(8, 4, 15);

        Computador computador; // ponteiro
        // não estamos instanciando mas atribuindo, referenciando
            
        computador = desktop; // ponteiro
        System.out.printf("Preço do Desktop 1: R$ %.2f \n", computador.calculaValor());
        
        computador = notebook; // ponteiro
        System.out.printf("Preço do Notebook 1: R$ %.2f \n", computador.calculaValor());
        
        // lista geral
        ArrayList<Computador> listaComputadores = new ArrayList<Computador>();
        listaComputadores.add(desktop); // add 1
        listaComputadores.add(notebook); // add 2
        listaComputadores.add(new Desktop(16, 6, 720)); // add 3
        // perceba uma outra maneira de instanciar, são muitas possibilidades...
        
        double total = 0;
        for (Computador c : listaComputadores) { // para cada "Computador" c, na listaComputadores...
            total += c.calculaValor();
        }

        System.out.println();
        System.out.printf("Preço total dos computadores comprados: %.2f \n", total);
        

        // perceba o conceito de "ponteiro" implementado aqui, uma hora a variável "computador" APONTA para a variável "desktop", outra hora para a variável "notebook", assumindo naturalmente as particularidades dos objetos instanciados por elas. Esse costuma ser o exemplo mais clássico de polimorfismo.
    }
}
