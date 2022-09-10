# body performance

* Dataset utilizado: 
https://www.kaggle.com/datasets/kukuroo3/body-performance-data

* Implementação do modelo no Heroku:
https://guarded-hamlet-42190.herokuapp.com/docs

Os dados fornecem diversas informações de pessoas, tais como, idade, pressão sistólica e diastólica, sexo, entre outras, e fornece uma classificação quanto ao desempenho em exercícios com as letras A, B, C e D. Na classificação, a letra A indica o melhor desempenho e a letra D o pior.

## Conteúdo das pastas

### 1_pesquisa_e_desenvolvimento

Contém notebooks com análise dos dados, engenharia de variáveis e pesquisa para a identificação do melhor modelo de classificação possível.

### 2_model_package

Implementação do pipeline do modelo como um pacote. Por meio deste pacote, um modelo pode ser treinado  a partir de um conjunto de dados, e o modelo treinado pode ser utilizado para previsões em novos dados. O pacote construído é utilizado na implementação de uma API

### 3_rest_API 

Código base da API alocada no Heroku. Na construção da API foi utilizado o modelo alocado na pasta 2_model_package.
