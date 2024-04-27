/*  
    COLLECTIONS
        - Importante API
        - Implementa diferentes estruturas de dados
        - Encapsuladas seguindo interfaces comuns

        SET - Conjunto
            A ordem dos elementos é irrelevante
            Não permite duplicação de itens (ao contrário do array)
        LIST - Lista
            Bem semelhante a um array (inclui o já usado "ArrayList")
            Um conjunto de dados dispostos em uma determinada ordem
        QUEUE - Fila
            Trabalha com sistema de prioridades
            O último elemento adicionado será o primeiro a ser tratado ou vice-versa
        MAP - Mapa
            Referencia os itens de forma não necessariamente númerica, como o Array
            Lembra os Objetos JS, pois implementa a estrutura: Chave x Valor
            Ex: a chave de acesso sendo uma String
                - Acessar na posição "Renard"...
                - Acessar na posição "Azul"...
    Métodos do COLLECTIONS que independem do objeto em si
        - sort(List)
        - shuffle(List, Random)
        - max(Collection, Comparator)
        - min(Collection, Comparator)
        - reverse(List)
*/

import java.util.ArrayList;
import java.util.Collections;

public class Lista {
    public static void main(String[] args) throws Exception {
        ArrayList<String> pessoas = new ArrayList<>();
        // LinkedList<String> pessoas = new LinkedList<>();
        
        pessoas.add("Renard");
        pessoas.add("Esdras");
        pessoas.add("Miguel");
        pessoas.add("Jailes");

        System.out.println("Orgem original:");
        System.out.println(pessoas);

        System.out.println();

        Collections.sort(pessoas);
        System.out.println("Ordem alfabética");
        System.out.println(pessoas);

        System.out.println();

        Collections.shuffle(pessoas);
        System.out.println("Disposição aleatória");
        System.out.println(pessoas);

        System.out.println();

        Collections.reverse(pessoas);
        System.out.println("Ordem reversa (do aleatório)");
        System.out.println(pessoas);

        System.out.println();
        System.out.println("Menor elemento por ordem alfabética:");
        System.out.println(Collections.min(pessoas));

        System.out.println();
        System.out.println("Maior elemento por ordem alfabética:");
        System.out.println(Collections.max(pessoas));
    }
}
