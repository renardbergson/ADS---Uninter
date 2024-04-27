/*  
    ENCAPSULAMENTO
        É um dos pilares da orientação a objetos
        Cápsula (protege o que está dentro)
        Protege o que está fora
        Baseado nos métodos "get" e "set"
*/

public class App {
    public static void main(String[] args) throws Exception {
        Horario hora = new Horario();
        
        // ❌ hora.hora = 25;
        // ❌ hora.minutos = 61;
        // ❌ hora.segundos = 61;

        hora.setHora(24);
        hora.setMinutos(50);
        hora.setSegundos(32);
    }
}
