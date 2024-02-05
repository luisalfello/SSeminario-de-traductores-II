# Seminario-de-traductores-II
Mini analizador Sintactico con objetos

AVISO: ESTA VERSIÓN DEL PROYECTO TIENE LA MISMA FUNCIONALIDAD DEL ANTERIOR, SOLO QUE SE TRABAJA CON OBJETOS, CADA ELEMENTO DE LA PILA PUEDE SER:

- ESTADO.

- TERMINAL.

- NO TERMINAL.

SE ANEXAN MODIFICACIONES AL FINAL.

En este trabajo analizaremos los elementos de la cadena, solo aplicando dos reglas:

R1 = E -> id + E

R2 = E -> id

Metodo:
Utilizaremos un elemento de tipo pila, en el cual añadiremos los elementos analizados, y el desplazamiento, este lo obtendremos por medio de la siguiente tabla:

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/afe00c0a-ea71-4c76-94f3-dcc67c529468)
PROGRAMADA:
![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/ea71a9d0-83ac-4aad-a073-8a8f74030bd4)

Obteniendo las filas según el desplazamiento y las columnas segun el caracter analizado.
Si el desplazamiento es postivo, entonces haremos una adicion en la pila, del elemento analizado de la cadena y el desplazamiento.
Si es negativo se hara una reduccion, según la regla, si es R1 seran 6 reducciones, si es R2 seran 2 reducciones.


Pruebas:

Ejercicio1



Ejercicio2

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/e43c1d15-9cae-4b89-8802-79d955e47fba)

Regla 2

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/9fcfd2f9-2777-4279-82c2-d3a5536fb892)

Caso error

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/0cbfe214-547f-48aa-9672-30eb01938473)

---------------------------------------------------------------
------------Modificaciones a la version anterior---------------
---------------------------------------------------------------

Pila:

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/0c39671a-20fb-4a45-8365-07857a789cd6)


Clases agreagadas:

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/d95aa6f8-6e78-4842-ad6c-0aea6fe2bd34)


Se agregan elemntos a la pila segun el tipo:

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/0fb93533-6d24-44d5-aa0f-766a8bb7f279)

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/0ac857d2-cdf7-4ade-9795-af53bb33c406)

