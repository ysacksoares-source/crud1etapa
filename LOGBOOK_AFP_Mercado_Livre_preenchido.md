# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

> **Nota de preenchimento:** este arquivo contém um rascunho orientado ao CRUD do Mercado Livre. Confira cada descrição com seu código e com o que realmente ocorreu nas aulas. Não invente commits, erros, feedbacks, testes ou revisões. O **Campo 01** e o **Checkpoint Conceitual** devem ser respondidos individualmente, sem consulta, conforme a regra do professor. Os dados pessoais, links e revisões por pares que não foram informados permanecem sinalizados para completar.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Ysack Lima Soares *(confirme a grafia como deseja entregar)* |
| **Curso / Módulo** | IA02AV |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | Mercado Livre — cadastro e gerenciamento de anúncios de produtos |
| **Link do meu repositório** | https://github.com/ysacksoares-source/crud1etapa.git |
| **Dupla de revisão (Campo 05)** | KAIO HENRIQUE |
| **Função neste ciclo** | Ysack Lima Soares · Kaio henrique |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ⬜ | ⬜ |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ⬜ | ⬜ |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ⬜ | ⬜ |
| 1 | Campo 02 — Aprofundamento | 16/11 | ⬜ | ⬜ |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ⬜ | ⬜ |
| 2 | Checkpoint Conceitual | 21/11 | ⬜ | ⬜ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ⬜ | ⬜ |
| 2 | Campo 04 — Interação com IA | 21/11 | ⬜ | ⬜ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [ ] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [ ] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [ ] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [ ] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [ ] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** Definir o aplicativo-base e preparar o ambiente para desenvolver um CRUD de anúncios de produtos inspirado no Mercado Livre.
2. **O que implementei (commits / arquivos / links):** Escolhi o Mercado Livre como referência e defini os dados principais de um anúncio: código, nome, preço, quantidade em estoque e categoria. _Confirmar quais arquivos e commits foram realmente criados._
3. **Objeto(s) de conhecimento mobilizado(s):** Modelagem inicial dos dados (*schema*), lógica de programação, ambiente de desenvolvimento, VS Code, Python, Git e GitHub. O Git registra as alterações e permite acompanhar a evolução do código.
4. **Desvio ou erro encontrado + causa técnica:** _Registrar o problema real de instalação/configuração, se ocorreu. Se não houve, escrever: não identifiquei erro técnico nesta etapa._
5. **Decisão de ajuste + fonte:** Organizar os dados do anúncio antes de programar, separando cada informação em uma variável. Fonte de estudo: material da aula e documentação oficial do Python (https://docs.python.org/3/).
6. **Feedback recebido e o que mudei:** _Preencher com o feedback real do professor ou colega; se não houve, registrar que não houve devolutiva nesta etapa._
7. **Próximo passo:** Implementar a entrada e a exibição dos dados de um produto, conferindo os tipos de cada campo.

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. _Preencher individualmente, sem consulta, durante o tempo orientado pelo professor._
2. _Preencher individualmente, sem consulta._
3. _Preencher individualmente, sem consulta._
4. _Opcional — preencher individualmente._

**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. _Preencher sem consulta: qual validação de entrada ainda não domino?_
2. _Preencher sem consulta: como identificar um produto pelo seu código/ID?_
3. _Preencher sem consulta: como impedir atualização ou exclusão de um produto inexistente?_

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> _Escreva sua hipótese inicial sem consultar este documento, materiais ou IA. Depois de registrar e fazer o commit, não altere este campo._

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** Python Software Foundation. *Python 3 — documentação oficial: Built-in Functions (`input`, `int`, `float`, `str`) e Tutorial — Input and Output*. https://docs.python.org/3/ — **Contribuição:** orienta a leitura dos dados digitados pelo usuário e a conversão de tipos. Isso ajuda a evitar que preço e quantidade permaneçam como texto e provoquem comparações ou cálculos incorretos.
- **Referência 2:** Allen B. Downey. *Think Python: How to Think Like a Computer Scientist*, 2ª edição, capítulos sobre variáveis, expressões, condicionais, iteração e estruturas de dados. https://greenteapress.com/wp/think-python-2e/ — **Contribuição:** ajuda a organizar a lógica do cadastro de produtos, aplicar condições e percorrer os registros para localizar, alterar ou excluir um anúncio.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> A hipótese inicial é que as falhas do CRUD podem estar relacionadas à entrada de dados sem validação, à conversão incorreta entre texto e números e à identificação inadequada dos produtos. A pesquisa reforçou essa hipótese e mostrou que também é necessário verificar se o produto existe antes de atualizar ou excluir, além de testar entradas vazias, preços inválidos e códigos repetidos.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| Ambiente Python e VS Code | 1 ambiente configurado | Executar e depurar o programa em Python. |
| Casos de teste | 12 casos (mínimo) | Cobrir cadastro, consulta, atualização, exclusão e entradas inválidas. |
| Registros de produtos | 10 registros fictícios | Testar produtos válidos, códigos repetidos, preço negativo e campos vazios. |
| Tempo de estudo e teste | 4 horas iniciais | Revisar tipos, condicionais, laços e estruturas de dados e corrigir os erros encontrados. |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** Representar os dados de um anúncio do Mercado Livre usando variáveis, tipos de dados e entrada/saída.
2. **O que implementei (commits / arquivos / links):** Planejei/implementei a leitura de código, nome, preço e quantidade por meio de `input()` e a apresentação dos dados com `print()`. _Ajustar conforme o código realmente feito._
3. **Objeto(s) de conhecimento mobilizado(s):** Variáveis; tipos `str`, `int` e `float`; entrada com `input()`; saída com `print()`; conversão de tipos; atribuição.
4. **Desvio ou erro encontrado + causa técnica:** Como `input()` retorna texto, uma tentativa de comparar preço diretamente com número pode gerar resultado incorreto ou erro de tipo. A causa é a ausência de conversão para `float` ou `int`.
5. **Decisão de ajuste + fonte:** Converter preço com `float()` e quantidade/código numérico com `int()` antes de realizar cálculos ou comparações. Fonte: documentação oficial do Python, funções embutidas (`int`, `float`, `input`).
6. **Feedback recebido e o que mudei:** _Preencher com o feedback real; não inventar comentário do professor ou colega._
7. **Próximo passo:** Adicionar validações para impedir preço negativo, quantidade inválida e campos obrigatórios vazios.

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** Aplicar operadores e representar o fluxo de cadastro e consulta de produtos por meio de um fluxograma.
2. **O que implementei (commits / arquivos / links):** Modelei o fluxo de entrada dos dados, cálculo de valor total (preço × quantidade) e exibição das informações. _Confirmar se foi feito fluxograma e quais arquivos foram alterados._
3. **Objeto(s) de conhecimento mobilizado(s):** Operadores aritméticos (`+`, `-`, `*`, `/`), relacionais (`==`, `!=`, `>`, `<`, `>=`, `<=`) e lógicos (`and`, `or`, `not`); tipos `str`, `int` e `float`; sequência de instruções e fluxograma.
4. **Desvio ou erro encontrado + causa técnica:** Uma condição pode apresentar resultado diferente do esperado quando os operadores são usados sem considerar a precedência ou quando `=` é confundido com `==`. Verificar se esse erro realmente ocorreu no código.
5. **Decisão de ajuste + fonte:** Separar as expressões com parênteses quando isso melhora a leitura e usar `==` nas comparações. Fonte: documentação Python — Expressions e Operators (https://docs.python.org/3/reference/expressions.html).
6. **Feedback recebido e o que mudei:** _Registrar a orientação recebida e a alteração realmente realizada; se não houve feedback, informar isso._
7. **Próximo passo:** Usar estruturas condicionais para validar os dados antes de aceitar um anúncio.

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** Utilizar `if`, `elif` e `else` para aplicar regras de negócio no cadastro e na consulta de anúncios.
2. **O que implementei (commits / arquivos / links):** Planejei/implementei verificações para campos obrigatórios, preço maior que zero, quantidade não negativa e opção válida no menu. _Confirmar o que existe no programa._
3. **Objeto(s) de conhecimento mobilizado(s):** Estruturas condicionais; expressões booleanas; comparação entre números; validação de entrada; regras de negócio.
4. **Desvio ou erro encontrado + causa técnica:** Uma entrada vazia ou um valor numérico negativo pode passar pelo cadastro se a condição verificar apenas se o campo foi preenchido. A causa é uma validação incompleta.
5. **Decisão de ajuste + fonte:** Validar separadamente presença do nome, preço positivo e quantidade não negativa antes de cadastrar. Fonte: documentação Python — Compound statements (`if`).
6. **Feedback recebido e o que mudei:** _Preencher com o feedback real do professor/colega ou informar que não houve devolutiva._
7. **Próximo passo:** Combinar condicionais aninhadas e operadores lógicos para validar mais de uma regra ao mesmo tempo.

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ ] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [ ] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [ ] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [ ] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [ ] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** | _…_ |
| **Data de realização** | _…_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. A entrada recebida por `input()` é texto, mesmo quando representa preço ou quantidade; por isso a conversão e a validação precisam acontecer antes dos cálculos. — *Objeto de conhecimento:* tipos de dados e conversão.
2. Uma operação de alteração ou exclusão precisa localizar o produto pelo código e confirmar que ele existe antes de modificar a coleção. — *Objeto de conhecimento:* busca, estruturas de dados e condicionais.
3. _Acrescente um achado observado nos seus testes, se houver._

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** O planejamento inicial considerava que bastaria receber os campos do anúncio e armazená-los; durante os testes, foi necessário prever também dados vazios, tipos incorretos e códigos não encontrados. _Confirme se esse desvio ocorreu no seu desenvolvimento._
- **Causa técnica:** A entrada do usuário não garante que o dado esteja no formato esperado; `input()` retorna `str`, e a existência do registro precisa ser verificada antes da atualização ou exclusão.

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** validar os campos obrigatórios, converter preço e quantidade para tipos numéricos e verificar a existência do código antes de alterar ou excluir o produto.
- **Fonte:** documentação oficial do Python — funções embutidas, estruturas condicionais e estruturas de dados: https://docs.python.org/3/.

**Objeto de conhecimento mobilizado nesta decisão:** validação de entrada, conversão de tipos, estruturas condicionais e busca em estrutura de dados.

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** ChatGPT (OpenAI)  **Data:** 16/11/2026

**4b. Pergunta formulada (transcrita integralmente):**

> “Meu aplicativo-base do CRUD é: Mercado Livre. Pode preencher o Logbook.”

**4c. Resposta da IA (resumida em parágrafo):**

> A IA organizou um rascunho do Logbook em torno de um CRUD de anúncios de produtos, relacionando cadastro, consulta, atualização e exclusão aos conteúdos de Python. Também indicou que os registros de commits, erros, feedbacks e testes precisam ser conferidos com o que realmente aconteceu no projeto.

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> Aceitei a organização dos conceitos e a ideia de validar entradas, converter tipos e conferir a existência do produto antes de atualizar ou excluir. Esses pontos se relacionam a tipos de dados, condicionais, funções e estruturas de dados.

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> Não tratei como fatos os exemplos de erros, commits, feedbacks ou testes que a IA sugeriu. Eles precisam ser comparados com o código e com o histórico real do Git. Também não aceitei preencher o Campo 01 ou o Checkpoint por consulta, pois o próprio protocolo exige realização individual sem consulta. A validação final deve ser feita executando o programa e conferindo a documentação oficial do Python.

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** Combinar condições para aceitar apenas anúncios que respeitem as regras de cadastro.
2. **O que implementei (commits / arquivos / links):** Planejei testar a validação de nome preenchido, preço positivo e quantidade não negativa antes de concluir o cadastro.
3. **Objeto(s) de conhecimento mobilizado(s):** Condicionais aninhadas; operadores lógicos `and`, `or` e `not`; expressões booleanas; tabela-verdade.
4. **Desvio ou erro encontrado + causa técnica:** Se uma condição usar `or` quando deveria exigir que todos os requisitos fossem verdadeiros, um anúncio inválido pode ser aceito.
5. **Decisão de ajuste + fonte:** Usar `and` quando todas as condições precisam ser atendidas e testar casos válidos e inválidos. Fonte: documentação Python — Boolean operations.
6. **Feedback recebido e o que mudei:** Preencher com a devolutiva real da P1 ou do professor; não presumir nota ou erro específico.
7. **Próximo passo:** Executar testes com combinações diferentes de nome, preço e quantidade.

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** Repetir operações do menu e percorrer os registros de produtos com laços de repetição.
2. **O que implementei (commits / arquivos / links):** Planejei usar `while` para manter o menu ativo até a opção de saída e `for` para percorrer registros em uma listagem, caso a versão do projeto já utilize coleção.
3. **Objeto(s) de conhecimento mobilizado(s):** Laços `while` e `for`; condição de parada; contador; `break`; `continue`; iteração.
4. **Desvio ou erro encontrado + causa técnica:** Uma condição de parada incorreta pode manter o menu em execução ou encerrar o programa antes da hora. _Descrever apenas se isso ocorreu de fato._
5. **Decisão de ajuste + fonte:** Definir explicitamente a opção de saída do menu e revisar a atualização da variável de controle. Fonte: Python Tutorial — More Control Flow Tools.
6. **Feedback recebido e o que mudei:** _Inserir o erro e a correção apontados na devolutiva real da P1. Se não recebeu devolutiva, registrar isso._
7. **Próximo passo:** Testar a repetição do menu e a saída do programa em diferentes opções.

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** Armazenar vários anúncios e percorrer os registros para exibir o catálogo.
2. **O que implementei (commits / arquivos / links):** Na evolução do projeto, planejei reunir os anúncios em uma lista e percorrer os elementos para apresentar os produtos cadastrados. _Confirmar se a implementação já usa lista._
3. **Objeto(s) de conhecimento mobilizado(s):** Listas; índices; elementos; `append()`; `remove()`; `len()`; iteração com `for`; acesso por posição.
4. **Desvio ou erro encontrado + causa técnica:** Uma busca por índice pode falhar quando a posição não existe, causando `IndexError`. A causa é acessar uma posição fora do intervalo da lista.
5. **Decisão de ajuste + fonte:** Verificar o tamanho da lista antes de acessar uma posição e percorrer os elementos diretamente quando o índice não for necessário. Fonte: Python Tutorial — Data Structures.
6. **Feedback recebido e o que mudei:** _Registrar o feedback real recebido ou informar que não houve devolutiva._
7. **Próximo passo:** Organizar cada produto com seus campos e permitir localizar um anúncio pelo código.

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** Localizar anúncios pelo código e organizar os atributos de cada produto.
2. **O que implementei (commits / arquivos / links):** Planejei testar a busca pelo código do produto e, na evolução das estruturas, representar cada anúncio por pares de chave e valor. _Confirmar a estrutura realmente usada._
3. **Objeto(s) de conhecimento mobilizado(s):** Dicionários; chave e valor; busca; igualdade; tipos de dados; matrizes/listas de registros.
4. **Desvio ou erro encontrado + causa técnica:** Uma busca pode falhar se o código estiver armazenado como texto e for procurado como inteiro, pois `"2"` é diferente de `2`; também pode falhar por chave escrita incorretamente.
5. **Decisão de ajuste + fonte:** Padronizar o tipo do código e o nome das chaves e verificar se a chave existe antes de acessar seu valor. Fonte: Python Tutorial — Dictionaries.
6. **Feedback recebido e o que mudei:** _Preencher com a devolutiva real do professor/colega._
7. **Próximo passo:** Implementar atualização e exclusão com verificação prévia da existência do código.

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ ] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ ] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [ ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** Completar as quatro operações do CRUD para gerenciar anúncios de produtos.
2. **O que implementei (commits / arquivos / links):** Planejei concluir `Create`, `Read`, `Update` e `Delete`: cadastrar, listar/buscar, alterar e excluir anúncios. _Anexar os arquivos e commits reais._
3. **Objeto(s) de conhecimento mobilizado(s):** CRUD; estruturas de dados; busca por identificador; validação de existência; atualização de campos; remoção de registros.
4. **Desvio ou erro encontrado + causa técnica:** Atualizar ou excluir um código inexistente pode provocar erro ou alterar o registro errado se a busca não confirmar a correspondência.
5. **Decisão de ajuste + fonte:** Pesquisar o código antes de atualizar/excluir e informar quando o produto não for encontrado. Fonte: documentação Python sobre listas/dicionários e testes de condição.
6. **Feedback recebido e o que mudei:** _Inserir o feedback real da revisão por pares e a mudança feita; não inventar nome de colega._
7. **Próximo passo:** Testar as quatro operações com códigos existentes e inexistentes.

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | _preencher com o nome real do colega_ |
| **Repositório revisado** | _colar o link real do repositório do colega_ |
| **Revisor** | Ysack Soares *(confirmar grafia)* |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 21/10_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** Separar as responsabilidades do CRUD em funções para reduzir repetição e facilitar manutenção.
2. **O que implementei (commits / arquivos / links):** Planejei dividir o programa em funções como `cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()` e `menu()`, conforme a estrutura efetivamente implementada.
3. **Objeto(s) de conhecimento mobilizado(s):** Funções; parâmetros; argumentos; retorno com `return`; escopo local e global; modularização.
4. **Desvio ou erro encontrado + causa técnica:** Uma função pode não produzir o resultado esperado quando não retorna o valor encontrado ou depende de variável definida em outro escopo.
5. **Decisão de ajuste + fonte:** Passar os dados necessários como parâmetros e retornar o resultado da busca para a função chamadora. Fonte: Python Tutorial — Defining Functions.
6. **Feedback recebido e o que mudei:** _Registrar o feedback verdadeiro da peer review e a refatoração correspondente._
7. **Próximo passo:** Revisar as funções e verificar se cada uma tem uma responsabilidade clara.

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** Compreender a recursividade e identificar quando uma função chama a si mesma.
2. **O que implementei (commits / arquivos / links):** Estudei a estrutura de uma função recursiva, com caso base e chamada recursiva; _descrever aqui se e onde isso foi aplicado no CRUD_.
3. **Objeto(s) de conhecimento mobilizado(s):** Recursividade; caso base; chamada recursiva; pilha de execução; condição de término.
4. **Desvio ou erro encontrado + causa técnica:** Sem caso base, uma função recursiva pode continuar chamando a si mesma até atingir o limite de recursão. A causa é não definir uma condição de parada.
5. **Decisão de ajuste + fonte:** Definir um caso base que encerre as chamadas e garantir que cada chamada aproxime o problema desse caso. Fonte: Python Tutorial — Python functions e documentação sobre limites de recursão.
6. **Feedback recebido e o que mudei:** _Registrar a orientação real recebida ou informar que não houve feedback._
7. **Próximo passo:** Praticar a explicação da pilha de chamadas e comparar uma solução recursiva com uma solução iterativa.

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> Uma decisão que consigo justificar é separar as operações do CRUD e validar os dados antes de alterar o estado do catálogo. A busca pelo código deve acontecer antes da atualização ou exclusão, pois isso evita modificar um produto diferente ou tentar alterar um registro inexistente. Essa escolha se apoia em condicionais, busca em estruturas de dados e modularização. _Manter somente se corresponder ao código que você realmente implementou._

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** ainda preciso ganhar segurança para explicar a recursividade e acompanhar a pilha de execução, além de identificar com rapidez erros de tipo e de escopo.
- **Plano de ação (passos e datas):** até 17/11, revisar um exemplo pequeno de função recursiva e explicar seu caso base; em 17/11, executar testes de cadastro, busca, atualização e exclusão com entradas válidas e inválidas; antes de 26/11, revisar as funções do CRUD e registrar os resultados reais.

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** Como você garantiria que a atualização de um anúncio não alterasse o produto errado quando o usuário informa um código inexistente ou repetido?
- **Resposta:**

> Primeiro, eu validaria o formato do código recebido e faria uma busca na estrutura de dados.  
> Se nenhum produto correspondesse ao código, o programa informaria que o anúncio não foi encontrado e encerraria aquela operação sem modificar os dados.  
> Se o código fosse encontrado, eu verificaria se ele identifica um único registro, evitando ambiguidades.  
> Só depois dessas verificações a função de atualização receberia o produto e aplicaria as mudanças nos campos permitidos.  
> Por fim, eu testaria os casos de código existente, inexistente e repetido para confirmar que os demais anúncios permanecem iguais.

**Objeto de conhecimento mobilizado:** busca, validação de entrada, estruturas condicionais, funções e integridade dos dados.
**Fonte:** documentação oficial do Python — estruturas de dados e definição de funções: https://docs.python.org/3/tutorial/.

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** Refatorar o CRUD para melhorar legibilidade, organização e facilidade de manutenção.
2. **O que implementei (commits / arquivos / links):** Planejei revisar nomes de variáveis e funções, reduzir trechos repetidos, separar responsabilidades e organizar validações. _Indicar os arquivos/commits efetivamente alterados._
3. **Objeto(s) de conhecimento mobilizado(s):** Refatoração; legibilidade; coesão; duplicação de código; modularização; testes de regressão.
4. **Desvio ou erro encontrado + causa técnica:** Uma alteração em uma função compartilhada pode afetar outras operações do CRUD se não houver testes de regressão.
5. **Decisão de ajuste + fonte:** Fazer pequenas alterações e testar novamente cadastro, consulta, atualização e exclusão após cada refatoração. Fonte: Python Tutorial e PEP 8 — Style Guide for Python Code (https://peps.python.org/pep-0008/).
6. **Feedback recebido e o que mudei:** _Inserir o feedback real da segunda revisão por pares e o que foi modificado._
7. **Próximo passo:** Executar testes finais com dados válidos, inválidos, ausentes e repetidos e registrar os resultados.

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | _preencher com o nome real do colega_ |
| **Repositório revisado** | _colar o link real do repositório do colega_ |
| **Revisor** | Ysack Soares *(confirmar grafia)* |
| **Ciclo / data** | _Ciclo 12 · 11/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> No início, eu entendia o CRUD principalmente como um conjunto de opções para cadastrar, mostrar, alterar e apagar produtos. Minha hipótese era que as falhas surgiriam principalmente na digitação dos dados. Ao longo do conteúdo, passei a considerar também os tipos de dados, as condições de validação, a busca pelo identificador, a organização dos registros e a separação das responsabilidades em funções. _Compare este texto com o que você realmente escreveu no Campo 01 e ajuste sem alterar o Campo 01._

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| Tipos de dados e validação | Eu não considerava que `input()` sempre retorna texto. | Aprendi a converter os valores para `int` ou `float` e validar campos antes de aceitar um anúncio. | Registro do Ciclo 02 e Campo 02. |
| Condicionais e laços | Eu tinha dificuldade para combinar regras e controlar a repetição do menu. | Aprendi a usar `if/elif/else`, operadores lógicos e laços com condição de parada. | Registros dos Ciclos 03, 04, 05 e 06. |
| Estruturas de dados e funções | Eu não separava claramente os dados do produto das operações realizadas sobre ele. | Aprendi a organizar registros em estruturas adequadas, buscar pelo código e dividir o CRUD em funções com responsabilidades específicas. | Registros dos Ciclos 07, 08, 09 e 10.

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** considerar que o valor digitado por `input()` já é numérico — **Correção:** converter explicitamente para `int` ou `float` e validar antes de calcular ou comparar.
   **O que corrigiu:** estudo dos tipos de dados, testes de entrada e consulta à documentação oficial do Python.
2. **Equívoco:** acreditar que atualizar ou excluir pode ser feito sem verificar se o produto existe — **Correção:** realizar a busca pelo identificador e tratar o caso em que não há correspondência.
   **O que corrigiu:** estudo das estruturas de dados, condicionais e testes do CRUD.

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> Em um sistema de biblioteca, por exemplo, as mesmas operações podem gerenciar livros: cadastrar título e autor, localizar um livro pelo código, atualizar seus dados e excluir um registro. A validação evita aceitar quantidade negativa de exemplares, e a busca impede alterar um livro inexistente. As funções podem separar cada operação e facilitar a manutenção do sistema.

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> Ainda preciso aprofundar o tratamento de exceções, a validação de entradas em diferentes formatos, a recursividade e a escrita de testes automatizados. Também preciso praticar a explicação do fluxo completo do programa sem depender do Logbook e conferir se cada função trata corretamente registros inexistentes e dados inválidos.

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | Ysack Soares *(confirmar grafia)* |
| **Curso / Time / Função** | _preencher curso/período; autor do CRUD Mercado Livre e revisor por pares_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _preenchimento reservado ao professor após a defesa._

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11
1. **O que apresentei/defendi (em 1 frase):** _preencher depois da defesa, descrevendo o que realmente apresentou._
2. **Objeto(s) de conhecimento que a banca mais explorou:** _preencher com os conceitos efetivamente questionados._
3. **Pergunta que mais me desafiou e como respondi:** _registrar a pergunta real e sua resposta._
4. **O que levo deste semestre para o próximo módulo:** _registrar sua reflexão após a defesa._

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
