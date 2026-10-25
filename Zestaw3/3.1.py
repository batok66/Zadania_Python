# 1.
# Kod jest składniowo poprawny, kompiluje się, jednak kompilator zgłasza ostrzeżenia o
# redundantnych nawiasach oraz średnikach.

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;

# poprawnie bez ostrzeżeń kompilatora
x = 2; y = 3
if x > y:
    result = x
else:
    result = y

# 2.
# Kod niepoprawny składniowo (An illegal target for a variable annotation).
# Po dwukropku w for może byc tylko jedna instrukcja, tu są dwie

# for i in "axby": if ord(i) < 100: print (i)

for i in "axby":
    if ord(i) < 100: print (i)

# 3.
# Kod poprawny składniowo zagnieżdzenie instrukcji jak poniżej jest możliwe po dwukropku.

for i in "axby": print (ord(i) if ord(i) < 100 else i)