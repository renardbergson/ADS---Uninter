/*  
    ITERATOR
        É uma forma "genérica" de passear pelos elementos de uma coleção
        Mesmo para iterar diferentes estruturas, é possível fazer isso de forma quase genérica
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class App {
    public static void main(String[] args) throws Exception {
        ArrayList<Integer> lista = new ArrayList<>();
        HashSet<Integer> conjunto = new HashSet<>();
        HashMap<String, Integer> mapa = new HashMap<>();
        
        // Nos exemplos abaixo, a intenção é passar por todos os elementos e somá-los
        // LAÇO FOR
        int soma = 0;
        for (int i = 0; i < lista.size(); i++) {
            soma += lista.get(i);
        }

        // LAÇO FOR EACH - "para cada item dentro da lista"
        soma = 0;
        for (int item : lista) {
            soma += item;
        }

        // USANDO ITERATOR PARA TODOS OS CASOS
        // Iterator item = mapa.keySet().iterator(); // itera as chaves
        // Iterator item = mapa.entrySet().iterator(); // itera os valores
        Iterator item = lista.iterator();

        soma = 0;
        while (item.hasNext()) { // existe um próximo? Se sim...
            soma += (int)item.next(); // type cast - classificamos o valor que o iterator obterá
        }
    }
}
