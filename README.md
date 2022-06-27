# ZADANIE – JUNIOR PYTHON DEVELOPER

## Opis potrzeby użytkownika końcowego

Sprzedawca posiada sklep e-commerce z różnymi produktami. Do tej pory handel był realizowany na
terenie Polski. Sprzedawca chciałby wysyłać towary do krajów Unii Europejskiej oraz do Stanów
Zjednoczonych. Pojawiała się zatem u niego potrzeba akceptacji płatności w dolarach amerykańskich
(USD) oraz w Euro. Kupujący musi wiedzieć ile towar kosztuje w danej walucie.

Sprzedawca potrzebuje rozwiązania, które cyklicznie raz dziennie lub na żądanie pobierze aktualny
kurs walut z Narodowego Banku Polskiego i dokona aktualizacji cen dla produktów w bazie danych.

## Wstępna konfiguracja środowiska

_cmd_

```cmd
pip install mysql-connector-python
```

1. Należy zainstalować bazę danych MySQL i utworzyć bazę o nazwie mydb.
2. Do bazy danych zaimportować [schemat]() sklepu ecommerce
3. Następnie należy zaimportować testowe [testowe dane]() do bazy danych  
   Uwaga: dane należy ładować w kolejności od góry do dołu, transakcja po transakcji z uwagi
   na to, że niektóre klienty np. MySQL Workbench ładują dane jednocześnie i może wtedy
   wystąpić błąd importu.

## Wymagania funkcjonalne

1. W tabeli Product należy dodać dwie nowe
   kolumny: UnitPriceUSD, UnitPriceEuro.

   _sql_

   ```sql
   ALTER TABLE `mydb`.`Product`
   ADD UnitPriceUSD DECIMAL;

   ALTER TABLE `mydb`.`Product`
   ADD UnitPriceEuro DECIMAL;
   ```

2. Utworzyć skrypt w języku Python, który połączy się po REST API do Narodowego Banku
   Polskiego i pobierze aktualny kurs waluty dla USD i Euro. API do NBP znajduje się
   tutaj: http://api.nbp.pl/en.html.

   _cmd_

   ```cmd
   pip install requests
   ```

   _python_

   ```py
   import requests

   res = requests.get('https://excample_url?format=json').json()
   print(len(res.text))
   ```

3. Następnie skrypt ten po pobraniu kursów powinien wykonać aktualizację cen wszystkich
   produktów w bazie danych (kolumna UnitPriceUSD, UnitPriceEuro).

   _cmd_

   ```cmd
   pip install mysql-connector-python
   ```

   _python_

   ```py
   import mysql.connector

   mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
   ```

4. Następnie skrypt powinien mieć oddzielny tryb działania, który na żądanie wygeneruje
   Excela z listą wszystkich produktów w bazie danych z następującymi kolumnami: **ProductID, DepartmentID, Category, IDSKU, ProductName, Quantity, UnitPrice, UnitPriceUSD, UnitPriceEuro, Ranking**

   _cmd_

   ```cmd
   pip install xlsxwriter
   ```

   _python_

   ```py
   workbook = xlsxwriter.Workbook(filename)
   worksheet = workbook.add_worksheet()
   for i in range(len(elems)):
      worksheet.write(row, col + i, elems[i])
   row += 1
   workbook.close()
   ```

## Wymagania poza funkcjonalne

1. Skrypt powinien być napisany obiektowo jeżeli to możliwe.
2. Kod w skrypcie powinien być udokumentowany według uznania.
3. Rozwiązanie należy wrzucić na konto GitHub.
4. Zmieniony schemat bazy danych należy wyeksportować w formie sql i także wrzucić na
   GitHub.
5. Skrypt powinien wykorzystywać moduł logging do tego aby logować operację z działania do
   pliku logu.
6. Skrypt powinien także obsłużyć wyjątek np. gdy API NBP nie będzie dostępne lub jak baza
   danych nie będzie dostępna lub jak wystąpi inny błąd. Wtedy błędy powinny być logowane
   do pliku logu.
7. Opcjonalnie skrypt może być stworzony w standardzie paczki python, którą można będzie
   zainstalować za pomocą komendy: pip install <module_name>.whl.
