/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package ese3ferrari;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;


/**
 *
 * @author mattia
 */
public class Fattura {
    //start_attributes
    public static int numeroFattura = 0;
    
    private int numeroIdentificativo;
    private LocalDate data;
    private String cliente;
    private String indirizzo;
    private String citta;
    private ArrayList<Prodotto> righe = new ArrayList<>();

    //end_attributes




    //start_constructors

    public Fattura(int giorno, int mese, int anno, String cliente, String indirizzo, String citta) {
        this.data = LocalDate.of(anno, mese, giorno);
        this.cliente = cliente;
        this.indirizzo = indirizzo;
        this.citta = citta;
        this.numeroIdentificativo = numeroFattura;
        numeroFattura++;
    }

    //end_constructors




    //start_methods


    public double imponibile() {
        double x = 0;
        for (var p: this.righe){
            x+= p.getPrezzo()*p.getQuantita();
        }
        
        return x;
    }
    
    public double iva() {
        double x = 0;
        for (var p: this.righe){
            x+= p.getPrezzo()*p.getQuantita()*(p.getAliquota()/100);
        }
        
        return x;
    }
    public double totale() {
        return this.imponibile()+this.iva();
    }
    
    public void aggiungiProdotto(String codice, String desc, double prezzo, double aliquota, int quantita) {
        this.righe.add(new Prodotto(codice, desc, prezzo, aliquota, quantita));
    }
    
    public void aggiungiProdotto(Prodotto p) {
        this.righe.add(p);
    }
    
    public void rimuoviProdotto(String codice) throws Exception {
        Prodotto eliminato = null;
        for(Prodotto p : this.righe){
            if (p.getCodice().equals(codice)) eliminato = p;
        }
        if(eliminato==null) throw new Exception("Non c'è il più il prodotto");
        else {
            this.righe.remove(eliminato);
        }
    }
   

    public static int getNumeroFattura() {
        return numeroFattura;
    }

    public static void setNumeroFattura(int numeroFattura) {
        Fattura.numeroFattura = numeroFattura;
    }

    public int getNumeroIdentificativo() {
        return numeroIdentificativo;
    }

    public void setNumeroIdentificativo(int numeroIdentificativo) {
        this.numeroIdentificativo = numeroIdentificativo;
    }

    public LocalDate getData() {
        return data;
    }

    public void setData(LocalDate data) {
        this.data = data;
    }

    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    public String getIndirizzo() {
        return indirizzo;
    }

    public void setIndirizzo(String indirizzo) {
        this.indirizzo = indirizzo;
    }

    public String getCitta() {
        return citta;
    }

    public void setCitta(String citta) {
        this.citta = citta;
    }

    public ArrayList<Prodotto> getRighe() {
        return righe;
    }

    public void setRighe(ArrayList<Prodotto> righe) {
        this.righe = righe;
    }

    @Override
    public String toString(){
        return "";
    }
    
    
     //end_methods
}
