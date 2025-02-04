import static org.junit.Assert.assertArrayEquals;
import java.util.ArrayList;
import java.util.List;
 
import org.junit.Test;
 
import com.example.Main3;
 
public class Prueba3 {
    @Test
    public void testObtenerNombresEnMayusculas() {
        List<String> lista = new ArrayList<>();
        lista.add("juan");
        lista.add("maria");
        lista.add("pedro");
        lista.add("luis");
        List<String> nombresEnMayusculas = Main3.obtenerNombresEnMayusculas(lista);
        assertArrayEquals(new String[] { "JUAN", "MARIA", "PEDRO" , "LUIS" }, nombresEnMayusculas.toArray(new String[0]));
    }
}