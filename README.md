Claro, aqui está um exemplo de README detalhado para o seu script "DeepFileCopy":

---

# DeepFileCopy

## Descrição
DeepFileCopy é um script Python desenvolvido para copiar arquivos de qualquer tipo de um diretório de origem para um diretório de destino, incluindo todos os arquivos de subdiretórios. O script é ideal para quem precisa organizar grandes volumes de dados, criar backups ou simplesmente transferir arquivos entre diferentes locais no sistema de forma eficiente e ordenada.

## Funcionalidades
- Copia todos os arquivos de um tipo especificado (padrão .pdf) de um diretório e suas subpastas.
- Evita a sobrescrita de arquivos com o mesmo nome, renomeando-os automaticamente.
- Simples de usar, com um código claro e comentado para fácil entendimento.

## Como Usar
1. **Instalação do Python**: Certifique-se de que o Python está instalado em sua máquina. O script foi testado e funciona bem no Python 3.6 ou superior. Caso não tenha o Python instalado, faça o download e a instalação a partir do [site oficial do Python](https://www.python.org/downloads/).

2. **Baixando o Script**: Faça o download do script `DeepFileCopy.py` do repositório.

3. **Configurando o Script**: Abra o script em um editor de texto ou IDE de sua preferência. Altere as variáveis `diretorio_origem` e `diretorio_destino` para os caminhos dos diretórios de origem e destino respectivamente. Opcionalmente, altere a variável `formato` para o tipo de arquivo que deseja copiar (por exemplo, '.txt', '.jpg', etc.).

    ```python
    diretorio_origem = '/caminho/para/diretorio/origem'
    diretorio_destino = '/caminho/para/diretorio/destino'
    formato = '.pdf'  # ou outro formato de arquivo
    ```

4. **Executando o Script**: Após configurar o script, salve as alterações e feche o editor. Abra o terminal ou prompt de comando, navegue até o diretório onde o script está localizado e execute-o com o comando:

    ```
    python DeepFileCopy.py
    ```

5. **Verificando os Resultados**: Após a execução, o script informará quantos arquivos foram copiados. Verifique o diretório de destino para ver os arquivos copiados.

## Contribuições
Contribuições para melhorar o script são sempre bem-vindas. Sinta-se livre para fazer um fork do repositório, propor melhorias ou reportar problemas.
