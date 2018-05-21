Instrukcja obsługi:

1) w terminalu przejdź do folderu głównego aplikacji, następnie użyj komendy pip3 install -r requirements.txt
	Aplikacja wymaga interpretera języka Python w wersji co najmniej 3. Jest to spowodowane możliwością
	prawidłowego wyświetlania znaków w formacie UTF.
2) uruchom aplikację komendą python3 weather_app.py z katalogu głównego programu
3) Aplikacja pozwala wprowadzać dane w takiej postaci:
	Dane mają postać dodatnią dla szerokości północnej i długości wschodniej.
	Dane mają postać ujemną dla szerokości południowej i długości zachodniej.
	np San Francisco : 37.77 -122.43

	Należy wprowadzić dane będące współrzędnymi dwóch wierzchołków prostokąta
	wyznaczającego obszar z którego będą zbierane dane. Na stronie głównej aplikacji
	można zobaczyć rysunek wyjaśniający tę koncepcję.
	Program oblicza średnią temperarturę w danym obszarze oraz wypisuje nazwy stacji
	i temperatury jakie zostały z nich odczytane.

Możliwe jest niepoprawne działanie aplikacji. Zdarza jej sie otwierać dwie karty przeglądarki na raz.

