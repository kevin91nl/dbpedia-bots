# DBPedia Bots

This repository is a collection of DBPedia Bots in order to collection information. The entries in the output file are separated by newlines and the attributes are separated by tabs.

## Language Bot

Usage:

```
python language.py data/language.txt
```

Produces a file containing language information from DBPedia. The first attribute is the ISO-6391 code of the language, the second attribute is the ISO-6391 code in which the label is displayed and the last attribute is the label of the language. The output looks like this:

```
...
nl	en	Dutch language
nl	ar	لغة هولندية
nl	de	Niederländische Sprache
nl	es	Idioma neerlandés
nl	fr	Néerlandais
nl	it	Lingua olandese
nl	ja	オランダ語
nl	nl	Nederlands
nl	pl	Język niderlandzki
nl	pt	Língua neerlandesa
nl	ru	Нидерландский язык
nl	zh	荷蘭語
en	en	English language
en	ar	لغة إنجليزية
en	de	Englische Sprache
en	es	Idioma inglés
...
```
