import csv

def calcular_media_idade(caminho_csv):
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        idades = [int(row['idade']) for row in reader]
        return sum(idades) / len(idades) if idades else 0
