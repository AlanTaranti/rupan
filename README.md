# AWS Info Extractor

Extrai informações dos serviços da AWS em formato de planilha

## Começando

Estas instruções vão te ajudar a iniciar o projeto.

### Pre-requisitos

- [Python 3](https://www.python.org/downloads/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Permissões
    - Módulo Security Groups:
        Usuario IAM na AWS com acesso programático e com a permissão *AmazonEC2ReadOnlyAccess*, *ReadOnlyAccess* ou permissão equivalente;
    - Módulo Access Keys:
        Usuario IAM na AWS com acesso programático e com a permissão *IAMReadOnlyAccess*, *ReadOnlyAccess* ou permissão equivalente;
    - Módulo Buckets:
        Usuario IAM na AWS com acesso programático e com a permissão *AmazonS3ReadOnlyAccess*, *ReadOnlyAccess* ou permissão equivalente;

### Instalando

```
pip install -r requirements.txt
```

### Configuração
Com o AWS CLI instalado, podemos seguir com a configuração.

Nesse passo, é necessário configurar o usuário IAM que será utilizado pela aplicação.
Tenha em mãos o AWS ACCESS KEY e o AWS SECRET KEY do usuário.

#### Adicionar o profile

Você pode adicionar o profile com o comando abaixo.

```
aws configure
```

### Executando

### AWS Security Group Extractor

Para executar o comando, basta executar o seguinte.
```
python3 aws-info-extractor.py security-group
```

### AWS IAM Access Keys Extractor

Para executar o comando, basta executar o seguinte.
```
python3 aws-info-extractor.py access-keys
```

### AWS Buckets Extractor

Para executar o comando, basta executar o seguinte.
```
python3 aws-info-extractor.py buckets
```

### Ajuda

Caso queira ver a ajuda do comando, basta executar:
```
python3 aws-info-extractor.py --help
```
