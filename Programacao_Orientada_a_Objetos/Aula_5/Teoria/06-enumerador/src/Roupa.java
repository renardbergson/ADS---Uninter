enum Estacao {
    verao, 
    outono,
    inverno,
    primavera
}

public class Roupa {
    // ❌ int colecao; // 1 verão, 2 outono, 3 inverno, 4 primavera
    // veja que, mesmo que implementássemos Strings ao invés de números, ainda teríamos problemas com as questões de caracteres maiúsculos e minúsculos
    
    String modelo;
    int tamanho;
    Estacao colecao; // colecao é do tipo "Estacao"

    /*  ❌
        public Roupa (String modelo, int tamanho, int colecao) {
        this.modelo = modelo;
        this.tamanho = tamanho;
        this.colecao = colecao;
        } 
    */

    public Roupa (String modelo, int tamanho, Estacao colecao) {
        this.modelo = modelo;
        this.tamanho = tamanho;
        this.colecao = colecao;
        } 

    /*  ❌
        public void mensagem () {
            switch (colecao) {
                case 1:
                    System.out.println("Arrase na praia!");
                    break;
                case 2:
                    System.out.println("Passe o outono com elegância");
                    break;
                case 3:
                    System.out.println("Se agasalhe bem e com estilo");
                    break;
                case 4:
                    System.out.println("Vista-se na estação das flores");
                    break;
                default:
                    break;
            }
        } 
    */

    public void mensagem () {
        switch (colecao) {
            case verao:
                System.out.println("Arrase na praia!");
                break;
            case outono:
                System.out.println("Passe o outono com elegância");
                break;
            case inverno:
                System.out.println("Se agasalhe bem e com estilo");
                break;
            case primavera:
                System.out.println("Vista-se na estação das flores");
                break;
            default:
                break;
        }
    } 

    // perceba que essa abordagem é pouco clara, pouco intuitiva, mais sujeita a problemas
}
