# AWS Security Group Extractor

Extrai as regras dos security groups dos serviços da AWS em formato de planilha

## Começando

Estas instruções vão te ajudar a iniciar o projeto.

### Pre-requisitos

- [Python 3](https://www.python.org/downloads/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Usuario IAM na AWS com acesso programático e com a permissão *AmazonEC2ReadOnlyAccess*, *ReadOnlyAccess* ou permissão equivalente;

### Instalando

```
pip install -r requirements.txt
```

### Configuração
Nesse passo, é necessário configurar os usuário IAM que serão utilizados pela aplicação.
Tenha em mãos o AWS ACCESS KEY e o AWS SECRET KEY do usuário.

#### Adicionar o profile default

Você pode adicionar o profile default (padrão) com o comando abaixo.
Esse profile default, é usado pelo script quando não é especificado nenhum profile na execução.

```
aws configure
```

### Adicionar profile extras
Caso queira utilizar mais de um profile, basta executar o comando abaixo, substituindo PROFILE pelo nome do profile desejado.

```
aws configure --profile PROFILE
```

### Executando

Para executar o script com o profile default, basta executar o seguinte comando.
```
python3 aws-sg-extractor.py
```

Para executar o script com o profile desejado, basta executar o seguinte comando.
```
python3 aws-sg-extractor.py --profile PROFILE
```

Caso queira ver a ajuda do comando, basta executar:
```
python3 aws-sg-extractor.py --help
```
