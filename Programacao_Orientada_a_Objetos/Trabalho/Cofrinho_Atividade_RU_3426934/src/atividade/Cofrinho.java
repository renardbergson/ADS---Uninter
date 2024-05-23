package atividade;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;
import java.text.NumberFormat;
import java.util.Locale;

public class Cofrinho {
	private ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();

    public void menu () {
        Scanner teclado = new Scanner(System.in);
        
        while (true) {
            System.out.println("BEM-VINDO AO COFRINHO!");
            System.out.println("Escolha uma das opções do menu:");
            System.out.println();

            
            System.out.println("1 - Adicionar Moeda");
            System.out.println("2 - Listar Moedas");
            System.out.println("3 - Remover Moeda");
            System.out.println("4 - Calcular total convertido para Real");
            System.out.println("0 - Encerrar");

            int opcaoMenu = teclado.nextInt();
            boolean menuInvalido = opcaoMenu != 1 && opcaoMenu != 2 && opcaoMenu != 3 && opcaoMenu != 4 && opcaoMenu != 0;

            // opção inválida
            if (menuInvalido) {
                continue;
            }

            // adicionar, listar, remover ou calcular
            switch (opcaoMenu) {
                case 1: // adicionar moeda
                    while (true) {
                        // menu escolha de moeda
                        System.out.println();
                        System.out.println("De qual tipo de moeda deseja adicionar?");
                        System.out.println();
    
                        System.out.println("1 - Real");
                        System.out.println("2 - Dólar");
                        System.out.println("3 - Euro");
                        System.out.println("4 - Retornar ao Menu Principal");
    
                        int opcaoMoeda = teclado.nextInt();
                        boolean opcaoInvalida = opcaoMoeda != 1 && opcaoMoeda != 2 && opcaoMoeda != 3 && opcaoMoeda != 4;
    
                        // opção inválida
                        if (opcaoInvalida) {
                            continue; // repete a pergunta
                        }
    
                        // cancelar depósito
                        if (opcaoMoeda == 4) {
                            System.out.println();
                            this.menu(); // menu principal
                            break; 
                        }
    
                        // prosseguir com depósito
                        System.out.println();
                        System.out.println("Digite o valor que deseja inserir. Ex: 2,50:");
    
                        double valorMoeda = teclado.nextDouble();
    
                        switch (opcaoMoeda) {
                            case 1:
                                // adicionar Real
                                adicionar(new Real(valorMoeda));
                                break;
                            case 2:
                                // adicionar Dólar
                                adicionar(new Dolar(valorMoeda));
                                break;
                            case 3:
                                // adicionar Euro
                                adicionar(new Euro(valorMoeda));
                                break;
                            default:
                                break;
                        }
                        
                        break; // sair do loop
                    }
                    break;
                case 2: // listar moedas
                    listarMoedas();
                    break;
                case 3: // remover moeda
                    remover(teclado);
                    break;
                case 4: // calcular total em real
                    totalConvertido();
                    break;
                case 0: // encerrar
                    System.out.println();
                    System.out.println("Programa encerrado!");
                    break;
                default:
                    break;
                }
                
            teclado.close();
            break; // sair do loop do menu
        }
    }

    public void adicionar (Moeda moeda) {
        listaMoedas.add(moeda);
        moeda.info();
        this.menu(); // menu principal
    }

    public void listarMoedas () {
        System.out.println();
        System.out.println("------------------");
        System.out.println("Depósitos no cofre");
        System.out.println();
        
        for (Moeda m : listaMoedas) {
            switch (m.tipo) {
                case "Real":
                    System.out.println(m.tipo + " " + converter("Real", m.valor));
                    break;
                case "Dólar":
                    System.out.println(m.tipo + " " + converter("Dólar", m.valor));
                    break;
                case "Euro":
                    System.out.println(m.tipo + " " + converter("Euro", m.valor));
                    break;
                default:
                    break;
            }
        }

        System.out.println("------------------");
        System.out.println();
        
        this.menu(); // menu principal
    }

    public void remover (Scanner teclado) {        
        while (true) {
            // menu escolha de moeda
            System.out.println();
            System.out.println("De qual tipo de moeda deseja remover?");
            System.out.println("1 - Real");
            System.out.println("2 - Dólar");
            System.out.println("3 - Euro");
            System.out.println("4 - Retornar ao Menu Principal");

            int opcao = teclado.nextInt();
            boolean opcaoInvalida = opcao != 1 && opcao != 2 && opcao != 3 && opcao != 4;

            // opção numérica inválida
            if (opcaoInvalida) {
                continue;
            }

            // retornar ao menu principal sem remover
            if (opcao == 4) {
                System.out.println();
                this.menu(); // menu principal
                break;
            }

            // prosseguir com a remoção
            System.out.println();
            System.out.println("Digite o valor (exato) do depósito que deseja remover. Ex: 2,50 ");
            double valorRemover = teclado.nextDouble();
            
            switch (opcao) {
                case 1:
                    remocao("Real", valorRemover);
                    break;
                case 2:
                    remocao("Dólar", valorRemover);
                    break;
                case 3:
                    remocao("Euro", valorRemover);
                    break;
                default:
                    break;
            }
            
            System.out.println();
            System.out.println("- Se havia algum depósito do valor informado, ele foi removido!");
            System.out.println();
            
            this.menu(); // menu principal
            break; // sair do loop
        }
    }

    private boolean remocao (String tipo, double valor) {
        int contador = 1;
                    
        Iterator<Moeda> item = listaMoedas.iterator();
        
        while (item.hasNext() && contador < 2) {
            final Moeda alvo = item.next();

            if (alvo.tipo == tipo && alvo.valor == valor) {
                item.remove();
                contador++; // remover um depósito de cada vez
            }
        }

        return true;
    }

    public static String converter (String tipo, double valor) {
    	// "static", para que seja possível chamar este médodo sem instanciar a Classe
        @SuppressWarnings("deprecation")
        Locale localBrasil = new Locale("pt", "BR");
        Locale localUsa = Locale.US;
        Locale localEuropa = Locale.FRANCE;

        String valorConvertido = "";

        switch (tipo) {
            case "Real":
                valorConvertido = NumberFormat.getCurrencyInstance(localBrasil).format(valor);
                break;
            case "Dólar":
                valorConvertido = NumberFormat.getCurrencyInstance(localUsa).format(valor);
                break;
            case "Euro":
                valorConvertido = NumberFormat.getCurrencyInstance(localEuropa).format(valor);
                break;
            default:
                break;
        }

        return valorConvertido;
    }

    public void totalConvertido () {
        double total = 0;

        Iterator<Moeda> item = listaMoedas.iterator();
        
        while (item.hasNext()) {
            total += item.next().converter();
        }
        
        System.out.println();
        System.out.println("* A soma do valor total (em reais) equivale a " + converter("Real", total));
        System.out.println();

        this.menu(); // menu principal
    }
}