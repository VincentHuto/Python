print("Movie Creation")


class movie:
    def __init__(self, titleIn, ratingIn, ratingNumbersIn):
        self.title = titleIn
        self.rating = ratingIn
        self.ratingNumbers = ratingNumbersIn

    def getTitle(self):
        return self.title

    def setTitle(self, titleIn):
        self.title = titleIn

    def getRating(self):
        return self.rating

    def setTitle(self, ratingIn):
        self.rating = ratingIn

    def getRatingNumbers(self):
        return self.ratingNumbers

    def setRatingNumbers(self, ratingNumbersIn):
        self.ratingNumbers = ratingNumbersIn

    def addRating(self, pos):
        if 5 > pos >= 1:
            self.ratingNumbers[pos] += 1
        else:
            print("Rating Position Out of Bounds")

    def getAverage(self):
        totalNumOfRatings = sum(self.getRatingNumbers())
        oneStar = self.getRatingNumbers()[0] * 1
        twoStar = self.getRatingNumbers()[1]*2
        threeStar = self.getRatingNumbers()[2]*3
        fourStar = self.getRatingNumbers()[3]*4
        fiveStar = self.getRatingNumbers()[4]*5
        totalStars = oneStar+twoStar+threeStar+fourStar+fiveStar
        return totalStars / totalNumOfRatings


movie1 = movie("Color Out of Space", "M", [4, 13, 3, 16, 720])
movie2 = movie("Call of Cthulhu", "PG-13", [1, 3, 5, 6, 49])
movie3 = movie("The Shadow over Innsmouth", "G", [3, 4, 45, 226, 429])
movies = [movie1,movie2,movie3]
for i in range(len(movies)):
    print("Movie Title", movies[i].getTitle())
    print("Rating", movies[i].getRating())
    print("List of Ratings", movies[i].getRatingNumbers())
    print("Average of Ratings", movies[i].getAverage())
    print()

