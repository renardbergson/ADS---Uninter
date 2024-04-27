/*  
    LOCALDATE
        - Forma robusta de representar datas
        - Substitui java.utilData e java.util.Calendar
        - Versão 8 do Java em diante
*/

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class App {
    public static void main(String[] args) throws Exception {
        LocalDate dataHoje = LocalDate.now();
        
        System.out.println(dataHoje);

        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println(dataHoje.format(formatador));
        // buscar documentação para conferir as demais opções de formatos
    }
}
