
░███████╗  
██╔██╔══╝  
╚██████╗░  MeusPila    
░╚═██╔██╗  
███████╔╝  
╚══════╝░  

### EM CONSTRUÇÃO...

Arquivo principal: `leitor.py`  

Exemplo de uso:  
  `python leitor.py operacoes.txt`  

onde `operacoes.txt` é um arquivo no seguinte formato:

```
DD/MM/YYYY T Q A V
```
onde 
- DD/MM/YYYY é a data da operação (dia/mês/ano),
- T é o tipo da operação: C (compra) ou V (venda),
- Q é a quantidade comprada,
- A é o nome do ativo,
- V é o valor do ativo por unidade.

Exemplo:
```
17/03/2021 C 50 B3SA3 52,68
25/03/2021 C 10 BTLG11 114,00
25/03/2021 V 100 EQTL3 22,58
25/03/2021 C 100 EQTL3 22,58
25/03/2021 C 57 PNVL3 19,18
```

Mais informações na Wiki:
https://github.com/kl0ck/acoes_python/wiki
