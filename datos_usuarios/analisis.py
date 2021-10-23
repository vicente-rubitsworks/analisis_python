#importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importar los datos
usuarios=pd.read_csv('datos_usuarios/usuario_works.csv', index_col='Id_usuario_works',na_values = 'null')
cod_comuna=pd.read_csv('datos_usuarios/cod_comuna.csv',  encoding='latin1', sep=';')

###mesclar los datos
merge=pd.merge(usuarios, cod_comuna, left_on='Id_comuna', right_on='Código Comuna 2018',how='left')


#crear las variables
agrupar_por_comuna=merge.groupby(['Nombre Comuna'])[['nomb_usuario']].count()
agrupar_por_region=merge.groupby(['Nombre Región'])[['nomb_usuario']].count()


#imprimir los datos

agrupar_por_comuna=agrupar_por_comuna.reset_index()
agrupar_por_region=agrupar_por_region.reset_index()
print(merge.info())

print(agrupar_por_comuna)

#sacar un grafico

x=agrupar_por_region['Nombre Región']
y=agrupar_por_region['nomb_usuario']

fig, ax = plt.subplots()




plt.bar(x,y,width=0.75, color="blue" )

ax.bar_label(ax.containers[0])

plt.savefig('clientes_region_bar.png')

plt.show()


plt.close('all')