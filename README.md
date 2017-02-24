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