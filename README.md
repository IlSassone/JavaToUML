# JavaToUML
This simple python program converts java classes into uml notations and saves the diagram in a PNG image


## How it works
To make this program work you have to put in your .java file some essential comments.
You have to wrap your attributes with ``` //start_attributes ``` ...your attributes... ``` //end_attributes ``` and the same with constructors and methods
And the result has to look like this

```java


public class Impiegato {
    //start_attributes
    private String matricola;
    private String nominativo;
    private int anno_assunzione;
    private int livello_retributivo;
    //end_attributes
    //start_constructors
    public Impiegato() {
        this.matricola = null;
        this.nominativo = null;
        this.anno_assunzione = 0;
        this.livello_retributivo = 0;
    }

    public Impiegato(String matricola, String nominativo, int anno_assunzione, int livello_retributivo) {
        this.matricola = matricola;
        this.nominativo = nominativo;
        this.anno_assunzione = anno_assunzione;
        this.livello_retributivo = livello_retributivo;
    }
    //end_construcotrs
    //start_methods
    public void setMatricola(String matricola) {
        this.matricola = matricola;
    }

    public void setNominativo(String nominativo) {
        this.nominativo = nominativo;
    }

    public void setAnno_assunzione(int anno_assunzione) {
        this.anno_assunzione = anno_assunzione;
    }

    public void setLivello_retributivo(int livello_retributivo) {
        this.livello_retributivo = livello_retributivo;
    }

    public String getMatricola() {
        return this.matricola;
    }

    public String getNominativo() {
        return this.nominativo;
    }

    public int getAnno_assunzione() {
        return this.anno_assunzione;
    }

    public int getLivello_retributivo() {
        return this.livello_retributivo;
    }

    public int Stipendio() {
        int annoCorrente = LocalDate.now().getYear();

        return 800 + (50 * (annoCorrente - this.anno_assunzione)) + (25 * this.livello_retributivo);
    }

    @Override
    public String toString() {
        return "Matricola: " + this.matricola
                + "\nNominativo: " + this.nominativo
                + "\nAnno d'assunzione: " + this.anno_assunzione
                + "\nLivello retributivo: " + this.livello_retributivo;
    }
    //end_methods
}
```
Then you must put your .java file in the same directory as main.py and type in the cmd
```batch
python main.py filename.java
```
