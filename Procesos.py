class CargaArc():
    def __init__(self,pelicula,actor,year,genero):
        self.pelicula = pelicula.strip()
        self.actor = [NameActor.strip() for NameActor in actor]
        self.year = year.strip()
        self.genero = genero.strip()
    def __str__(self):
        return self.pelicula +' '+ str(self.actor) +' '+ self.year +' '+ self.genero

class ProcPeliculas():
    def __init__(self):
        self.MoviesList = []
    def Pelicutorio(self, movie):
        for i in self.MoviesList:
            if i.pelicula == movie.pelicula:
                return
        self.MoviesList.append(movie)
    def Factorio (self, actores):
        ActList = []
        for i in self.MoviesList:
            if actores in i.actor:
                ActList.append(i)
        return ActList
    def Anotorio (self, onions):
        YearList = []
        for i in self.MoviesList:
            if onions == i.year:
                YearList.append(i)
        return YearList
    def Genotorio (self, generos):
        GeneroList = []
        for i in self.MoviesList:
            if generos == i.genero:
                GeneroList.append(i)
        return GeneroList