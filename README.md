# JavaToUML
This is a simple python program to automate the creation of uml diagrams.
## Usage
1. go to your folder which contains the java class you want to make the model on.
2. open the terminal in that folder
3. type this
```bash
user:~/your/class/folder/location$  python3 <path_to_the_python_script> <JavaClassFileName.java>
```
# Important
To create the UML the python script utilizes some markup comments that MUST be present in the java code:
```java
  public class Impiegato {

    //start_attributes

    private String matricola;
    private String nominativo;
    private LocalDate annoAssunzione;
    private byte livelloRetributivo;
    

    //end_attributes

    //start_constructors
    
    public Impiegato(String nominativo, int annoAssunzione, byte livelloRetributivo) throws Exception{
        if(annoAssunzione>LocalDate.now().getYear()) throw new Exception("Data sbagliata");
        else{
            this.matricola = "MAT"+contaMatricole;
            this.nominativo = nominativo;
            this.annoAssunzione = LocalDate.of(1, Month.JANUARY, annoAssunzione);

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

   
    //end_methods
    
}
```
As you can see the attributes are wrapped into "//start_attributes...[some code here]...//end_attributes" for example. This comments MUST be present and they are mandatory for the pythonn script to work




