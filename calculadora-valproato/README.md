# Calculadora Valproato (Depakene)

Projeto simples em Python para planejar a entrega de Valproato 250 mg e 500 mg.

## Por que eu fiz

Esse programa vai ser usado na farmacia da prefeitura do meu bairro, para evitar desperdicio de medicacoes e de dinheiro publico. A ideia e simples: usar primeiro a sobra que o paciente ja tem em casa e so depois abrir caixas novas.

## Como funciona

- Cada caixa tem 50 comprimidos e nao pode fracionar caixa.
- Voce informa a miligramagem (250 ou 500), os meses, os comprimidos por mes e a sobra inicial.
- O programa calcula mes a mes quantas caixas entregar e quanto sobra para o mes seguinte.

## Como rodar no VSCode

1. Instale o Python 3.10 ou maior.
2. Abra a pasta do projeto no VSCode.
3. Instale a dependencia:

```
pip install -r requirements.txt
```

4. Rode o programa:

```
python app.py
```

## Arquivos

- `app.py` - a tela do programa.
- `calculadora.py` - o calculo mes a mes.
- `requirements.txt` - so tem o customtkinter.

## Aviso

Isso aqui e so uma ajuda para organizar a dispensacao. Nao e orientacao medica.
