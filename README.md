# Seminario-de-traductores-II
Compilador

En esta versión tenemos que analizar una cadena completa, simulado un programa en c, para esto identificaremos los dintintos TOKENS y estos nos regresan un valor el cual tomara como valor una coordenada en la matriz de acciones.

Se utilizaran 52 reglas, cada una con caracteristicas distintas todas esociadas en el archivo: Compilador.lr

En este caso la cadena que se analizara, será la siguiente: 

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/7ebaf3ba-c03c-4e97-a4e0-deaa6c50b383)

Primero analizaremos el archivo: Compilador.lr para extraer la tabla y las reglas.

Despues creamos el objeto analizador sintactico en el cual mandamos las variables anteriores y ademas la cadena la cual haremos el analisis lexico para obtener el tipo de cada token.

Una ves analizamos solo calculamos el elemento que se añadira a la pila, sea un token o una regla y hacemos los pop segun la regla en la que se haya caido

# EJEMPLO

Primeras 9 iteraciones.

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/b8b80c90-0f91-4aee-9fb6-67c7977fac20)

Ultimas 9 iteraciones.

![image](https://github.com/luisalfello/SSeminario-de-traductores-II/assets/84816868/8d3278a5-3d1c-4460-ae4e-55bd697bc9ef)

