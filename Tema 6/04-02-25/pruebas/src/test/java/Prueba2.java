import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;
import com.example.Main2;

public class Prueba2 {
    @Test
    public void testSumarValoresPares(){
        List<Integer> lista = Arrays.asList(1, 2, 3, 4, 5, 6);
        assertEquals(12, Main2.sumaValoresPares(lista)); // 2 + 4 + 6 = 12
    }
}
