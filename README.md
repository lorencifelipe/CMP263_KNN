# Atividade prática: Algoritmo k-Nearest Neighbors (KNN)

O diretório dataset contém os dados de teste, divididos em "nao_normalizados" e "normalizados". No primeiro subdiretório estão os dados de treinamento e teste não normalizados, enquanto no segundo, seguem os mesmos conjuntos normalizados.

O diretório resultados contém arquivos com os resultados dos testes. Nomenclatura: se extraídos de dados normalizados "normalizado_k.txt", se extraídos de dados não normalizados "nao_normalizado_k.txt" (onde k indica o valor do hiperparâmetro k selecionado). 
A primeira linha de cada arquivo de resultado indica o valor de k testado. A seguir, linha a linha, segue o classificador obtido pelo algoritmo para cada instância (se 0, há indícios de tumor benigno, se 1, há indícios de tumor maligno). Por fim, na última linha segue a acurácia geral dos testes.


