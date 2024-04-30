/*  
    HERANÇA
        Esse princípio permite que classes compartilhem atributos e métodos evitando retrabalho.
        Para herdar atributos de uma classe, usa-se a palavra reservada "extends", seguida do nome da classe mãe
    HERANÇA + CONSTRUTORES
        Suponhamos que neste sistema é vital que cada livro sempre receba "titulo" e "autoria"
        
        Ao estender uma classe, a classe herdeira não contemplará só os atributos e métodos mas também a Tipagem. Então, para não obter erros, neste caso, temos algumas opções:
        
        1 - Estabelecer um construtor vazio na classe mãe 
        2 - Representar o construtor original dentro da classe herdeira, através de um novo construtor, usando a palavra reservada "super"

    PALAVRAS RESERVADAS: SUPER x THIS
        É possível usar essas duas palavras ao evocar atributos ou métodos de nomes iguais, presentes tanto na classe mãe como na classe herdeira

        SUPER:
            I - Faz referência explícita à classe mãe
            II - Invoca o construtor da classe mãe
            III - deve estar na primeira linha
        THIS:
            I - Faz referência explícita ao próprio objeto/classe
            II - Utilizada para resolver ambiguidades de nome

    INSTANCEOF
        Ao estender uma classe, visto que a classe herdeira herda também a Tipagem da classe mãe, considera-se que a herdeira é também do tipo da classe mãe, ou seja, uma instância da classe mãe

*/

public class App {
    public static void main(String[] args) throws Exception {
        Livro livro = new Livro("POO com Java", "Renard");
        livro.mostrarTitulo();

        System.out.println();

        LivroDigital livroDigital = new LivroDigital("POO com Java", "Renard", "45 Mb");
        livroDigital.info();
        livroDigital.mostrarImpostos();

        System.out.println();

        System.out.println(livro instanceof Livro); // true
        System.out.println(livroDigital instanceof Livro); // true
        System.out.println(livro instanceof LivroDigital); // false
        System.out.println(livroDigital instanceof LivroDigital); // true
    }
}
