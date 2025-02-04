package com.example;

import java.util.ArrayList;
import java.util.List;

public class Main3 {
    
    public static List<String> obtenerNombresEnMayusculas(List<String> lista){
        //obtener nombres en mayusculas de la lista
        List<String> nombresMayusculas = new ArrayList<>();
        for (String nombre : lista) {
            nombresMayusculas.add(nombre.toUpperCase());
            }
            return nombresMayusculas;
    }
    public static void main(String[] args) {
    }   
}

