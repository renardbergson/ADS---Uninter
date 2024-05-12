public class ValorInvalido extends Exception {
    String mensagem = "❌ Valor Inválido! (Tratado por exceção criada)";

    public String getMessage () {
        return mensagem;
    }
}
