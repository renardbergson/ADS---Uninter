public class Avaliacao {
    double nota1, nota2, nota3;

    // Construtor
    Avaliacao (double nota1, double nota2, double nota3) {
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }

    // neste caso, não se usa "void", porque queremos retornar alguma coisa
    public double mediaAritmetica () {
        return (nota1 + nota2 + nota3) / 3;
    }

    public double mediaPonderada () {
        return ( (nota1 * 2) + (nota2 * 3) + (nota3 * 4) ) / 9;
    }
}