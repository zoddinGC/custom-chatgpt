
# Custom ChatGPT V1.2

Este projeto foi feito com o intuito de aprender a utilizar a nova API do ChatGPT conhecida como `chatgpt-3.5-turbo` e também de mostrar para pessoas de todas as áreas suas funcionalidades, lugares de uso e limitações.

Assim, qualquer pessoa pode baixar este programa e utilizar em sua máquina para testar. Basta colocar a chave da sua conta do ChatGPT para linkar sua conta ao apliactivo e começar a brincar.

Abaixo há um vídeo que você pode assistir para entender um pouco mais sobre como este aplicativo funciona. Foi desenvolvido 100% em Python.

A base de dados que ele utiliza como conhecimento foi feita em Excel para que todos possam visualizar rapidamente como o ChatGPT entende as mensagens e também para rápida edição das mesmas para bases de conhecimento personalizadas.

&nbsp;
## Instalação

Assista ao **vídeo abaixo** para entender como instalar a aplicação ou siga o tutorial por **escrito abaixo do vídeo**.

### Como instalar (vídeo)

[![COMO INSTALAR CUSTOM CHATGPT](https://github.com/zoddinGC/custom-chatgpt/blob/main/youtube/Installer%20image.png?raw=true)](https://www.youtube.com/watch?v=dvWfFrWAgmo "Instalação Custom ChatGPT")

### Como instalar (instalador.exe)

- Clique na pasta `installer` localizada acima ou [clique aqui](https://github.com/zoddinGC/custom-chatgpt/blob/main/installer/customChatGPT_WINDOWS_1.2_setup.exe)

- Na pasta, clique em **Download** para baixar o instalador

- Após baixar o instalador, basta dar 2 cliques para iniciar a Instalação

- No instalador, selecione a língua desejada, aceite os termos de uso e siga os passos para instalar

- Após clicar em **Instalar** no final, basta iniciar o aplicativo e usar (lembre-se de abrir em modo administrador para editar as bases de conhecimento)

### Como instalar (git clone)

- No terminal git, digite: `git clone https://github.com/zoddinGC/custom-chatgpt/`

- Após baixar os arquivos, digite no terminal da sua IDE `python .\src\CustomBot.py\` ou rode o arquivo `CustomBot.py`

- Pronto, a aplicação já está rodando em seu computador

&nbsp;
## Demonstração

Assista ao vídeo abaixo para entender como a ferramenta funciona e divirta-se!

### Como usar (vídeo)

[![COMO INSTALAR CUSTOM CHATGPT](https://github.com/zoddinGC/custom-chatgpt/blob/main/youtube/Usage%20image.png?raw=true)](https://www.youtube.com/watch?v=3KlVZibOYvE "Instalação Custom ChatGPT")

### Como usar (texto)

- **Página Inicial**
    
    * Botão **COMEÇAR CHAT** irá iniciar o chat com o ChatGPT Original (igual ao site)
    * Botão **EDITAR API KEY** irá trocar de tela para uma nova onde você poderá colocar/editar sua chave API da sua conta <sup>1</sup>
    * Caixa de Seleção **CONHECIMENTO PERSONALIZADO** deve ser marcada caso você queira testar com conhecimento prévio
    * Ao marcar a caixa acima, uma **LISTA SUSPENSA** irá aparecer para selecionar a base de conhecimento
    * Também ao marcar a caixa, um botão de **EDITAR CONHECIMENTO** irá aparecer ao lado da lista suspensa <sup>2</sup>

- **Página para Editar API KEY**

    * A **CAIXA DE TEXTO** central é onde deve ser inserida a chave da sua conta OpenAI
    * O botão **SALVAR CHAVE** irá testar a validade da sua API KEY e retornar se deu certo ou não <sup>1</sup>

- **Página EDITAR CONHECIMENTO**
    * Uma **LISTA SUSPENSA** estará na parte superior da aplicação para selecionar uma base prévia ou criar uma nova <sup>2</sup>
    * Ao selecionar uma base, um botão **EDITAR** irá aparecer abaixo para abrir o Excel para editar a base
    * **IMPORTANTE**: após editar uma base, **SALVE** o arquivo e **FECHE** o Excel para evitar conflitos

- **Página CONVERSA COM CHATGPT**
    * Uma **CAIXA DE TEXTO** estará presente abaixo para que você digite sua mensagem ao ChatGPT
    * Um **BOTÃO DE ENVIAR** mensagem estará presente no lado direito para enviar a mensagem ao ChatGPT (tecla *enter* não funciona)<sup>2</sup>

    &nbsp;

    1- A aplicação requer conexão com a internet para funcionar e, por utilizar uma API da OpenAI externa ao programa, alguns anti-vírus podem travar a aplicação ao clicar para rodar a API. Caso isso aconteça, basta desativar seu Firewall enquanto utilizar a aplicação.

    2- Ao mexer com arquivos dentro da pasta *Arquivos e Programas* para editar as bases de conhecimento, alguns anti-vírus podem bloquear a aplicação também ou até mesmo o Windows. Caso isso aconteça, rode a aplicação em modo *Administrador* e/ou desative a proteção em tempo real do seu anti-vírus.


&nbsp;


## Funcionalidades

- Chat em tempo real com o ChatGPT
- Uso de bases de conhecimento pré-feitas
- Edição de qualquer base de conhecimento

&nbsp;
## Stack utilizada

**Front-end:** Python, Tkinter

**Back-end:** Python, Excel

&nbsp;
## Licença

[MIT](https://github.com/zoddinGC/custom-chatgpt/blob/main/LICENSE)

&nbsp;
## Autores

- [@zoddinGC](https://github.com/zoddinGC/)

