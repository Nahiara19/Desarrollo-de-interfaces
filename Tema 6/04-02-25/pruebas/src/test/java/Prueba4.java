import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;
import com.example.Main4;

public class Prueba4 {
    @Test
    public void testObtenerPromedioEdades(){
        List<Integer> edades = Arrays.asList(20, 25, 30, 35, 40);
        double promedio = Main4.obtenerPromedioEdades(edades);
        assertEquals(30.0, promedio, 0.01);
    }
}
