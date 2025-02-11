## Simple Youtube Downloader

## Passo a passo inicial para todos os sistemas

Em qualquer um dos dois sisemas operacionais que este projeto foi desenvolvido será necessário primeiramente instalar
as dependẽncias do projeto. Essas dependências podem ser encontradas no arquivo na raiz do projeto "requirements.txt".

> **Detalhe:**
> Se você estiver usando Linux precisará usar **pip3** ao invés de **pip** em todos os comandos listados no Readme, o mesmo vale para o outro
> comandos com python, no linux usará **python3** e no windows apenas **python**.

Aperte `CTRL + J` para abrir o terminal no VsCode. Ou acesse o terminal do editor de código que está usando. Com o terminal aberto você pode usar os comandos a seguir:

```bash
pip install -r requirements.txt
```

## Uso manual

Após instalar as dependências você vai abrir o arquivo `main.py` e lá irá retirar o comentário da função do seu sistema operacional,
Caso use Linux então retire a hashtag da frente do nome que possui `linux_download_video()`, caso esteja rodando um sistema windows
o comando que terá sua hashtag removida será o `windows_download_video()`.

Após isso, você estará pronto para para usar o sistema seguindo as próximas instruções:

```bash
python main.py
```

Depois disso é só seguir as instruções que o sistema vai te dar e o vídeo será baixado.

## Uso automatico

O sistema pode baixar uma lista de vídeos se você fornecer os links para ele. Para usar essa pegada mais automática você deve ir até o arquivo `config/youtube_link`. Lá você deve colcar os links dos vídeos no Youtube que gostaria de baixar (**SEPARADOS POR NOVAS LINHAS!**)

Depois de ter esse arquivo pronto você pode voltar para o arquivo `main.py` dentro dos parênteses da função do seu sistema operacional escrever um `True`. Isso vai ativar o modo de download dos links presentes na lista.

Caso queria cancelar o código por alguma razão, saiba que isso é possível apertando `CTRL + C` no terminal.
> OBS: Certifique-se de que **clicou** no terminal antes de apertar `CTRL + C`!


