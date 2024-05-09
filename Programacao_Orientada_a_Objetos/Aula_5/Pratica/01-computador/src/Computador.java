public abstract class Computador {
    // uma classe abstrata NÃO pode ser instanciada mas pode ser atribuida
    // permite criar métodos abstratos

    int gbMemoria;
    int numProcessadores;

    public Computador (int gbMemoria, int numProcessadores) {
        this.gbMemoria = gbMemoria;
        this.numProcessadores = numProcessadores;
    }

    public abstract double calculaValor();
    // o cálculo do valor será uma particularidade de cada modelo
}
