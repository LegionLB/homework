# C:\\Users\\TenshiRin\\Desktop\\pyTest.txt

class Check:

    def __init__(self, path):
        self.path = path

    def check_text(self):
        words = 0
        lines = 0
        characters = 0
        space_button = 0
        f = open(self.path, 'r')
        for i in f:
            wordlist = i.split(' ')
            lines = lines + 1
            characters = characters + len(i)
            words = words + len(wordlist)
        print("The count of words = ", words), print("The count of lines = ", lines), print("The count of characters = "
                                                                                                 , characters)

a = Check('C:\\Users\\TenshiRin\\Desktop\\pyTest.txt')
a.check_text()
