import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;
 
import java.io.IOException;
 
/**
 * JavaFX App
 */
public class App extends Application {
 
    @Override
    public void start(Stage stage) throws IOException {
        Label label1 = new Label("Numero 1: ");
        TextField numero1 = new TextField();
        Label label2 = new Label("Numero 2: ");
        TextField numero2 = new TextField();
        Label res = new Label("Resultado: ");
        TextField resultado =  new TextField();
        Button sumar =  new Button("Sumar");
        Button restar =  new Button("Restar");
        Button multiplicar =  new Button("Multiplicar");
        Button dividir =  new Button("Dividir");
 
 
        GridPane grid =  new GridPane();
        grid.setVgap(10);
        grid.setHgap(10);
        grid.add(label1, 0, 0);
        grid.add(numero1, 0, 1);
        grid.add(label2, 1, 0);
        grid.add(numero2, 1, 1);
        grid.add(res, 0, 2);
        grid.add(resultado, 0, 3);
        grid.add(sumar, 0, 4, 1, 1);        
        grid.add(restar, 1, 4, 1, 1);      
        grid.add(multiplicar, 0, 5, 2, 1);  
        grid.add(dividir, 1, 5, 2, 1);      
       
        sumar.setOnAction(event -> {
            resultado.setText(String.valueOf(Float.parseFloat(numero1.getText()) + Float.parseFloat(numero2.getText())));
        });
        restar.setOnAction(event -> {
            resultado.setText(String.valueOf(Float.parseFloat(numero1.getText()) - Float.parseFloat(numero2.getText())));
        });
        multiplicar.setOnAction(event -> {
            resultado.setText(String.valueOf(Float.parseFloat(numero1.getText()) * Float.parseFloat(numero2.getText())));
        });
        dividir.setOnAction(event -> {
            resultado.setText(String.valueOf(Float.parseFloat(numero1.getText()) / Float.parseFloat(numero2.getText())));
        });
 
        Scene escena = new Scene(grid, 400, 250);
        stage.setTitle("Calculadora");
        stage.setScene(escena);
        stage.show();
 
    }
 
    public static void main(String[] args) {
        launch();
    }
 
}