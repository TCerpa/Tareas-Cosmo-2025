import numpy as np
import matplotlib.pyplot as plt

#Método de integración
def trapecio(f,a,b,n):
    h = (b-a)/n
    suma_f=0.
    for k in range(1,n):
        suma_f+= f(a+k*h)
    return h*((f(a)+f(b))/2 + suma_f)
#Definimos E(x)
def E(O_m0,O_l0,z):
    O_k0 = 1-(O_m0+O_l0)
    return 1/np.sqrt(O_m0*(1+z)**3+O_k0*(z+1)**2+O_l0)

#Función definida por partes
def f_K(O_m0, O_l0, z):
    c = 3e5  
    H0=67.66
    O_k0 = 1 - (O_m0 + O_l0)
    #Hacemos la integración de 1/E
    integrando = lambda z: 1/E(O_m0,O_l0,z)   
    integral = trapecio(integrando, 0, z, 500)
    #Definimos los resultados de f para los distintos valores de O_k0
    if O_k0 > 0:  
        return (c/(H0*np.sqrt(O_k0)))*np.sinh(np.sqrt(O_k0)*integral)
    elif O_k0 == 0:  
        return (c/H0)*integral
    else:  
        return (c/(H0*np.sqrt(-O_k0)))*np.sin(np.sqrt(-O_k0)*integral)

#Creamos listas con los valores de O_m0 y O_l0 para luego evaluar la función
O_m0_vals = np.linspace(0.0, 1.1, 50)   
O_l0_vals = np.linspace(-0.5, 1.1, 50)  
#Creamos grillas para cada densidad normalizada. Esto es necesario para un grafico de contorno. Contiene los valores de O_m0 y O_l0, respectivamente.
O_m0_grid, O_l0_grid = np.meshgrid(O_m0_vals, O_l0_vals)
#Creamos una lista de lista para almacenar los valores de f_k(chi) para cada par (O_m0 , O_l0). Tambien necesario para el grafico de contorno.
f_K_values = np.zeros_like(O_m0_grid)

#Aqui recorremos las grillas y llenamos f_K_values para cada par O_m0 y O_l0.
for i in range(len(O_m0_vals)):      
    for j in range(len(O_l0_vals)):  
        #Recuperamos los valores de O_m0 y O_l0 de la grilla.
        O_m0 = O_m0_grid[j, i]  
        O_l0 = O_l0_grid[j, i]  
        #Calculamos el valor de la funciíon y lo almacenamos.
        f_K_values[j, i] = f_K(O_m0, O_l0, z=1.0)

# Creamos el plot de contornos utilizando las grillas.
plt.figure(figsize=(10, 8))
contour = plt.contour(O_m0_grid, O_l0_grid, f_K_values)
plt.clabel(contour, inline=True, fontsize=8) #Label para cada linea. Muestra el valor de f_k(chi) para cada linea en Mpc.
# Línea para universo plano (O_m0 + O_Λ0 = 1)
O_m0_flat = np.linspace(0, 1, 100)
O_l0_flat = 1 - O_m0_flat
plt.plot(O_m0_flat, O_l0_flat, 'r--', linewidth=1, label='Universo plano (O_k0 = 0)')
#Marcamos el punto que representa los valores publicados por Plank para las densidades.
plt.scatter(0.315, 0.685, color='red', s=100, zorder=5, label='Valores Planck = (0.315,0.685)')
#Le damos formato al gráfico.
plt.xlabel('$\Omega_{m,0}$', fontsize=10)
plt.ylabel('$\Omega_{\Lambda,0}$', fontsize=10)
plt.title('Líneas de constante $f_K(\chi)$ para z = 1.0', fontsize=12)
plt.grid(True)
plt.legend(loc='lower right')
plt.xlim(0, 1.)
plt.ylim(-0.5, 1.1)
plt.show()