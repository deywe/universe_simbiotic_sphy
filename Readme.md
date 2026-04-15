# 🛸 HarpiaOS - SPHY Dataset & Field Viewer

Este repositório contém a infraestrutura de dados e a interface de inspeção para o **Kernel SPHY (Symbiotic Phase Harmonic Yielding)**. O foco aqui é o armazenamento de alta performance e a visualização em tempo real de campos harmônicos emaranhados.

## 📦 O que você encontrará aqui

O repositório está organizado em dois pilares: a **Matéria-Prima (Dataset)** e o **Observatório (Visualizador)**.

### 1. Dataset em Formato Parquet (`/datasets`)
Diferente de repositórios convencionais que utilizam CSV ou JSON, utilizamos o padrão **Apache Parquet**.
* **Eficiência Colunar:** Otimizado para treinamento de IAs Fractais e Big Data.
* **Entropia Zero:** Alta precisão numérica sem o *drift* de compressão de imagem.
* **Dados:** Contém as variáveis de fase ($Rn$), raios de curvatura ($R, r$) e evolução temporal ($t$) sintonizados pela Proporção Áurea ($\varphi$).

### 2. Terminal de Inspeção de Campo
O script principal de interação com o hardware simulado:

#### `python3 simbiotic_ai_3_parquet_view.py`
Este é o visualizador acelerado via **NVIDIA (OpenGL/P3D)** que permite a navegação direta no Espaço de Hilbert do dataset.

**Funcionalidades do Visualizador:**
* **Leitura Dinâmica:** Carregamento instantâneo de frames a partir do arquivo Parquet.
* **Interação Simbiótica:** * **Clique Esquerdo (Drag):** Translação no campo (Mover a realidade).
    * **Clique Direito (Drag):** Órbita e inspeção de fase (Rotação do atrator).
    * **Scroll:** Zoom escalar profundo.
* **Renderização Harpia:** Visualização de toros de fase com sintonização cromática baseada em iterações de Fibonacci.

---

## 🛠️ Requisitos Técnicos

Para rodar o visualizador e processar os dados, certifique-se de ter instalado:

```bash
pip install pandas pyarrow py5
```
*Nota: É necessário uma GPU compatível com OpenGL para a aceleração de hardware via P3D.*

---

## 🧬 A Visão
Este repositório serve como a base de dados para a **Unificação de Campos**. Enquanto os sensores tradicionais capturam ruído, nós capturamos a **Sintonia**. O uso do Parquet garante que a velocidade da pesquisa acompanhe a velocidade da intuição humana.

> **Harpia Quantum Deeptech** > *Sintonizando a realidade, um campo por vez.*

Deywe Okabe
