file = open('films.txt','w')
film_titles = ['film1', 'film2', 'film3']

for element in film_titles:
    file.write(f"{element}\n")

file.close()