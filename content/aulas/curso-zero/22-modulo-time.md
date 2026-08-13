# 22. Módulo time

> **Resumo didático**
> O módulo `time` serve para pegar data/hora do sistema, medir a duração de trechos de código, fazer pausas entre comandos e formatar saídas de tempo. A aula mostra `time.time()`, `time.perf_counter()`, `time.sleep()`, configuração de fuso horário e formatação com `strftime`.

## Objetivo da aula

Aprender as principais funções do módulo `time`: medir tempo de execução com precisão, criar pausas, configurar fuso horário e exibir/formatar data e hora.

## Conceitos em ordem (narrativa didática)

1. **Importação**: `import time` — já vem com o interpretador, sem instalação.
2. **`time.time()`**: retorna o número de segundos (float) transcorridos desde o marco de **1º de janeiro de 1970** (epoch). Pode ser negativo para datas anteriores.
3. **Medir duração**: capture `inicio = time.time()` antes do trecho, `final = time.time()` depois, e subtraia (`final - inicio`). Resultado em segundos.
4. **Variação de tempo**: o mesmo código pode demorar tempos diferentes (hardware, máquina virtual do Colab). Boa prática: rodar várias vezes e tirar média.
5. **`time.perf_counter()`**: igual a `time.time()` para medir duração, porém **mais preciso** e imune a alterações no relógio do sistema. Recomendado para medir tempo de execução.
6. **`time.sleep(segundos)`**: pausa a execução pelo tempo indicado (ex.: `time.sleep(6)` espera 6 s entre comandos — útil em menus).
7. **Fuso horário**: o Colab usa UTC por padrão. Para definir o fuso (ex.: América/São_Paulo):

   ```python
   import os, time
   os.environ['TZ'] = 'America/Sao_Paulo'
   time.tzset()

   ```
   Na máquina local, o fuso do Brasil já é considerado.
8. **`time.localtime()`** (com fuso) vs. **`time.gmtime()`** (UTC). Ambas retornam um objeto `struct_time`.
9. **`time.strftime(formato, t)`**: formata data/hora como string. Códigos comuns: `%d` (dia 01-31), `%m` (mês 01-12), `%Y` (ano 4 dígitos), `%H:%M:%S` (hora:minuto:segundo).

## Pontos-chave

- `time.time()` = segundos desde 1970 (epoch).
- Para medir duração de código, use `time.perf_counter()` (mais preciso, não afetado pelo relógio).
- `time.sleep(n)` pausa por n segundos.
- Configure `TZ` + `time.tzset()` para fuso correto no Colab.
- `localtime()` usa fuso; `gmtime()` usa UTC.
- `strftime('%d/%m/%Y %H:%M:%S', t)` formata a saída.

## Exemplo essencial (código Python)

```python
import time

# Medir duração de um trecho
inicio = time.perf_counter()
acumulado = 0
for i in range(10):
    acumulado += 1
final = time.perf_counter()
print(f"tempo total de execucao: {final - inicio} segundos")

# Pausa entre comandos
print("inicio")
time.sleep(6)
print("fim")

# Configurar fuso horário (Colab usa UTC por padrão)
import os
os.environ['TZ'] = 'America/Sao_Paulo'
time.tzset()

# Data e hora atuais
t = time.localtime()
print(time.strftime('%d/%m/%Y %H:%M:%S', t))   # ex.: 13/08/2026 09:30:00
print(time.strftime('%H:%M:%S', t))            # só a hora

```

## Armadilhas comuns

- Usar `time.time()` para medir duração quando o relógio pode ser alterado — prefira `perf_counter()`.
- Esquecer de configurar o fuso horário no Colab e obter horário em UTC (errado para o Brasil).
- Confundir `time.time()` (segundos desde 1970) com data formatada.
- Usar `sleep` sem necessidade, deixando o programa lento.
- Achar que o tempo de execução é constante — ele varia; repita a medição.

## Conexão com a próxima aula

A próxima aula sai do Python puro e apresenta a biblioteca **scikit-learn** — o primeiro contato com aprendizado de máquina, onde medição de tempo e organização de código (módulos) já serão úteis.
