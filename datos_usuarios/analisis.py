#importar librerias
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt



#importar los datos
usuarios=pd.read_csv('datos_usuarios/usuario_works.csv',encoding='utf-8', index_col='Id_usuario_works',na_values = 'null',escapechar='\n')
cod_comuna=pd.read_csv('datos_usuarios/cod_comuna.csv',  encoding='latin1', sep=';')

###mesclar los datos
merge=pd.merge(usuarios, cod_comuna, left_on='Id_comuna', right_on='Código Comuna 2018',how='left')



#crear las variables
usuarios['desc_profesional']=usuarios['desc_profesional'].str.strip()
agrupar_por_comuna=merge.groupby(['Nombre Comuna'])[['nomb_usuario']].count()
agrupar_por_region=merge.groupby(['Nombre Región'])[['nomb_usuario']].count()


usuarios['desc_profesional']=usuarios['desc_profesional'].str.upper()
agrupar_por_cat=usuarios.groupby(['desc_profesional'])[['nomb_usuario']].count()


#imprimir los datos

agrupar_por_comuna=agrupar_por_comuna.reset_index()
agrupar_por_region=agrupar_por_region.reset_index()





print(merge.info())

print(usuarios.isna().sum())

agrupar_por_cat=agrupar_por_cat.reset_index()

print(agrupar_por_cat)

#sacar un grafico


x=agrupar_por_cat['desc_profesional']
y=agrupar_por_cat[agrupar_por_cat['nomb_usuario']!=1]

fig, ax = plt.subplots()




plt.bar(y['desc_profesional'] ,y['nomb_usuario'] ,width=0.75, color="blue" )

ax.bar_label(ax.containers[0])

#plt.savefig('clientes_region_bar.png')


plt.show()

plt.close('all')

"""

D =usuarios.isna().sum()

D = D.to_dict()

plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.xticks(rotation=60)



"""