import unittest
import pandas as pd
from sklearn import metrics

from modelo.configuracoes.config import AppConfig
from modelo.preve_modelo import preve_pipeline
from modelo.processing.gerenciamendo_dados import carrega_dataset
from modelo.configuracoes.caminhos import DADOS_DIR


def test_preve_modelo():

    #carrega os dados
    str_file=DADOS_DIR/AppConfig.nome_dados_teste
    df = carrega_dataset(str_file)    

    #prepara os dados
    var_prev=[var for var in df.columns if var not in ['Unnamed: 0','class','prev_val']]
    X = df[var_prev]

    #faz previsao
    results = preve_pipeline(X)
    y_hat = results.get("predictions")
    print(results.get("predictions")[0])
    #print(type(results))
    #print(y_hat)

    # transformação: dados previstos
    class_map = {0:'C', 1:'D', 2:'A', 3:'B'}
    y_hat = pd.Series(y_hat).map(class_map)

    #precisao
    prec=metrics.accuracy_score(df['class'], y_hat)
    assert prec == 0.7114427860696517, "--Teste--: a precisao nao esta correta"



# ponto de entrada
if __name__=="__main__":
    test_preve_modelo()
