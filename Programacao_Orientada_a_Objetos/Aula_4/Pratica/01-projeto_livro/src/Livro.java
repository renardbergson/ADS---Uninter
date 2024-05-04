public class Livro {
    private String titulo;
    private Autor autor;
    private String genero;
    private int edicao;

    public Livro (String titulo, Autor autor, String genero, int edicao) {
        setTitulo(titulo);
        setAutor(autor);
        setGenero(genero);
        setEdicao(edicao);
    }

    public void setTitulo (String titulo) {
        this.titulo = titulo;
    }

    public void setAutor (Autor autor) {
        this.autor = autor;
    }

    public void setGenero (String genero) {
        this.genero = genero;
    }

    public void setEdicao (int edicao) {
        this.edicao = edicao;
    }

    public String getTitulo () {
        return titulo;
    }

    public Autor getAutor () {
        return autor;
    }

    public String getGenero () {
        return genero;
    }

    public int getEdicao () {
        return edicao;
    }

    public void info () {
        System.out.println("Título do Livro: " + titulo);
        System.out.println("Gênero do Livro: " + genero);
        System.out.println("Edição do Livro: " + edicao);
        autor.info();
    }
}
