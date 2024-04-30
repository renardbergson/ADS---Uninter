public class LivroDigital extends Livro {
    // agora, os atributos e métodos de "Livro" estarão disponíveis aqui também
    // apenas reescreve-se o que for diferente e/ou acrescenta-se o que for novo

    // OPÇÃO 2 - Referenciar construtor da classe mãe
    public LivroDigital (String titulo, String autoria, String tamanho) {
        super (titulo, autoria); // "super", param originais
        this.tamanhoDoArquivo = tamanho; // podemos adicionar novos param no novo construtor
    }

    // NOVO
    public String linkDownload;
    public String tamanhoDoArquivo;

    void info () {
        System.out.println("Título do livro digital: " + titulo);
        System.out.println("Autoria: " + autoria);
        System.out.println("Tamanho: " + tamanhoDoArquivo);
    }

    // super x this
    void mostrarImpostos () {
        System.out.println();
        System.out.println("Imposto do livro físico: " + super.imposto()); // classe mãe
        System.out.println("Imposto do livro digital: " + this.imposto()); // esta classe ("this" opcional)
    }
    //============================

    // MUDOU
    public float imposto () {
        return super.imposto() + 2; // imposto igual ao da classe mãe + 2
    }
    //========================
}
