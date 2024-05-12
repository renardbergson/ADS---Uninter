/*  
    EXERCÍCIO 1
    Desenvolva uma classe "Conta", que descreva uma conta bancária

    - Atributos
        Nome
        Saldo
    - Métodos
        Depositar
        Sacar
        Transferir
        Info
    Lance exceptions para tentativas de saque e depósito de valores negativos
    Opcional: cria classes para criar suas próprias exceções
*/

public class App {
    public static void main(String[] args) { 
        // * retirar "throws exception", para tornar esta classe responsável pelo tratamento de exceções *
        // no exemplo abaixo, "depositar" possui tratamento genérico, "sacar" e "transferir" possuem tratamento com Classes criadas para esse propósito
        // * observe que o "catch" para tratamento de exceção genérica deve ser o último! *

        Conta c1 = new Conta("Renard", 1250);
        Conta c2 = new Conta("Esdras", 820);

        try {
            c1.info();
            c1.depositar(50);
            c1.info();
            c1.sacar(300);
            c1.info();

            // EXCEÇÃO GENÉRICA
            //c1.depositar(0);

            // EXCEÇÃO CRIADA 1 (saldo insuficiente)
            //c1.sacar(1001);

            // EXCEÇÃO CRIADA 2 (valor inválido)
            //c1.sacar(0);

            c2.info();
            c1.transferir(100, c2);
            c1.info();
            c2.info();

            // EXCEÇÃO CRIADA 3 (saldo insuficiente)
            //c1.transferir(901, c2);

            // EXCEÇÃO CRIADA 4 (valor inválido)
            //c1.transferir(0, c2);
        } 
        catch (SaldoInsuficiente e) {
            System.out.println(e.getMessage());
        }
        catch (ValorInvalido e) {
            System.out.println(e.getMessage());
        } 
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
        finally {
            System.out.println();
            System.out.println("Finalizando programa...");
        }
    }
}
