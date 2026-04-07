from attendance import SistemaEscolar
import os

# teste funcional: verifica se a função de adicionar aluno está funcionando corretamente
def test_adicionar_aluno():
    escola = SistemaEscolar(arquivo_db="teste_db.json") # banco simulado para o teste
    escola.lista_alunos = [] # Limpa a lista para o teste
    
    escola.adicionar_aluno("Aluno Teste")
    
    # VERIFICAÇÃO (assert para confirmar que a condição é verdadeira)
    assert len(escola.lista_alunos) == 1
    assert escola.lista_alunos[0]['nome'] == "Aluno Teste"
    
    if os.path.exists("teste_db.json"):
        os.remove("teste_db.json")

# teste propositalmente falho
def test_falha_proposital():
    # Aqui afirmo que 1 é igual a 2, o que é falso. O teste vai estourar um erro.
    assert 1 == 2, "Esse teste falhou propositalmente para demonstração"
