import json
import os
import csv
from datetime import datetime

class SistemaEscolar:
    def __init__(self, arquivo_db="database.json"):
        self.arquivo_db = arquivo_db
        self.lista_alunos = []
        self.carregar_dados() # carrega os dados ao iniciar o sistema

    def adicionar_aluno(self, nome):
        # verifica se o aluno já existe para evitar duplicatas
        if not any(a['nome'] == nome for a in self.lista_alunos):
            self.lista_alunos.append({
                'nome': nome,
                'presencas': 0,
                'faltas': 0,
                'notas': []
            })
            self.salvar_dados()

    def carregar_dados(self):
        # le o arquivo JSON se ele existir e não estiver vazio
        if os.path.exists(self.arquivo_db):
            try:
                # verifica se o arquivo tem conteúdo (tamanho > 0)
                if os.path.getsize(self.arquivo_db) > 0:
                    with open(self.arquivo_db, 'r', encoding='utf-8') as f:
                        self.lista_alunos = json.load(f)
                    print(f"✅ {len(self.lista_alunos)} alunos carregados.")
                else:
                    print("Arquivo de dados vazio. Iniciando nova lista.")
                    self.lista_alunos = []
            except json.JSONDecodeError:
                print("Erro ao ler arquivo JSON (corrompido). Iniciando nova lista.")
                self.lista_alunos = []
        else:
            print("Nova base de dados iniciada.")

    def salvar_dados(self):
        # Salva o estado atual da lista no arquivo JSON
        with open(self.arquivo_db, 'w', encoding='utf-8') as f:
            json.dump(self.lista_alunos, f, indent=4, ensure_ascii=False)

    def realizar_chamada(self):
        print("\n=== LISTA DE ALUNOS ===")
        for i, aluno in enumerate(self.lista_alunos):
            print(f"[{i:02d}] {aluno['nome']}")
        
        entrada = input("\nIDs Faltosos (separados por espaços): ")
        indices_faltosos = [int(x) for x in entrada.split()]

        for i, aluno in enumerate(self.lista_alunos):
            if i in indices_faltosos:
                aluno['faltas'] += 1
            else:
                aluno['presencas'] += 1
        
        self.salvar_dados()
        print("Chamada salva!")

    def lancar_nota(self, indice, nota):
        if 0 <= indice < len(self.lista_alunos):
            self.lista_alunos[indice]['notas'].append(nota)
            self.salvar_dados()

    def gerar_csv_aula(self):
        data_hoje = datetime.now().strftime("%d-%m-%Y")
        nome_arq = f"aula_{data_hoje}.csv"
        with open(nome_arq, 'w', newline='', encoding='utf-8-sig') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Nome', 'Faltas Acumuladas', 'Média'])
            for a in self.lista_alunos:
                media = sum(a['notas'])/len(a['notas']) if a['notas'] else 0
                escritor.writerow([a['nome'], a['faltas'], f"{media:.2f}"])
        print(f"📊 CSV gerado: {nome_arq}")

if __name__ == "__main__":
    escola = SistemaEscolar()
    
    # se a lista estiver vazia, adiciona um aluno para teste
    if not escola.lista_alunos:
        escola.adicionar_aluno("aluno")
    
    escola.realizar_chamada()
    escola.gerar_csv_aula()
