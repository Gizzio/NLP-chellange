
Dialogi z lektur
=====================================

## Format danych

Pierwsza kolumna zbioru `in.tsv` zawiera początek dialogu pewnej lektury. Dialogi mogą być być prowadzone przez dowolną ilość osób
i nie zawierają innych adnotacji niż sama wypowiedź (np. komentarzy narratora). Poszczególne wypowiedzi w początku dialogu oddzielone są separatorem `[SEP]`.
Każda kolejna kolumna to propozycja kontynuacji dialogu. Kontynuacja dialogu może pochodzić z tej samej lub innej lektury.
Istnieje tylko jedna taka poprawna kontynuacja dialogu- ta, która faktycznie występuje w książce.
Zadaniem jest zwrócić poprawną kontynuację dialogu.

Jako format wyjściowy zwróć wszystkie proponowane kontynuacje dialogu uszeregowane  w kolejności od najbardziej prawdopodobnej do najmniej prawdopodbnej.
Propozycje powinny być identyczne jak w pliku `in.tsv` i oddzielone tabulacjami.

## Metryka

Metryka ewaluacji to [Mean Reciprocal Rank](https://en.wikipedia.org/wiki/Mean_reciprocal_rank) (MRR) lub Mean Average Precision (MAP). W przypadku niniejszego zadania, gdzie tylko jedna odpowiedź jest prawidłowa,
metryki MRR i MAP są tożsame.

## Zasady wyzwania

Dozwolone jest używanie gotowych, dostępnych modeli językowych (np. https://github.com/sdadas/polish-roberta ), ale nie wolno odwoływać się do żadnych danych poza tymi, zawartymi w zadaniu.
W szczególności nie wolno korzystać z żadnych książek, np. dotrenowywać modelu językowego na lekturach innych, niż te zawarte w zadaniu.

##  Przykład

Przykładowy wiersz `in.tsv` z trzema propozycjami kontynuacji dialogu:


```
Cześć, jestem Adam![SEP]Cześć, mam na imię Ala[SEP]Jak się masz?	Milordzie, fortuna nam sprzyja!	Dobrze. A Ty?	Co się stało?
```

Odpowiadający wiersz z `expected.tsv`:


```
Dobrze. A Ty?
```


Przykładowy plik `out.tsv`:


```
Dobrze. A Ty?	Co się stało?	Milordzie, fortuna nam sprzyja!
```

Directory structure
-------------------

* `README.md` — this file
* `config.txt` — configuration file
* `train/` — directory with training data
* `train/train.tsv` — sample train set
* `dev-0/` — directory with dev (test) data
* `dev-0/in.tsv` — input data for the dev set
* `dev-0/expected.tsv` — expected (reference) data for the dev set
* `test-A` — directory with test data
* `test-A/in.tsv` — input data for the test set
* `test-A/expected.tsv` — expected (reference) data for the test set
