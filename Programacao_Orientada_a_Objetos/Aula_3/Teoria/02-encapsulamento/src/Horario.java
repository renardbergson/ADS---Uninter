public class Horario {
    private int hora;
    private int minutos;
    private int segundos;

    // Protegemos os atributos, os tornando Privados e criamos métodos públicos (get, set), com verificações, para os definir

    // HORA
    public int getHora () { // mostrar a hora
        return hora;
    }

    public void setHora (int hora) { // definir a hora
        if (hora >= 0 && hora <= 23) {
            this.hora = hora;
            System.out.println("Hora setada com sucesso!");
            return;
        }

        System.out.println("Hora inválida!");
    }

    // MINUTOS
    public int getMinutos () { // mostrar a hora
        return minutos;
    }

    public void setMinutos (int minutos) { // definir a hora
        if (minutos >= 0 && hora <= 59) {
            this.minutos = minutos;
            System.out.println("Minutos setados com sucesso!");
            return;
        }

        System.out.println("Minutos inválidos!");
    }

    // SEGUNDOS
    public int getSegundos () { // mostrar a hora
        return segundos;
    }

    public void setSegundos (int segundos) { // definir a hora
        if (segundos >= 0 && segundos <= 59) {
            this.segundos = segundos;
            System.out.println("Segundos setados com sucesso!");
            return;
        }

        System.out.println("Segundos inválidos!");
    }
}
