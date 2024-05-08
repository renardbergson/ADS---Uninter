public class Gato implements Animal { // podemos implementar várias interfaces!

    @Override
    public void emitirSom () {
        System.out.println("Miaaau");
    }

    @Override
    public void dormir () {
        System.out.println("zzZzZzzZzZzzZzz...");
    }
    
}
