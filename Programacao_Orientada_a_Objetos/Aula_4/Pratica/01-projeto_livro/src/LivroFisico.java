public class LivroFisico extends Livro {
    private int tiragem;
    private String peso;
    
    public LivroFisico (String titulo, Autor autor, String genero, int edicao, int tiragem, String peso) {
        super(titulo, autor, genero, edicao); // herdadas da classe-mãe
        setTiragem(tiragem);
        setPeso(peso);
    }

    public void setTiragem (int tiragem) {
        this.tiragem = tiragem;
    }

    public void setPeso (String peso) {
        this.peso = peso;
    }

    public int getTiragem () {
        return tiragem;
    }

    public String getPeso () {
        return peso;
    }

    @Override // É uma boa prática. Indica que queremos sobrescrever um método vindo de uma superclasse. Previne erros de digitação, por exemplo: "infor" (dará erro)
    public void info () {
        super.info(); // obtemos as mesmas info da classe-mãe "Livro"
        System.out.println("Tiragem do livro físico: " + tiragem); // informação nova
        System.out.println("Peso do livro físico: " + peso); // informação nova
    }
}
