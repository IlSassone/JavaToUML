/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ese1ferrari;

import java.time.*;

/**
 *
 * @author user
 */
public class Impiegato {
    //start_attributes
    private String matricola;
    private String nominativo;
    private LocalDate annoAssunzione;
    private int livelloRetributivo;
    
    public static final int BASE_STIPENDIO = 800;
    public static final int ANZIANITA = 50;
    public static final int QUOTA_RETRIBUTIVA = 25;
    public static int contaMatricole = 0;
    //end_attributes
    
    //start_constructors
    public Impiegato(String nominativo, int annoAssunzione, int livelloRetributivo) throws Exception{
        if(annoAssunzione>LocalDate.now().getYear()) throw new Exception("Data sbagliata");
        else{
            this.matricola = "MAT"+contaMatricole;
            this.nominativo = nominativo;
            this.annoAssunzione = LocalDate.of(annoAssunzione, Month.JANUARY, 1);

            if(livelloRetributivo<1) livelloRetributivo=1;
            else if (livelloRetributivo>6) livelloRetributivo=6;

            this.livelloRetributivo = livelloRetributivo;
            contaMatricole++;
        }
        
    }
    //end_constructors
    
    
    //start_methods
    
    public String getMatricola() {
        return matricola;
    }

    public void setMatricola(String matricola) {
        this.matricola = matricola;
    }

    public String getNominativo() {
        return nominativo;
    }

    public void setNominativo(String nominativo) {
        this.nominativo = nominativo;
    }

    public LocalDate getAnnoAssunzione() {
        return annoAssunzione;
    }

    public void setAnnoAssunzione(LocalDate annoAssunzione) {
        this.annoAssunzione = annoAssunzione;
    }

    public int getLivelloRetributivo() {
        return livelloRetributivo;
    }

    public void setLivelloRetributivo(byte livelloRetributivo) {
        this.livelloRetributivo = livelloRetributivo;
    }
    
    public double stipendio(){
        return BASE_STIPENDIO+(QUOTA_RETRIBUTIVA*this.livelloRetributivo)+
                ((LocalDate.now().getYear()-this.annoAssunzione.getYear())*ANZIANITA);
    }

    @Override
    public String toString() {
        return "Impiegato{" + "matricola=" + matricola + ", nominativo=" + nominativo + ", annoAssunzione=" + annoAssunzione + ", livelloRetributivo=" + livelloRetributivo + ", Stipendio=" + this.stipendio() + '}';
    }
    
    //end_methods
    
}
