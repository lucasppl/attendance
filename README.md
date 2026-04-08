# Branch de Integração Contínua (CI)

> Esta branch foi criada exclusivamente para o desenvolvimento e validação do pipeline de testes automatizados do projeto **[Hello, Python!](https://github.com/lucasppl/attendance/blob/main/README.md)**.

## Objetivo desta Branch
O propósito aqui é servir como um "laboratório isolado". Nela, configuramos o GitHub Actions para verificar a qualidade do código sem risco de afetar a versão estável na branch `main`.

## 🛠️ O que está sendo testado aqui?
- **Build Automático:** Preparação do ambiente Python 3.10.
- **Testes Unitários:** Verificação das funções da classe `SistemaEscolar`.
- **Relatórios JUnit:** Geração automática de evidências de teste em formato XML.
- **Proteção de Deploy:** Validação da regra que impede que códigos com erro ou códigos fora da branch principal sejam publicados.

---
*Nota: Esta branch é temporária e faz parte da atividade prática de Teste de Software.*

![logo](img/logo.png)
