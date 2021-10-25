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

```
aws configure
```

### Executando
```
python3 aws-sg-extractor.py
```
