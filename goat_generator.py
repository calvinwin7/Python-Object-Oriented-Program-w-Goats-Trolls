import random

FIRST_NAMES = ['Calvin', 'Thomas', 'Jeff', 'Jeffrey', 'Tom', 'Tamson', 'Henry', 
                 'Mark', 'John', 'Andre', 'Bruno', 'Benjamin', 'Aaron', 'Sophia', 'Kate', 'Pavani', 
                    'Levi', 'Gojo', 'Andreina', 'Iris', 'Pepe', 'Huda', 'Amaya', 'Chelley', 'Ace', 
                        'Karen', 'Larry', 'Catherine', 'Carolyn', 'Phil', 'Roman', 'Kendall', 'Kylie', 
                        'Stephen', 'LeBron', 'Katara', 'Aang', 'Toph', 'Zuko', 'Yue', 'Rapunzel', 'Flynn']

LAST_NAMES = ['Nguyen', 'Hanks', 'Sumner', 'Matthews', 'Brady', 'Pham', 'Ford', 
                    'Cuban', 'Havilcheck', 'Fernandes', 'Sesko', 'Wan-Bissaka', 'The First', 'Bishop'
                        'Pointi', 'The Goat', 'Satoru', 'Santos', 'Kendall', 'Garcia', 'Mustafa', 'Papaya', 
                            'Martin', 'Smith', 'Jasmine', 'Bird', 'Hahn', 'Do', 'Jackson', 'Slack', 
                                'Jenner', 'Curry', 'James', 'Water', 'Air', 'Beifong', 'Destiny', 'Princess'
                                'Blonde', 'Rider']

SUFFIXES = ['Esq.', 'Jr.', 'Sr.', 'III', 'IV', 'I', 'II']

def makeGoatName():
    name = FIRST_NAMES[random.randrange(len(FIRST_NAMES))]
    last_name = LAST_NAMES[random.randrange(len(LAST_NAMES))]

    if random.random < 0.25:
        middle_initial = chr(random.randint(0, 0.25) + 65)
        name += " " + middle_initial + "."

    name += last_name

    if random.random() < 0.10:
        name += SUFFIXES[random.randint(len(SUFFIXES))]

    return name


def main():
    for i in range(50):
        name = makeGoatName() + "\t"
        if (len(name)) < 14:
            name += "\t"
        name += makeGoatName()
        print(name)

    
    
if __name__ == "__main__":
    main()


    
