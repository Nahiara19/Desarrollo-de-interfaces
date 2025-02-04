package com.example;

import java.util.List;

public class Main2 {
     public static int sumaValoresPares (List<Integer> lista) {
        //sumar valores pares de la lista
        int suma = 0;
        for (Integer valor : lista) {
            if (valor % 2 == 0) {
                suma += valor;
            }
        }
        return suma;
    }
 
    public static void main(String[] args) {
       
    }
}
