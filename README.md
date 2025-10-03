# PREGUNTA 6:
## Using CAMB, plot the evolution of the density parameters for matter, radiation, dark energy and curvature.

Utilicé las herramientas básicas de camb para setear parametros y obtener el background. Con ello, los métodos de camb permiten obtener directamente las densidades de especie. El primer gráfico muestra la evolución de las densidades de especie en función del factor de escala. Se puede apreciar el periodo en que domina radiación, luego un breve periodo de equivalencia, para luego un periodo en el que domina materia. Finalmente, se observa que domina dark energy. Sin más que agregar, el código contiene los comentarios necesarios.

<img width="640" height="480" alt="Densidades_de_especie" src="https://github.com/user-attachments/assets/f48583ed-0097-4c60-9829-419c7415e051" />

Este segundo gráfico muestra escencialmente lo mismo pero se muestras las densidades de especie normalizadas.
<img width="640" height="480" alt="Densidades_de_especie_norm" src="https://github.com/user-attachments/assets/e6ddb27c-8bfb-4242-9b3b-f426c8473285" />

# Pregunta 7:
## Using Python, plot the lines of constant f_K(χ) in the plane Ωm,0 − ΩΛ,0.

La implementación del código contiene los comentarios necesarios para ver el proceso realizado para resolver el problema.

El gráfico muestra las líneas de igual f_K(χ) en el plano Ωm,0 − ΩΛ,0. Me parecio interesante marcar los valores entregados por Planck para Ωm,0 y ΩΛ,0. Vemos que el punto es intersectado por una de las líneas de contorno (6000 Mpc) y por la línea punteada que representa el Universo plano. Esto es una forma de probar los modelos cosmológicos y muestra que distintos modelos podrían calzar con las observaciones. 

Bajo la línea punteada se obsevan las curvas para un universo abierto (Ωk,0>0) y sobre ella las curvas en universo cerrado (Ωk,0<0).

<img width="1000" height="800" alt="Lineas_constante_f(chi)" src="https://github.com/user-attachments/assets/816fdfea-d194-4f35-8bae-fb7fec17aeb8" />
