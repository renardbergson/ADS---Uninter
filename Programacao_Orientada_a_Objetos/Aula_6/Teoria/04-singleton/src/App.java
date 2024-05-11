/*  
    SINGLETON

    O Singleton é um padrão de projeto criacional que permite a você garantir 
    que uma classe tenha apenas UMA INSTÂNCIA, enquanto provê UM PONTO DE ACESSO GLOBAL 
    para essa instância.
*/

public class App {
    public static void main(String[] args) throws Exception {
        // ❌ Singleton s1 = new Singleton();
        Singleton s1 = Singleton.getInstance();
        Singleton s2 = Singleton.getInstance();
        
        // EXEMPLO 1
        s1.numero += 10; // 20 + 10 = 30
        System.out.println(s1.numero);
        System.out.println(s2.numero);

        System.out.println();

        // EXEMPLO 2
        s2.numero += 20;
        System.out.println(s1.numero);
        System.out.println(s2.numero);

        /*  
            Perceba que, mesmo chamando "getInstance" em outras Classes, em outros contextos: 
                I - Sempre retornará a mesma instância
                II - Uma modificação feita em uma chamada / instância valerá para todas as outras
        */
    }
}
