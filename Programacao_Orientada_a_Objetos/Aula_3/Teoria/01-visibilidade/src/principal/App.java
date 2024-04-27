/*  
    VISIBILIDADE
    As palavras reservadas ao controle de visibilidade vêm antes de Classes, Atributos e Métodos

    PUBLIC:
        Resumo: Torna o elemento visível para todas as outras classes
            ✅ Mesma Classe
            ✅ Qualquer Classe no mesmo pacote
            ✅ Classes herdeiras e mesmo pacote
            ✅ Classes herdeiras e pacotes diferentes
            ✅ Qualquer Classe em outros pacotes
    PRIVATE:
        Resumo: Torna o elemento visível somente dentro da classe
            ✅ Mesma Classe
            ❌ Qualquer Classe no mesmo pacote
            ❌ Classes herdeiras e mesmo pacote
            ❌ Classes herdeiras e pacotes diferentes
            ❌ Qualquer Classe em outros pacotes
    PROTECTED:
        Resumo: Torna o elemento visível apenas para classes derivadas (herança)
            ✅ Mesma Classe
            ✅ Qualquer Classe no mesmo pacote
            ✅ Classes herdeiras e mesmo pacote
            ✅ Classes herdeiras e pacotes diferentes
            ❌ Qualquer Classe em outros pacotes
    DEFAULT:
        Resumo: Se não especificado, o elemento adota a visibilidade padrão
            ✅ Mesma Classe
            ✅ Qualquer Classe no mesmo pacote
            ✅ Classes herdeiras e mesmo pacote
            ❌ Classes herdeiras e pacotes diferentes
            ❌ Qualquer Classe em outros pacotes
*/

package principal;

public class App {
    public static void main(String[] args) throws Exception {
        Aluno a = new Aluno(1001, "Renard Bergson", "111222333-44");
        // não é possível acessar o atributo "matrícula" diretamente, mas passar para o construtor sim

        a.info();
    }
}
