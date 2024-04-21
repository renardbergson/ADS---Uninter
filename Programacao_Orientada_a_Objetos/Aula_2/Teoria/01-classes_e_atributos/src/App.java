/*  
    CLASSE
        Classifica os objetos
        Busca abstrair conceitos do mundo real
        Aproximação da lógica de programação com a linguagem falada

        Ex:
            Classe = Carro
                Objeto = McQueen
                    Cor: Vermelho
                    Modelo: Mazda
                    Velocidade: 220 km/h
                Objeto = Ramirez
                    Cor: Amarelo
                    Modelo: Ferrari
                    Velocidade: 20 km/h
                Objeto = Sally
                    Cor: Azul
                    Modelo: Porsche
                    Velocidade: 210 km/h
    ATRIBUTOS
        São as características, do que o objeto é composto
    MÉTODOS
        O que o objeto faz (análogo a uma função)
    ESTADO
        O valor que cada atributo recebe, o valor atual de cada um
*/

public class App {
    public static void main(String[] args) throws Exception {
        Aluno a = new Aluno(); // instanciamos um objeto da classe "Aluno" e o atribuimos à variável "a"
        a.nome = "Renard Bergson";
        a.cpf = "000111222-33";
        a.matricula = 1001;

        System.out.println("Nome: " + a.nome);
        System.out.println("Cpf: " + a.cpf);
        System.out.println("Matrícula: " + a.matricula);

        System.out.println();

        Aluno b = new Aluno();
        b.nome = "Esdras Medeiros";
        b.cpf = "111222333-44";
        b.matricula = 1002;

        System.out.println("Nome: " + b.nome);
        System.out.println("Cpf: " + b.cpf);
        System.out.println("Matrícula: " + b.matricula);
    }
}