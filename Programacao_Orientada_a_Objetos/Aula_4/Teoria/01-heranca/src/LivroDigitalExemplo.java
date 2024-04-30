public class LivroDigitalExemplo {
    // Exemplo de classe com códigos duplicados, semelhante à classe geral "livro" (má prática)
    public String autoria;
    public String titulo;
    public int numeroPaginas;
    public float custoProducao;
    public float precoVenda;

    // NOVO
    public String linkDownload;
    public float tamanhoDoArquivo;
    //============================

    public void mostrarTitulo () {
        System.out.println("Título da Obra: " + titulo);
    }

    public float lucro () {
        return precoVenda - custoProducao;
    }

    // MUDOU
    public float imposto () {
        return 0.2f * lucro() + 2;
    }
    //========================
}
