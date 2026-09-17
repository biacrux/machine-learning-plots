# Trabalho Prático Final

Trabalho prático de Machine Learning em Python (Jupyter Notebook), com carregamento e análise dos datasets `NFLX.csv` e `precos_estimados.csv`.
O trabalho prático foi feito no RStudio mas aqui vai ser corrido no VSCode.

## Requisitos

- **Python** — [python.org/downloads](https://www.python.org/downloads/)
- **Jupyter Notebook** e a extensão **Jupyter** no VS Code

## Instalação

### 1. Python

Descarregar em [python.org/downloads](https://www.python.org/downloads/)  botão "Download Python 3.x.x".

Confirmar a instalação num terminal:
```
py --version
```

### 2. Jupyter e bibliotecas

```
py -m pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

| Biblioteca | Para quê |
|---|---|
| `jupyter` | correr notebooks `.ipynb` |
| `pandas` | manipular dados em tabelas (DataFrames) |
| `numpy` | operações matemáticas |
| `matplotlib` | criar gráficos |
| `seaborn` | gráficos estatísticos |
| `scikit-learn` | modelos de machine learning (regressão, KNN, métricas) |

### 3. Extensões do VS Code

No separador de Extensões (`Ctrl+Shift+X`):

- **[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** (Microsoft)
- **[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)** (Microsoft)

## Como correr o notebook

1. Abrir a pasta `trab_pratico_final` no VS Code (`File` , `Open Folder`)
2. Abrir o ficheiro `solucao[1].ipynb`
3. Confirmar o kernel Python selecionado, no canto superior direito

## Como ver os gráficos

Os gráficos não aparecem todos de uma vez — é preciso **correr cada célula individualmente**:

- Clicar na célula e premir **Shift + Enter**, ou
- Usar o botão ** Run Cell** ao lado de cada célula

## Estrutura de pastas

```
trab_pratico_final/
├── NFLX.csv              # dataset com dados históricos da Netflix
├── precos_estimados.csv  # dataset de preços estimados
└── solucao[1].ipynb      # notebook com o código e os gráficos
```

## Notas

- Os `.csv` estão na mesma pasta que o notebook, por isso os caminhos no código usam só o nome do ficheiro: `pd.read_csv('NFLX.csv')`
- Se aparecer `ModuleNotFoundError`, falta instalar essa biblioteca: `py -m pip install <nome>`
