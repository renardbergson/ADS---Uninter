public class IngressoVip extends Ingresso {
    public double adicional;

    public IngressoVip (String nomeEvento, double valor, double adicional) {
        super(nomeEvento, valor);
        this.adicional = adicional;
    }

    @Override // queremos sobrescrever o método "info" da superclasse
    public void info () {
        super.info();
        System.out.printf("Valor adicional: R$ %.2f \n", adicional);
        System.out.printf("TOTAL A PAGAR: R$ %.2f \n", valor + adicional);
    }
}
