import numpy as np
import matplotlib.pyplot as plt
import camb

#Inicializamos el objeto camb que contendrá los parametros cosmológicos.
pars = camb.CAMBparams()
#Seteamos los valores de los parametros cosmológicos. En la documentación de camb aparece lo siguiente:
#H0    = H0; ombh2 = physical density in barions (Omega_b*h^2) (default 0.022); omch2 = physycal density en CDM (Omega_c*h^2) (default 0.12)
#omk   = Omega_K curvature parameter (default 0.0); TCMB  = CMB temperature (default 2.7255)
pars.set_cosmology(H0=67.66, ombh2=0.02242, omch2=0.11933)
#Este método construye y resuelve el modelo cosmológico según los parametros creados y entregados como argumento.
background = camb.get_background(pars)
#Creamos una lista con valores del factor de escala. De 10^-6 (universo temprano) a 10^0 (presente).
a_values = np.logspace(-6, 0, 1000)
#Con los valores de a, calculamos una lista para el redshift.
z_values = (1/a_values)-1 
#Este metodo nos entrega un diccionario que contiene las densidades de cada especie en función del factor de escala.
densidades = background.get_background_densities(a_values,format='dict')
#El diccionario se ordena de la siguiente manera:
#dict_keys(['tot', 'K', 'cdm', 'baryon', 'photon', 'neutrino', 'nu', 'de'])

#En la documentación de camb dice que el método anterior devuelve 8*\pi*G*a^4*rho_i en Mpc. El facto que acompaña a rho_i es 4.885*10**(-27)*a_values**4. Calculado por mi. 
#Entonces, las densidades serán la suma de las especies correspondientes para matter, radiation, dark energy, curvature.
dens_m  = (densidades['cdm']+densidades['baryon']+densidades['nu'])/(4.885*10**(-27)*a_values**4)
dens_r  = (densidades['photon']+densidades['neutrino'])/(4.885*10**(-27)*a_values**4)
dens_de = densidades['de']/(4.885*10**(-27)*a_values**4)
dens_k  = densidades['K']/(4.885*10**(-27)*a_values**4)
#Hacemos el plot de cada densidad en el mismo gráfico.
plt.loglog(a_values,dens_m,label='Matter')
plt.loglog(a_values,dens_r,label='Radiation')
plt.loglog(a_values,dens_de,label='Dark Energy')
plt.loglog(a_values,dens_k,label='Curvature')
plt.xlabel('log[a(z)]')
plt.ylabel('log[rho_i(a)]')
plt.title('Evolución de densidades de especies')
plt.legend()
plt.show()

#######################################################

#Este es un gráfico alternativo que muestra como evolucionan las densidades normalizadas en función del redshift.
Omega_m  = background.get_Omega('cdm',z_values)+background.get_Omega('baryon',z_values)+background.get_Omega('nu',z_values)
Omega_r  = background.get_Omega('photon',z_values)+background.get_Omega('neutrino',z_values)
Omega_de = background.get_Omega('de',z_values)
Omega_k  = 1- (Omega_m+Omega_r+Omega_de)
#Omega_tot=Omega_de+Omega_k+Omega_m+Omega_r #print(Omega_tot) out: 1
plt.loglog(a_values, Omega_m , label='Matter')
plt.loglog(a_values, Omega_r , label='Radiation')
plt.loglog(a_values, Omega_de, label='Dark Energy')
plt.xlabel('log[a(z)]')
plt.ylabel('log[Ω_i(a)]')
plt.title('Evolución de densidades normalizadas de especies')
plt.legend()
plt.show()
