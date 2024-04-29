public class Nota {
    private double nota1;
    private double nota2;
    private int faltas;

    Nota () {
        // vazio
    }

    Nota (double nota1, double nota2, int faltas) {
        setNota1(nota1); // o "this" já existe dentro do método
        setNota2(nota2); // o "this" já existe dentro do método
        setFaltas(faltas);
    }

    public void setNota1 (double nota) {
        if (nota < 0 || nota > 10) {
            System.out.println("Primeira nota inserida inválida!");
            return;
        }

        nota1 = nota;
    }

    public void setNota2 (double nota) {
        if (nota < 0 || nota > 10) {
            System.out.println("Segunda nota inserida inválida!");
            return;
        }

        nota2 = nota;
    }

    public void setFaltas (int faltas) {
        if (faltas < 0 || faltas > 40) {
            System.out.println("Número de faltas inválido!");
        }

        this.faltas = faltas;
    }

    public double getNota1 () {
        return nota1;
    }

    public double getNota2 () {
        return nota2;
    }

    public int getFaltas () {
        return faltas;
    }

    public void resultado () {
        double media = (nota1 + nota2) / 2;

        System.out.println("Primeira Nota: " + nota1);
        System.out.println("Segunda Nota: " + nota2);
        System.out.println("Faltas do aluno: " + faltas);
        System.out.printf("Média do aluno: %.2f \n", media);

        if (faltas > 7) {
            System.out.println("Aluno reprovado por faltas!");
            System.out.println();
            return;
        }
        
        if (media < 5) {
            System.out.println("Aluno reprovado por média!");
            System.out.println();
        } else if (media < 7) {
            System.out.println("Aluno designado para o exame final.");
            System.out.println();
        } else {
            System.out.println("Aluno aprovado!");
            System.out.println();
        }
    }
}
