# Definējiet klasi Song

class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made: {self.title} - {self.author}")

    def sing(self, max_lines=-1):
        print(f"{self.title} - {self.author}")
        for line in self.lyrics[:max_lines]:
            print(line)
        return self

    def yell(self, max_lines=-1):
        print(f"{self.title} - {self.author}")
        yell_part = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in self.lyrics[:max_lines]:
            print(line.upper())
        return self
      
ziemelmeita = Song(
    "Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"]
)

ziemelmeita.sing(1).yell(2)
