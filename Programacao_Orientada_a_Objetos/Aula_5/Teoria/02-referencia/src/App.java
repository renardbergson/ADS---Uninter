// Veremos a seguir o conceito chamado de "referência"

public class App {
    public static void main(String[] args) throws Exception {
        
        Funcionario f1 = new Funcionario("Renard");
        Funcionario f2 = f1;

        System.out.println("Nome do primeiro funcionário: " + f1.nome); // Renard
        System.out.println("Nome do segundo funcionário: " + f2.nome); // Renard

        System.out.println();

        f2.nome = "Bergson";
        System.out.println("Nome do primeiro funcionário: " + f1.nome); // Bergson
        System.out.println("Nome do segundo funcionário: " + f2.nome); // Bergson

        System.out.println();

        f1.nome = "Medeiros";
        System.out.println("Nome do primeiro funcionário: " + f1.nome); // Medeiros
        System.out.println("Nome do segundo funcionário: " + f2.nome); // Medeiros

        /*  
            A mudança ocorre em ambos porque, com o operador "new" estamos separando um espaço na 
            memória para instanciar "f1". No momento em que dizemos que "f2" é igual a "f1", na 
            prática, os dois apontam para o mesmo espaço alocado de memória.
        */
    }
}
