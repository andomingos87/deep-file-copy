import os
import shutil

def copiar_arquivos(diretorio_origem, diretorio_destino, formato='.pdf'):
    # Cria o diretório de destino se ele não existir
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    quantidade_copiados = 0  # Contador para os arquivos copiados

    # Percorre o diretório de origem e suas subpastas
    for pasta, _, arquivos in os.walk(diretorio_origem):
        for arquivo in arquivos:
            # Verifica se o arquivo tem a extensão especificada
            if arquivo.lower().endswith(formato):
                # Monta o caminho completo do arquivo de origem e destino
                caminho_origem = os.path.join(pasta, arquivo)
                caminho_destino = os.path.join(diretorio_destino, arquivo)

                # Renomeia o arquivo no destino se já existir um com o mesmo nome
                contador = 1
                nome_base, extensao = os.path.splitext(arquivo)
                while os.path.exists(caminho_destino):
                    novo_nome = f"{nome_base}_{contador}{extensao}"
                    caminho_destino = os.path.join(diretorio_destino, novo_nome)
                    contador += 1

                # Copia o arquivo para o destino
                shutil.copy(caminho_origem, caminho_destino)
                quantidade_copiados += 1

    return quantidade_copiados

# Exemplo de uso do script
diretorio_origem = '/diretorio/de/origem'
diretorio_destino = '/diretorio/de/destino'

# Executa a função e imprime o resultado
quantidade_copiados = copiar_arquivos(diretorio_origem, diretorio_destino)
if quantidade_copiados > 0:
    print(f"Sucesso! {quantidade_copiados} arquivos copiados.")
else:
    print("Nenhum arquivo encontrado ou copiado.")
