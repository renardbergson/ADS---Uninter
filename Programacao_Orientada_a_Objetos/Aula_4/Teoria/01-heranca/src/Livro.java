public class Livro {
    public String titulo;
    public String autoria;
    public int numeroPaginas;
    public float custoProducao;
    public float precoVenda;
    
    // OPÇÃO 1 - Construtor Vazio
    /* 
        public Livro () {
            
        }
    */

    public Livro (String titulo, String autoria) {
        this.titulo = titulo;
        this.autoria = autoria;
    }

    public void mostrarTitulo () {
        System.out.println("Título do livro: " + titulo);
    }

    public float lucro () {
        return precoVenda - custoProducao;
    }

    public float imposto () {
        return 0.2f * lucro();
    }
}
