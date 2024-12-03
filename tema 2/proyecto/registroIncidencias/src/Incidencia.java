public class Incidencia{
    private String nombre;
    private String apellidos;
    private String telefono;
    private String matricula;
    private String modelo;
    private String incidencia;

    public Incidencia(String nombre, String apellidos, String telefono, String matricula, String modelo, String incidencia) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.telefono = telefono;
        this.matricula = matricula;
        this.modelo = modelo;
        this.incidencia = incidencia;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nom) {
        this.nombre = nom;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String ape) {
        this.apellidos = ape;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String tel) {
        this.telefono = tel;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String mat) {
        this.matricula = mat;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String mod) {
        this.modelo = mod;
    }

    public String getIncidencia() {
        return incidencia;
    }

    public void setIncidencia(String in) {
        this.incidencia = in;
    }

}