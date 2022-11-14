# Automaçao de backup de arquivo(Só funciona no meu pc)
```
pip install pyautogui
```

## importar a biblioteca para a automação
```
import pyautogui
```

## importar a biblioteca time para controlar o tempo de execução do código
```
import time
```

## exibir uma mensagem de alerta

```
pyautogui.alert('O código vai começar. Não user nada do seu computador enquanto o código está rodando')
```

## setando o valor de espera para cada linha de comando
```
pyautogui.PAUSE = 0.5
```

## abrir o google drive no PC

```
pyautogui.press('winleft')
```
pyautogui.press: pressiona uma tecla

```
pyautogui.write('chrome')
```
pyautogui.write: escreve um texto

```
pyautogui.press('enter')
```

```
time.sleep(1)
```
time.sleep: vai esperar conforme o valor passado em segundos

```
pyautogui.write('https://drive.google.com/drive/u/1/my-drive')
```

```
pyautogui.press('enter')
```

## entrar na area de trabalhado(aonde está o arquivo)
```
pyautogui.hotkey('winleft', 'd')
```
pyautogui.hotkey: para fazer atalhos no computador

## cliquei no arquivo e arrastei ele
```
pyautogui.position()
```
pyautogui.position: pega a posisão do eixo X e Y do mouse

```
pyautogui.mouseTo(136, 421)
```
pyautogui.mouseTo: qual a posicao que ele vai passar

```
pyautogui.mouseDown()
```
pyautogui.mouseDown: clica aonde está o mouse com a posição que foi passada(botao esquerda do mouse)

```
pyautogui.mouseTo(1026, 536)
```
pyautogui.mouseTo: carregando o arquivo até essa posicao

## enquanto eu estou arrastando ele eu vou mudar para o google drive
```
pyautogui.hotkey('alt', 'tab')
```
abrindo o google drive(com esse atalha do windows)

## larguei o arquivo no google drive
```
pyautogui.mouseUp()
```
pyautogui.mouseUp: larguando o mouse

## esperar 5 segundos
time.sleep(5)

## alerta de finalização
```
pyautogui.alert('O código está finalizado.')
```