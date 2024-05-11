public class Usuario {
    int id;
    String nome;
    String cpf;

    public Usuario (int id, String nome, String cpf) {
        this.id = id;
        this.nome = nome;
        this.cpf = cpf;
    }

    public boolean equals (Object obj) { // todos os objetos são filhos de uma superclasse "Object"
        if (this == obj) {
            return true;
        } else {
            return false;
        }
    }
}
