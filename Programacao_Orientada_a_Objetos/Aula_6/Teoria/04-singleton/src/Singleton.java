public class Singleton {
    public int numero;

    private static Singleton instancia = null; // a princípio é um objeto nulo

    private Singleton () { // construtor privado *
        numero =  20;
    }

    public static Singleton getInstance () { // obter instância
        if (instancia == null) {
            instancia = new Singleton();
        }

        return instancia;
        // que seja nulo ou não, retorna a instância, o que muda é a atribuição de endereço
        // garante retornar sempre a mesma instância ao longo do ciclo de vida do projeto
    }
}
