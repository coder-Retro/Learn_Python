celsiusTemps = [1,2,3,4,5]
fehrenheitTemps = list(map(lambda x:(x*(9/5))+32,celsiusTemps))
print(f"Temps in Fehrenheit: {fehrenheitTemps}")