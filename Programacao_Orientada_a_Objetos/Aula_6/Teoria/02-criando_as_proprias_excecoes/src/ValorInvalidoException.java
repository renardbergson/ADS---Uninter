public class ValorInvalidoException extends Exception {
    String mensagem;

    public ValorInvalidoException (String mensagem) {
        this.mensagem = mensagem;
    }

    public String mensagem () {
        return mensagem;
    }
}
