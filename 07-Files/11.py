file = open('films.txt','w')
film_titles = ['film1', 'film2', 'film3']

for i in range(0, len(film_titles)):
    file.write(f"{film_titles[i]}\n")

file.close()