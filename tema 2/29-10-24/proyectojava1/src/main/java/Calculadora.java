import javafx.application.Application;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Calculadora extends Application{
    @Override
    public void start(Stage stage) {
        Label label1 = new Label("numero 1: ");
        TextField numero1 =  new TextField();
        Label label2 = new Label("numero 2: ");
        TextField numero2 = new TextField();
        TextField resultado = new TextField();
        Button  sumar =  new Button("Sumar");

        GridPane grid =  new GridPane();
        grid.setVgap(10);
        grid.setHgap(10);
        grid.add(label1,0,0);
        grid.add(numero1,1,0);
        grid.add(label2,0,1);
        grid.add(numero2,1,1);

        Scene escena = new Scene(grid,400,250);
        stage.setTitle("Calculadora");
        stage.


    }

    public static void main (String[] args) {
        launch(args);
    }


}
