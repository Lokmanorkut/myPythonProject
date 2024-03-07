mylist=[1,2,3]
#
#print(len(mylist))

class Movie():
    def __init__(self,title,director,duration) -> None:
        self.title=title
        self.director=director
        self.duration=duration
        
    def __str__(self) -> str:
        return f"{self.title} by {self.director}"
        
    
    def __len__(self):
        return self.duration
    def __del__(self):
        print("movie has been deleted")
m=Movie("film adı","yönetmen",120)

        
print(str(mylist))

print(len(m))

del m

print(m)