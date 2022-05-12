# Tradutor de Código Morse

## 1. Desafio: 

Inicie um projeto que tenha o objetivo de criar uma tradução de código morse.

A ideia é ter uma solução que:
-	recebe um código morse e traduz para texto
-	recebe um texto e traduz para código morse

Imagine que o cliente vai enviar "." e "-" e o servidor vai receber estas informações e interpretar o que aquele código morse representa. Ou receber um texto e gerar o código morse correspondente.

Não é necessário você se preocupar com gramática, concordância, frases complexas, este não é o objetivo do desafio.

O objetivo do desafio é você definir uma arquitetura que entregue uma solução de tradução (de código morse para texto e vice-versa) pensando em como esta solução poderia ser criada de forma que fosse o mais escalável possível.

Reflita sobre a arquitetura que você gostaria de usar, que serviços teria e como eles iriam se comunicar. Se você achar interessante usar RabbitMQ, Celery, Redis ou qualquer outra tecnologia similar, sinta-se à vontade para fazer. Se você preferir usar somente Python com Django ou Flask, também é possível. Você é livre para criar a arquitetura que você achar mais interessante.

É importante para a gente você descrever o que motivou suas decisões e, caso você tivesse mais tempo, como seria a evolução desta arquitetura/produto. Para isso, ao entregar esse desafio enviando por e-mail o link do projeto no github/gitlab, nos envie também um documento detalhando essas informações.

Caso você não conheça o código morse, segue uma tabela abaixo que pode te ajudar.

![table_morse](https://user-images.githubusercontent.com/82230820/167986087-36b64bde-a902-43dc-b4dd-72c94863265c.jpg)

## 2. Stack de desenvolvimento:

**Front-end**

`HTML` e `CSS`
  
Stacks utilizadas para estruturar os elementos das páginas e definir a aparência da interface.

**Back-end**

`FLASK`

A escolha do microframework se deu a partir da análise da complexidade do desafio. Como esta aplicação tem uma estrutura simples, o Flask corresponde bem ao seu propósito, performando de maneira *ágil* e *modular*. A decisão também foi aliada ao fato de ser o primeiro framework em Python que venho estudando para *Residência de Softaware - Porto digital*, justamente por ter uma curva de aprendizado menos complexa quando comparado a outros.

## 3. Instalação e configuração:

Passo a passo:

1. Clone este repositório 
```
git clone https://github.com/marcelle-mascarenhas/codigo-morse.git
```
2. Dentro da pasta raíz, recrie o ambiente virtual
```
python -m venv venv
```
3. Ative o ambiente virtual
```
.\venv\scripts\activate
```
4. Instale o Flask
```
pip install flask
```
5. Comando para executar a aplicação
```
 flask run
 ```
6. Abra um navegador e acesse o link
```
http://127.0.0.1:5000/
```

## 4. Estrutura

Para construção de aplicativos escaláveis e de fácil manutenção, é importante definir a estrutura adequada. Por ser uma aplicação pequena e com poucas funcionalidades, foi implementanda uma estrutura de módulo de arquivo único. 

Na prática, essa estrutura tem uma pasta contendo um arquivo *app.py* como um módulo com suas variáveis de configuração. Na mesma pasta do projeto, temos as pastas *templates* e *static* contendo html e estilos, respectivamente.

```bash
.
├── app.py
├── static
│   └── morse-code.png
│   └── style.css    
├── templates
│   └── encode.html
│   └── decode.html 
│   └── index.html 

```
  #### Detalhamento do arquivo `app.py`
  
 - Import *Flask*;
 - Rotas (pontos de interação) --> .route("/"), .route("/decode)" e .route("/encode)";
 - Funções para codificar e decodificar o código morse: *def encrypt/()* e *def decrypt()*;
 - Método *render_template*: renderiza os arquivos html indicados.


## 5. Fluxo de funcionamento

A página inicial conta com uma interface simples e intuitiva, nela o usuário tem duas opções de escolha:  `CODIFICAR` ou `DECODIFICAR` uma entrada. Ao selecionar a opção desejada será direcionado para página de destino. Caso a escolha seja a opção `CODIFICAR`, o usuário dispõe de dois *inputs*  e um botão `CODIFICAR`, o primeiro input é para inserção dos caracteres, e o segundo (desabilidado) para exibição da conversão. 

Do lado do servidor, as entradas do usuário são verificadas por meio de *expressões regulares* e validadas de acordo com um dicionário - *dict_morse* - usado para mapear todos os simbolos de “texto normal” para suas respectivas traduções de Código Morse. Posteriormente, quando o **.route(/encode)** é acessado, o navegador renderiza o resultado da codificação para o usuário.

## 6.Capturas de tela

**PÁGINA INICIAL**
![tela-inical](https://user-images.githubusercontent.com/82230820/168054096-015ddc61-8a34-459d-9494-99adf1781c79.png)

**CODIFICAR**
![tela-encode](https://user-images.githubusercontent.com/82230820/168054306-7a8253b7-ed4b-4099-a1d0-39044311b8ea.png)

**DECODIFICAR**
![tela-decode](https://user-images.githubusercontent.com/82230820/168054732-100d98ad-4bbb-4dd8-b00a-deab23dd4773.png)

## 7. Escalabilidade

**Sugestão: Cloud Compunting**

Quanto maior a quantidade de requisições nessa aplicação, maior será a preocupação em termos de dimensionamento (escala). Porém, com o sistema hospedado em Cloud existe a facilidade de contar com o uso de escalabilidade, através de ferramentas que automatizam a ampliação ou diminuição de processamento, memória e outras features. 

Algumas vantagens: 

- [x] Menor risco de perda de dados
- [x] Maior capacidade de integração
- [x] Maior velocidade de processamento
- [x] Acessibilidade imediata a informações e aplicações
- [x] Atualizações automáticas
- [x] Economia de custos em termos de instalação e manutenção

## 8.Implementações futuras

- [ ] Tratamento de erros para inputs inválidos (back-end)
- [ ] Tratamento de erros para inputs inválidos (front-end)
- [ ] Iterface flexível e responsiva, adaptando-se a diferentes resoluções de tela.



