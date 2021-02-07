import csv

#Distância Euclidiana 
def euclidean(xi,xj):
    soma = 0
    for l in range(0,30):
        soma+=(float(xi[l])-float(xj[l]))**2
    result = soma**0.5 
    return result

#Leitura de arquivo de treino e de teste
def read_files(train,test):
    treino = []
    teste = []
    with open('dataset'+train,'r') as cancer_train:
        data = csv.reader(cancer_train, delimiter = ',')
        for line in data:
            treino.append(line)
    with open('dataset'+test,'r') as cancer_test:
        data = csv.reader(cancer_test, delimiter = ',')
        for line in data:
            teste.append(line)
    return(treino,teste)

#Retorna valor da distância euclidiana
def getEuclidean(e):
    return e[1]

#Cálculo da acurácia
def acuracia(result, teste):
    n = len(result)
    hits = 0
    i = 0
    while(i<n):
        if(result[i]==int(float(teste[i+1][30]))):
            hits+=1
        i+=1
    return(hits/n)

#Knn        
def knn():
    k = int(input("Insira o valor de k: "))
    #Comente/descomente as linhas 44 e 45 para selecionar o carregamento de dados normalizados ou não normalizados
    treino, teste = read_files('/normalizados/cancer_train.csv','/normalizados/cancer_test.csv') #Normalizados
    #treino, teste = read_files('/nao_normalizados/cancer_train.csv', '/nao_normalizados/cancer_test.csv') #Não normalizados
    d = []
    k_nearest_target = []
    result = []
    maligno, benigno = 0, 0
    for i in range(1,len(teste)):
        for j in range(1,len(treino)):
            d.append([j,euclidean(teste[i],treino[j])])
        d.sort(key = getEuclidean)
        for x in range(k):
            index = d[x][0]
            k_nearest_target.append(int(float(treino[index][30])))
        for a in k_nearest_target:
            if(a==0): 
                benigno+=1
            else:
                maligno+=1
        if(benigno>maligno):
            result.append(0)
        else:
            result.append(1)
        d.clear()
        k_nearest_target.clear()
        maligno, benigno = 0, 0    
    #Saída
    print("k =",k)
    for r in result:
        print(r)
    print("Acurácia:",acuracia(result,teste))
knn()
