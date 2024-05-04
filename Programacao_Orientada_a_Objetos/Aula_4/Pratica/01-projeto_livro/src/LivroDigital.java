public class LivroDigital extends Livro {
    private int download;
    private String tamanho;
    
    public LivroDigital (String titulo, Autor autor, String genero, int edicao, int download, String tamanho) {
        super(titulo, autor, genero, edicao); // herdadas da classe-mãe
        setDownload(download);
        setTamanho(tamanho);
    }

    public void setDownload (int download) {
        this.download = download;
    }

    public void setTamanho (String tamanho) {
        this.tamanho = tamanho;
    }

    public int getDownload () {
        return download;
    }

    public String getTamanho () {
        return tamanho;
    }

    @Override // É uma boa prática. Indica que queremos sobrescrever um método vindo de uma superclasse. Previne erros de digitação, por exemplo: "infor" (dará erro)
    public void info () {
        super.info(); // obtemos as mesmas info da classe-mãe "Livro"
        System.out.println("Quantidade de downloads do livro digital: " + download); // informação nova
        System.out.println("Tamanho do livro digital: " + tamanho); // informação nova
    }
}
