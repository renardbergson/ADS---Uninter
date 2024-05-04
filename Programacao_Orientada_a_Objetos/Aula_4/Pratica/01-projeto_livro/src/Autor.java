public class Autor {
    private String nome;
    private String email;
    private String nacionalidade;

    public Autor (String nome, String email, String nacionalidade) {
        setNome(nome);
        setEmail(email);
        setNacionalidade(nacionalidade);
    }

    public void setNome (String nome) {
        this.nome = nome;
    }

    public void setEmail (String email) {
        this.email = email;
    }

    public void setNacionalidade (String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public String getNome () {
        return nome;
    }

    public String getEmail () {
        return email;
    }

    public String getNacionalidade () {
        return nacionalidade;
    }

    void info () {
        System.out.println("Nome do autor: " + nome);
        System.out.println("E-mail do autor: " + email);
        System.out.println("Nacionalidade do autor: " + nacionalidade);
    }
}
