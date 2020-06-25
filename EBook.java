/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ese2ferrari;

import java.util.Objects;

/**
 *
 * @author mattia
 */
public class EBook {
    //start_attributes
    
    public static final double PREZZO_PAGINA = 0.05;
    public static final double PREZZO_LIBRO = 4;
    
    private String titolo;
    private String autore;
    private int nPagine;

    //end_attributes



    //start_constructors
    
    public EBook(String titolo, String autore, int nPagine) {
        this.titolo = titolo;
        this.autore = autore;
        this.nPagine = nPagine;
    }

    //end_constructors



    //start_methods
        
    public String getTitolo() {
        return titolo;
    }

    public void setTitolo(String titolo) {
        this.titolo = titolo;
    }

    public String getAutore() {
        return autore;
    }

    public void setAutore(String autore) {
        this.autore = autore;
    }

    public int getnPagine() {
        return nPagine;
    }

    public void setnPagine(int nPagine) {
        this.nPagine = nPagine;
    }
    
    public double prezzo(){
        return (this.nPagine*PREZZO_PAGINA)+PREZZO_LIBRO;
    }
    
    @Override
    public String toString() {
        return "EBook{" + "titolo=" + titolo + "; autore=" + autore + "; nPagine=" + nPagine + "; prezzo=" + this.prezzo() +  '}';
    }


    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final EBook other = (EBook) obj;
        if (this.nPagine != other.nPagine) {
            return false;
        }
        if (!Objects.equals(this.titolo, other.titolo)) {
            return false;
        }
        if (!Objects.equals(this.autore, other.autore)) {
            return false;
        }
        return true;
    }
    
    
    
    
    //end_methods

    

    

    


}
