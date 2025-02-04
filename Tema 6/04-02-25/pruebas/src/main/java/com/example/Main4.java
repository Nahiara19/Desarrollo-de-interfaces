package com.example;

import java.util.List;

public class Main4 {
    public static double obtenerPromedioEdades(List<Integer> edades) {
        int sumaEdades = 0;
        for (int edad : edades) {
            sumaEdades += edad;
        }
        return (double) sumaEdades / edades.size();
    }

    public static void main(String[] args) {
    }
}