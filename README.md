# Trening
Zadania treningowe

Zadanie 1

a. Napisz funkcję square(num), która zwróci wartość num podniesione do kwadratu.

b. Napisz funkcję multiply(subject, times), która zwróci wartość zmiennej subject pomnożoną przez wartość argumentu times.
   
c. Napisz funkcję power, która przyjmuje dwa argumenty:
   -base: obowiązkowy,
   -exponent: opcjonalny o standardowej wartości równej 2.
   Funkcja ma zwrócić wartość base podniesione do potęgi exponent.
   
d. Napisz funkcję convert_to_usd, która przyjmuje parametr zlotys, czyli kwotę w złotówkach. Funkcja ma zwrócić podaną kwotę w    dolarach amerykańskich. Jako przelicznik przyjmij wartość 3,85 PLN = 1 USD.

e. Napisz funkcję calculate_net, która przyjmie argumenty:
   -gross, czyli kwotę brutto ceny zakupu,
   -vat, czyli wartość podatku VAT. Możesz założyć, że VAT ma być liczbą zmiennoprzecinkową z zakresu 0 – 1.
   Funkcja ma zwrócić wartość netto ceny.

Zadanie 2.

Gdy klub piłkarski A gra dwumecz z klubem piłkarskim B, oznacza to, że grają jeden mecz na boisku drużyny A i jeden na
boisku drużyny B. Wygrywa ta drużyna, która zdobędzie więcej goli w obu meczach. W przypadku, gdy drużyny zdobyły tyle
samo bramek, gole zdobyte na wyjeździe liczą się jako "trochę ważniejsze" i wygrywa ta drużyna, która zdobyła więcej
bramek na wyjeździe. Remis w dwumeczu wypada wtedy, gdy obie drużyny mają tyle samo bramek na wyjeździe.

Na przykład:
W Pucharze Polski grają dwa zespoły: Grom i Błyskawica. Zespoły rozegrały następujące mecze:
Gospodarz: Grom.
Grom 0:2 Błyskawica

Gospodarz: Błyskawica.
Błyskawica 1:3 Grom

Sumaryczny wynik dwumeczu wynosi 3:3. Jednak Grom na wyjeździe zdobył 3 bramki, a Błyskawica tylko 2. Zatem wygrywa Grom.

Napisz funkcję, football_win, która przyjmie następujące parametry:
Gole zdobyte przez zespół A w pierwszym meczu (na boisku zepołu A),
Gole zdobyte przez zespół B w pierwszym meczu (na boisku zepołu A),
Gole zdobyte przez zespół A w drugim meczu (na boisku zespołu B),
Gole zdobyte przez zespół B w drugim meczu (na boisku zespołu B),
po czym zwróci 1, jeśli dwumecz wygrał zespół A, 2 – jeśli B. W przypadku remisu, zwróć X. Wynik ma być łańcuchem
tekstowym, nie liczbą!

Zadanie 3.
a. Napisz funkcję multiplication_table(n), gdzie n to liczba, dla której generujemy tabliczkę mnożenia.

Program ma wyświetlić tabliczkę mnożenia dla danej liczby, jak w przykładzie:

multiplication_table(3)
wynik:

1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
10 * 3 = 30

b. Napisz funkcję even_odd(n), która na podstawie wartości parametru liczbowego wypisuje wszystkie liczby od zera do n.
Przy każdej liczbie program ma napisać, czy liczba jest parzysta czy nie. Np.:

0 – parzysta
1 – nieparzysta
2 – parzysta
3 – nieparzysta

c. Napisz funkcję tree(n), gdzie n to dowolna liczba naturalna. Funkcja ma rysować drzewko z gwiazdek jak w przykładzie:

# dla wartości n=5:
tree(5)
wynik:

*
**
***
****
*****

d. Napsz funkcję factorial(n), która przyjmie jako parametr liczbę naturalną n. Funkcja ma zwrócić wartość n!, czyli
wynik mnożenia wszystkich liczb naturalnych w zakresie 1..n

Zadanie 4.
Napisz funkcję message, która jako parametr przyjmie słownik o następujących kluczach:

name,
role,
movie.
Następnie niech funkcja przygotuje sformatowany napis: "In movie, name is a role.", gdzie w odpowednie miejsca podstawi
wartości z ww. kluczy. Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość None.

Przykład:

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
Wynik:

In Star Wars, Han Solo is a smuggler.
input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
Wynik:

None

Zad. 5
a. Napisz funkcję mean(numbers), gdzie numbers to lista liczb dowolnego typu. Funkcja powinna zwrócić średnią
arytmetyczną wszystkich elementów listy numbers.

b. Napisz funkcję d6(num), która zasymuluje rzuty kostką sześcienną. num to parametr, który oznacza liczbę rzutów
kostką. Funkcja ma zwrócić sumę wyrzuconych oczek.

Zad. 6
a. Napisz funkcję safe_get, która przyjmue dwa parametry:
l: dowolna lista,
index: liczba.

Funkcja powinna zwracać element listy o indeksie index. Jeśli nie ma takiego elementu, powinna zwracać None.

uwaga: zrób to używając obsługi wyjątków.

b. Napisz funkcję divide, która przyjmie dwa argumenty: a i b. Muszą być to liczby naturalne. Funkcja ma działać
następująco:
- ma sprawdzić, czy a i b to liczby,
- ma obsłużyć problem dzielenia przez zero.
Oba powyższe przypadki muszą być obsłużone przez wychwytywanie wyjątków.

Jeśli któryś z powyższych warunków nie zostanie spełniony, funkcja ma zwrócić None.

c. Napisz funkcję phone, która przyjmie parametr number, który oznacza numer telefonu. Funkcja ma sprawdzić, czy podany
numer znajduje się na liście numerów (wymyśl jakieś). Jeśli nie - musi zwrócić wyjątek typu Exception z komentarzem
'Nie ma takiego numeru!'.

Zadanie 7.
A.
Stwórz klasę Calculator. Konstruktor ma nie przyjmować żadnych danych. Każdy nowo stworzony obiekt powinien mieć pustą
listę, w której będzie trzymać historię wywołanych operacji (stwórz ją w konstruktorze). Następnie dodaj do klasy
następujące metody:

- add(num1, num2) – metoda ma dodać do siebie dwie zmienne i zwrócić wynik. Dodatkowo na liście operacji ma zapamiętać
napis: "added num1 to num2 got result".
- multiply(num1, num2) – metoda ma pomnożyć przez siebie dwie zmienne i zwrócić wynik. Dodatkowo na liście operacji ma
zapamiętać napis: "multiplied num1 with num2 got result".
-subtract(num1, num2) – metoda ma odjąć od siebie dwie zmienne i zwrócić wynik. Dodatkowo na liście operacji ma
zapamiętać napis: "subtracted num1 from num2 got result".
-divide(num1, num2) – metoda ma podzielić przez siebie dwie zmienne i zwrócić wynik. Dodatkowo na liście operacji ma
zapamiętać napis: "divided num1 by num2 got result". Pamiętaj, że nie można dzielić przez zero.
-printOperations() – metoda ma wypisać wszystkie zapamiętane operacje.
-clearOperations() – metoda ma wyczyścić wszystkie zapamiętane operacje.

Pamiętaj o używaniu self w odpowiednich miejscach. Stwórz kilka kalkulatorów i przetestuj ich działanie.

B. Stwórz klasę AdvancedCalculator, która dziedziczy po klasie Calculator. Klasa powinna implementować następujące
metody:

- pow(num1, num2) – metoda ma zwracać num1 do potęgi num2. Dodatkowo w tablicy operacji ma zapamiętać napis:
"num1^num2 equals result".
- root(num1, num2) – metoda ma wyliczyć pierwiastek num2 stopnia z num1. Dodatkowo w tablicy operacji ma zapamiętać
napis: "root num2 of num1 equals result".

Zadanie 8.
Stwórz klasę Employee, która ma spełniać następujące wymogi:

Mieć atrybuty:
id - atrubyt ten powinien trzymać numer identyfikacyjny pracownika,
first_name - atrybut określający imię pracownika,
last_name - atrybut określający nazwisko pracownika,
salary - atrybut określający ile pracownik zarabia za godzinę.

- Posiadać konstruktor przyjmujący id, imię, nazwisko i płace za godzinę.
- Posiadać metodę 'raise_salary(percent)' której rolą będzie zwiększenie wartości atrybutu salary o podany procent.

Pamiętaj o sprawdzeniu czy podana wartość jest:
-Wartością numeryczną,
-Wieksza (lub równa) od 0.0

Zadanie 9.
A.
Napisz obiektowo program, który będzie obsługiwał skanowanie produktów w sklepie.

Stwórz klasę 'Product'. Klasa ta ma posiadać podane atrybuty:

id - liczba całkowita. Powinna być unikalna w całym systemie (jak to osiągnąć będzie wyłumaczone w dalszej części zadania).
name - string. Jest to nazwa danego produktu.
description - string. Jest to opis danego produktu.
price - float. Jest to cena za jeden produkt. Powinna być większa od 0.01.
quantity - liczba całkowita większa od zera.

Klasa powinna mieć też nastepujące metody:

konstruktor - powinien przyjmować opis, cenę i ilość produtku.
atrybut id powiniem mieć możliwość wyłącznie odczytu. Rozważ użycie dekoratora.
metodę get_total_sum() która będzie zwracała łączną kwotę za dany produkt (wyliczaną jako ilość * cena produktu.

Generowanie unikalnego id dla produktu:

W dalszej części programu będziemy chcieli identyfikować nasze produkty po ich id. Dlatego musimy zagwarantować że każdy z stworzonych produktów będzie miał unikalny numer identyfikacyjny. W tym celu powinniśmy zdefiniować zmienną next_id, którą należy umieścić poza klasą.

Zmienna ta będzie trzymała id ktore zostanie nadane następnemu stworzonemu produktowi. Nastepnie w kostruktorze klasy musimy wykonać następujące czynności:

własnie tworzonemu produktowi przypisać id trzymane w zmiennej next_id,
zwiększyć wartość next_id o jeden.

# w konstruktorze
self.id = next_id
next_id += 1
Dzieki temu żaden z naszych produktów nie będzie miał takiego samego id.

B.
Napisz klasę ShoppingCart. Klasa ta ma posiadać podane atrybuty:

products - tablica z obiektami klasy Product.
Klasa powinna mieć też nastepujące metody:

add_product(new_product) - metoda ta powinna dodawać nowy produkt do tablicy z produktami. Kluczem produktu powinno być jego id (dzięki temu będziemy mogli łatwo znaleźć produkt w naszym koszyku).
remove_product(product_id) - metoda ta powinna usuwać produkt z koszyka. Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić.
change_product_quantity(product_id, new_quantity) - metoda ta powinna zmianiać ilość danego produktu w koszyku. Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić.
print_receipt() - metoda drukująca paragon. Na paragonie powinno się znaleźć: lista wszystkich produktów, wraz z ich id, nazwą, ceną, ilością i łączą ceną (pamiętaj że masz do tego dedykowamą metodę w klasie Product) i łączna kwota za wszystkie produkty znajdujące się w koszyku.
Zmodyfikuj klasę produktu tak, żeby umożliwiała nadawanie rabatu. Jeżeli ilość danego produktu jest większa lub równa 3 to metoda get_total_sum() powinna nadawać 20% zniżki na łączną kwotę za te produkty.