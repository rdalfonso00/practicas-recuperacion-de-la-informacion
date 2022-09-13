# %% [markdown]
# # Laboratorio 4

# %% [markdown]
# 1. Utilice el archivo generado en el laboratorio 3 con los documentos de la colección de CACM preprocesados.
# 1. Obtengan el vocabulario de la colección utilizando truncamiento. Impriman la longitud del vocabulario. Después de observar el vocabulario resultante, proponga mecanismos para reducirlo. Codifique los mecanismos propuestos. Escriba la longitud del vocabulario reducido. Las longitudes deberán escribirse a pantalla
# 1. Escriban los vocabularios finales a archivos vocabulario.txt y vocabulario_reducido.tx
# 
# 

# %% [markdown]
# ## PREPROCESAMIENTO DE documentos.txt
# 

# %% [markdown]
# Primero extraemos las palabras de documentos_final.txt
# 

# %%

filename = "documentos_trunc.txt"
file = open(filename, 'rt',encoding='utf-8-sig')
text = file.read()
file.close()
import re
words = re.split(r"\n", text)
doc_words = ""
i = 0
for w in words:
    split = re.split(r"\|", w)
    if len(split) == 1:
        continue
    elif len(split) == 4:
        #doc_data[i]['d_num'] = split[0]
        doc_words += split[2] + " "
    doc_words += split[1] + " "
    i = i + 1
print(doc_words[:1000])

# %% [markdown]
#  separamos todas las palabras (omitiendo vacías)

# %%
all_words = [x for x in (doc_words).split(" ") if x]
print(all_words[:100])
print(str(len(all_words)))

# %% [markdown]
# Ahora buscaremos reducir el vocabulario existente

# %%
from collections import Counter

c = Counter(all_words)
#print(c.items())
labels, values = zip(*c.items())
print(labels[:10])
print(values[:10])
print(len(labels))

# %%
# vemos los datos en deciles
import statistics
deciles = statistics.quantiles(values, n=10)
print(deciles)

# %% [markdown]
# Viendo la distribución de los datos en deciles, vemos que la casi mitad de las palabras del vocabulario aparecen en frecuencias cercanas a 1 y 2.
# 
# Se optará por eliminar solamente las palabras con 1 ocurrencia en el vocabulario.

# %%
reduced_words = {k: v for k, v in c.items() if v != 1}
print(len(reduced_words))
print("We deleted " + str(len(labels) - len(reduced_words)) + " words from the vocabulary")

# %% [markdown]
# Vemos que se eliminaron 4,750 palabras, que a mi consideración fueron demasiadas, seguiremos revisando el vocabulario existente.
# 
# Analizaremos la distribución del largo de los términos del vocabulario.

# %%
len_freq_dict = dict()
for w in labels:
    len_freq_dict[len(w)] = 0
for w in labels:
    len_freq_dict[len(w)] = len_freq_dict[len(w)] + 1
len_freq_list = (sorted(len_freq_dict.items()))
len_freq_list

# %%
x = len_freq_list[0][1] +len_freq_list[1][1] + len_freq_list[2][1]
print(str(x / len(labels) * 100)+"%")

# %% [markdown]
# Aquí ya vemos que las palabras con 1, 2 y 3 caracteres que existen en el vocabulario conforman el 14.5% del diccionario, por lo que estas serán las que se eliminarán

# %%
reduced_words = {k: v for k, v in c.items() if len(k) > 3}
print("We deleted " + str(len(labels) - len(reduced_words)) + " words from the vocabulary")

# %% [markdown]
# Por último, las palabras serán escritas a vocabulario.txt y vocabulario_reducido.txt

# %%
voc = ', '.join(list(labels))
reduced_voc = ', '.join(list(reduced_words.keys()))
with open('vocabulario_trunc.txt', 'w') as f:
    f.write(voc)
    f.close()
with open('vocabulario_reducido_trunc.txt', 'w') as f:
    f.write(reduced_voc)
    f.close()
print(len(reduced_words))

