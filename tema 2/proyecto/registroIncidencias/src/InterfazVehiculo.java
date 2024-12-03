import java.util.HashSet;
import java.util.Set;
import javafx.application.Application;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class InterfazVehiculo extends Application {
    private static TableView<Incidencia> tabla;
    private final ObservableList<Incidencia> datos = FXCollections.observableArrayList();

    public static void main(String[] args) {
        // TODO code application logic here
        launch(args);
    }

    @Override
    public void start(Stage escenario) throws Exception {
        HBox principal = new HBox();

        //escena para contener el layout principal
        Scene escena = new Scene(principal);
        //configuración del escenario 
        escenario.setScene(escena);
        escenario.setTitle("Registro de incidencias");
        //abrir ventana
        escenario.show();

        tabla = new TableView<>();

        TableColumn nomCol = new TableColumn("Nombre");
        nomCol.setMinWidth(200);
        nomCol.setCellValueFactory(new PropertyValueFactory<Incidencia, String>("nombre"));

        TableColumn matCol = new TableColumn("Matricula");
        matCol.setMinWidth(200);
        matCol.setCellValueFactory(new PropertyValueFactory<Incidencia, String>("matricula"));

        tabla.getColumns().addAll(nomCol, matCol);
        tabla.setItems(datos);
        


        VBox secundario = new VBox();

        Double ancholb = 160.0;
        //Nombre
        HBox nom = new HBox();
        Label lb1 = new Label("Nombre:");
        lb1.setPrefWidth(ancholb);
        TextField tx1 = new TextField();
        //Apellidos
        HBox ape = new HBox();
        Label lb2 = new Label("Apellidos:");
        lb2.setPrefWidth(ancholb);
        TextField tx2 = new TextField();
        //Telefono
        HBox tel = new HBox();
        Label lb3 = new Label("Telefono:");
        lb3.setPrefWidth(ancholb);
        TextField tx3 = new TextField();
        //Matricula
        HBox mat = new HBox();
        Label lb4 = new Label("Matricula:");
        lb4.setPrefWidth(ancholb);
        TextField tx4 = new TextField();
        //Modelo
        HBox mod = new HBox();
        Label lb5 = new Label("Modelo:");
        lb5.setPrefWidth(ancholb);
        TextField tx5 = new TextField();
        //Incidencia
        HBox in = new HBox();
        Label lb6 = new Label("Incidencia:");
        lb6.setPrefWidth(ancholb);
        TextArea tx6 = new TextArea();
        tx6.setPrefWidth(200);

        //activar evento click en tabla
        tabla.setOnMousePressed(evento -> {
            System.out.println(evento.getClickCount());
            tx1.setText(tabla.getSelectionModel().getSelectedItem().getNombre());
            tx2.setText(tabla.getSelectionModel().getSelectedItem().getApellidos());
            tx3.setText(tabla.getSelectionModel().getSelectedItem().getTelefono());
            tx4.setText(tabla.getSelectionModel().getSelectedItem().getMatricula());
            tx5.setText(tabla.getSelectionModel().getSelectedItem().getModelo());
            tx6.setText(tabla.getSelectionModel().getSelectedItem().getIncidencia());
        });
        
        
        HBox bn = new HBox(5);
        Button btn = new Button("Insertar");
        btn.setOnAction(evento -> {
            datos.add(new Incidencia(tx1.getText(), tx2.getText(), tx3.getText(), tx4.getText(), tx5.getText(), tx6.getText()));
        });
        Button btn2 = new Button("Modificar");
        btn2.setOnAction(evento -> {
            //recuperar la fila seleccionada
            Incidencia i = tabla.getSelectionModel().getSelectedItem();
            
            //actualizar el obbjeto con los datos de los textfield
            i.setNombre(tx1.getText());
            i.setApellidos(tx2.getText());
            i.setTelefono(tx3.getText());
            i.setMatricula(tx4.getText());
            i.setModelo(tx5.getText());
            i.setIncidencia(tx6.getText());
            
            //refrescar la tabla
            tabla.refresh();
        });
        Button btn3 = new Button("Limpiar");
        btn3.setOnAction(evento -> {
            //limpiar los campos 
            tx1.setText("");
            tx2.setText("");
            tx3.setText("");
            tx4.setText("");
            tx5.setText("");
            tx6.setText("");
        });
        
        bn.getChildren().addAll(btn,btn2,btn3);
        
        nom.getChildren().addAll(lb1, tx1);
        ape.getChildren().addAll(lb2, tx2);
        tel.getChildren().addAll(lb3, tx3);
        mat.getChildren().addAll(lb4, tx4);
        mod.getChildren().addAll(lb5, tx5);
        in.getChildren().addAll(lb6, tx6);

        nom.setPadding(new Insets(15, 12, 15, 12));
        ape.setPadding(new Insets(15, 12, 15, 12));
        tel.setPadding(new Insets(15, 12, 15, 12));
        mat.setPadding(new Insets(15, 12, 15, 12));
        mod.setPadding(new Insets(15, 12, 15, 12));
        in.setPadding(new Insets(15, 12, 15, 12));

        nom.setSpacing(15);
        ape.setSpacing(15);
        tel.setSpacing(15);
        mat.setSpacing(15);
        mod.setSpacing(15);
        in.setSpacing(15);

        btn.setPrefSize(200, 100);
        btn.setAlignment(Pos.CENTER);
        btn2.setPrefSize(200, 100);
        btn2.setAlignment(Pos.CENTER);
        btn3.setPrefSize(200, 95);
        btn3.setAlignment(Pos.CENTER);

        secundario.getChildren().addAll(nom, ape, tel, mat, mod, in, bn);

        principal.getChildren().addAll(tabla, secundario);

    }
}
