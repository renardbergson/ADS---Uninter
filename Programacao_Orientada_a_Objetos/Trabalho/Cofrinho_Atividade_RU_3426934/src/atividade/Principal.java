package atividade;

public class Principal {

	public static void main(String[] args) {
		Cofrinho cofre = new Cofrinho();

		try {
			cofre.menu();
		} 
		catch (Exception InputMismatchException) {
			// usuário inseriu letra em algum menu ou inseriu valores usando ponto
			System.out.println();
			System.out.println("Erro! A opção digitada não corresponde ao valor esperado.");
			System.out.println("Verifique as instruções a seguir e tente novamente:");
			System.out.println();
			System.out.println("I - Digite números inteiros para interagir com os Menus");
			System.out.println("II - Para inserir valores quebrados no cofre, utilize vírgula");
		}
		finally {
			System.out.println();
			System.out.println("Finalizando programa...");
		}
	}
	
}