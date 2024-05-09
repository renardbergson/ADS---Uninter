public class Desktop extends Computador {
    double precoAcessorios;

    public Desktop (int gbMemoria, int numProcessadores, double precoAcessorios) {
        super(gbMemoria, numProcessadores);
        this.precoAcessorios = precoAcessorios;
    }

    @Override
    public double calculaValor () {
        double total = (gbMemoria * 200) + (numProcessadores * 400) + precoAcessorios;
        return total;
    }
}
