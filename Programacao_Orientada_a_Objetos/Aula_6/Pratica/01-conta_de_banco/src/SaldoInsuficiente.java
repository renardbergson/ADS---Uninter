public class SaldoInsuficiente extends Exception {
    String mensagem = "❌ Saldo Insuficiente! (Tratado por exceção criada)";

    public String getMessage () {
        return mensagem;
    }
}
