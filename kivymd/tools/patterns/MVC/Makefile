# FILE TO FIND AND CREATE LOCALIZATION FILES FOR YOUR APPLICATION. \
\
In this file, you can specify in which files of your project to search for \
localization strings. \
These files should be listed in the below command: \
\
\
xgettext -Lpython --output=messages.pot --from-code=utf-8 \
    path/to/file-1 \
    path/to/file-2 \
    ...

.PHONY: po mo

po:
	xgettext -Lpython --output=messages.pot --from-code=utf-8 \
             View/%s/%s.kv \
             View/%s/%s.py
	msgmerge --update --no-fuzzy-matching --backup=off data/locales/po/en.po messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off data/locales/po/ru.po messages.pot

mo:
	mkdir -p data/locales/en/LC_MESSAGES
	mkdir -p data/locales/ru/LC_MESSAGES
	msgfmt -c -o data/locales/en/LC_MESSAGES/%s.mo data/locales/po/en.po
	msgfmt -c -o data/locales/ru/LC_MESSAGES/%s.mo data/locales/po/ru.po