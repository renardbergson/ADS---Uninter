/*  
    POLIMORFISMO
        Basicamente, "Polimorfismo" significa "muitas formas". Com Polimorfismo, os mesmos Atributos e 
        Objetos podem ser utilizados/sobrescritos em Objetos distintos, porém, COM IMPLEMENTAÇÕES LÓGICAS DIFERENTES. Meio que já começamos a introduzir esse conceito, ao sobrescrever o método "info()" em classes herdeiras, usando a marcação @override, que também é um dos tipos de polimorfismo!
        Outro exemplo desse ponto de vista é aplicado quando instanciamos uma classe que assumirá a forma de outra, para a execução de determinado comportamento, ou seja, instanciar uma classe filha e acessá-la como se ela fosse um elemento da classe-mãe.

        Ex1:
        Jogo de aventura com uma superclasse "Guerreiro"

                                            **************************
                                            *       Personagem       *
                                            **************************
                                            *      + usa_arma        *
                                            **************************

        
        **************************          **************************          **************************   
        *        Guerreiro       *          *         Arqueiro       *          *           Mago         *
        **************************          **************************          **************************
        *      + usa_arma        *          *      + usa_arma        *          *      + usa_arma        *
        *        (espada)        *          *         (arco)         *          *        (cajado)        *
        **************************          **************************          **************************

        Guerreiro, Arqueiro e Mago são classes distintas, mas todas são polimórficas de uma classe central chamada Personagem[usaArma].

        Ex2:
        Imagine que vamos codar uma loja de carros online. Neste caso, vamos criar uma classe bem genérica chamada "Carro" e depois suas subclasses, fusca, ferrari, gol, etc. Visto que, todo ano há um aumento diferente para cada modelo, como implementar um método que atenda a todas essas necessidades?
        
        Podemos ter um método abstrato na superclasse, por exemplo, de nome "aumento()", depois, em cada subclasse sobrescrevemos esse método com o aumento pertinente. Assim, objetoFerrari.aumento() será diferente de objetoFusca.aumento().
        
        Polimorfismo em questão:
        Observe que usamos o MESMO NOME de método para as subclasses, porém, cada um age de FORMA DIFERENTE, ou seja, cada objeto terá sua particularidade.

        TIPOS DE POLIMORFISMO
            I - Horizontal ou Sobrecarga
                Não depende de herança para acontecer e caracteriza-se pela criação de métodos com o mesmo nome, porém com parâmetros diferentes.
            II - Vertical, Override ou Sobrescrita (aulas anteriores)
                Caracteriza-se pela sobrescrita de um método da superclasse a partir da subclasse.
            
*/

public class App {
    public static void main(String[] args) throws Exception {
        Horizontal superclasse = new Horizontal();
        superclasse.fazAlgo();
        superclasse.fazAlgo("Este é o método que exemplifica Polimorfismo Horizontal");

        System.out.println(); // espaço em branco

        Vertical subclasse = new Vertical();
        subclasse.fazAlgo();
    }
}
