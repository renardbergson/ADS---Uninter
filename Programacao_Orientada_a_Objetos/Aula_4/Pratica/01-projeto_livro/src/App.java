/*  
    EXERCÍCIO 1
    
    Escreva um código para a representação UML a seguir:

                  |-------------------------------- 1 🔸 *******************************
                  |                                      *            Livro            *   
                  |                                      *******************************
                  |                                      *       - titulo: String      *
                  |                                      *        - autor: Autor       *
                  |                                      *       - genero: String      *
                  |                                      *        - edicao: int        *
                  |                                      *******************************
                  |                                      *           + get ()          *
                  |                                      *           + set ()          *
                  |                                      *******************************
                  |                                                    △
    *******************************                    |---------------|-------------|
    *            Autor            *                    |                             |
    *******************************          ********************           *********************
    *       - nome: String        *          *    Livro fisico  *           *   Livro digital   *
    *      - email: String        *          ********************           *********************
    *   - nacionalidade: String   *          *  - tiragem: int  *           * - download: int   *
    *******************************          *  - peso: String  *           * - tamanho: String *
    *           + get ()          *          ********************           *********************
    *           + set ()          *          *     + get()      *           *     + get()       *
    *******************************          *     + set()      *           *     + set()       *
    .                                        ********************           *********************
    
    O losango indica que a classe "Autor" COMPÕE / INTEGRA / FAZ PARTE de "Livro"
    O "1" indica que cada "Livro" tem UM "Autor"
    A seta fechada indica que "Livro fisico" e "Livro digital" são HERDEIRAS de "Livro"
*/                                           

public class App {
    public static void main(String[] args) throws Exception {
        LivroFisico lv = new LivroFisico("Java - Primeiros Passos", new Autor("Renard Bergson", "renardrock@gmail.com", "Brasileiro"), "Educativo", 1, 1000, "920g");

        System.out.println();
        System.out.println("DADOS DO LIVRO FÍSICO");
        lv.info();
        System.out.println();

        LivroDigital ld = new LivroDigital("Java - Primeiros Passos", new Autor("Renard Bergson", "renardrock@gmail.com", "Brasileiro"), "Educativo", 1, 9, "232mb");

        System.out.println("DADOS DO LIVRO DIGITAL");
        ld.info();
        System.out.println();
    }
}
