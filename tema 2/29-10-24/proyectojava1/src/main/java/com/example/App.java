package com.example;

import javafx.application.Application;
import javafx.beans.binding.StringBinding;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Tooltip;
import javafx.scene.effect.DropShadow;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

/**
 * JavaFX App
 */
public class App extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        //aquí comienza lógicamente la pantalla
        Label label = new Label("Ingrese su nombre:");
         
        //un texto
        TextField campoTexto = new TextField();

        //un boton
        Button boton = new Button("Aceptar");
        Tooltip tooltip = new Tooltip("mensajito que pongo al boton");
        boton.setTooltip(tooltip);

        DropShadow sombra = new DropShadow();
        boton.setEffect(sombra);

        boton.setOnMouseEntered(evento ->  boton.setStyle("-fx-background-color:#ff0000"));
        boton.setOnMouseExited(evento -> boton.setStyle("-fx-background-color:#0000ff"));

        // funcionamiento del boton con funciones lambda
        boton.setOnAction(evento -> {
           String nombre = campoTexto.getText() ;
           System.out.println(nombre);
        });

        //programación tradicional de java 
        /* boton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                String nombre = campoTexto.getText() ;
                System.out.println(nombre);
            }
        }); */
    

        VBox layout = new VBox(10);
        layout.getChildren().addAll(label, campoTexto, boton);

        //crear la escena
        Scene escena =  new Scene(layout, 300, 200);
        stage.setScene(escena);
        stage.setTitle("Mi pantalla");
        stage.show();

    }


    public static void main(String[] args) {
        launch();
    }

}