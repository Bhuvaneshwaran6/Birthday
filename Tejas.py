import time
from random import randint

for i in range(1, 85):
    print('')

space = ''
wishes = [
    "Wishing you a year filled with success and happiness! 🎉",
    "May all your dreams come true on this special day! 🌟",
    "Here's to another year of amazing adventures and achievements! 🎂",
    "May your life be as bright and joyful as this day! 🌈",
    "Wishing you health, wealth, and happiness in abundance!",
    "May your birthday be the start of a year filled with good luck and joy!",
    "Sending you lots of love and warm wishes on your special day!",
    "May your heart be as light as a feather and your days filled with laughter!",
    "Wishing you a birthday that's as sweet as your favorite cake!",
    "May your life be a fantastic journey filled with love and success!",
    "May your day be as bright as your smile and as lovely as your personality!",
    "Happy Birthday! May you keep smiling and shining always!",
    "Cheers to another year of wisdom, happiness, and amazing memories!",
    "May your birthday be the beginning of a year filled with great achievements!",
    "Wishing you endless joy, laughter, and success in the year ahead!",
    "May your special day be filled with love, laughter, and good times!",
    "Here's to a day as bright as your future and as sweet as your dreams!",
    "Wishing you a year of opportunities, happiness, and great moments!",
    "May you continue to inspire and spread happiness wherever you go!",
    "May your birthday be the stepping stone to all your dreams coming true!",
    "Wishing you a year of exciting adventures and beautiful surprises!",
    "May your heart be filled with love and your life with success!",
    "Happy Birthday! May your day be as fantastic as you are!",
    "Cheers to another year of awesome you! Happy Birthday!",
    "May your day be filled with joy, love, and unforgettable moments!",
    "Wishing you the happiest of birthdays and a year of amazing experiences!",
    "May your day be as bright as your smile and as warm as your heart!",
    "Here's to a year of dreams realized and goals achieved! Happy Birthday!",
    "Wishing you a day as wonderful as your presence in our lives!",
    "May your birthday be the start of a year filled with love and blessings!",
    "May your special day be the beginning of an incredible journey!",
    "Happy Birthday! May your year be filled with laughter and success!",
    "Wishing you a day of endless happiness and a life full of adventures!",
    "May your birthday bring you everything you've ever wished for!",
    "Here's to another year of growth, success, and happiness! Happy Birthday!",
    "May your life be a masterpiece, and each day a new stroke of brilliance!",
    "Wishing you a year of exciting possibilities and beautiful memories!",
    "May your birthday be the key to unlocking your dreams and desires!",
    "Happy Birthday! May your day be as colorful and joyful as you are!",
    "Cheers to another year of laughter, love, and fantastic moments!",
    "May your heart be filled with joy, and your path be paved with success!",
    "Wishing you a day of surprises, and a year of exciting discoveries!",
    "May your birthday be the beginning of a wonderful adventure!",
    "May your day be filled with love, laughter, and all the things you enjoy!",
    "Here's to a year of happiness, health, and endless smiles! Happy Birthday!",
    "Wishing you a lifetime of dreams achieved and goals fulfilled!",
    "May your day be as bright as your smile and as warm as your heart!",
    "Happy Birthday! May your year be filled with love and excitement!",
    "May your birthday be a beautiful chapter in the story of your life!",
    "May your special day be the start of a new phase filled with joy and success!",
    "Wishing you a year of amazing experiences and great memories!",
    "May your life be a masterpiece, and each day a new work of art!",
    "Happy Birthday! May your journey be filled with happiness and laughter!",
    "Cheers to another year of growth, success, and wonderful moments!",
    "May your heart be filled with love, and your life with achievements!",
    "Wishing you a day of happiness and a year of exciting opportunities!",
    "May your birthday be the key to unlocking your passions and dreams!",
    "Here's to a year of colorful experiences and beautiful memories! Happy Birthday!",
    "May your day be as bright as your spirit and as sweet as your dreams!",
    "Wishing you a year of love, laughter, and all the things that make you happy!",
    "May your birthday be the start of a wonderful journey filled with blessings!",
    "May your special day be the first step towards achieving your goals!",
    "Happy Birthday! May your year be filled with success and joy!",
    "May your life be a canvas, and each day a new stroke of brilliance!",
    "Wishing you a year of incredible adventures and memorable moments!",
    "May your birthday be the catalyst for all your dreams and aspirations!",
    "May your day be filled with love, laughter, and the things that bring you joy!",
    "Here's to a year of prosperity, growth, and endless smiles! Happy Birthday!",
    "Wishing you a lifetime of accomplishments and dreams coming true!",
    "May your day be as radiant as your smile and as warm as your heart!",
    "Happy Birthday! May your journey be a collection of beautiful moments!",
    "Cheers to another year of laughter, love, and fantastic experiences!",
    "May your heart be brimming with joy, and your path filled with achievements!",
    "Wishing you a day of unexpected delights and a year of thrilling discoveries!",
    "May your birthday be the launchpad for your passions and desires!",
    "May your day be as vibrant as your personality and as full of surprises!",
    "Here's to a year of opportunities, happiness, and extraordinary adventures! Happy Birthday!",
    "May your life be a work of art, and each day a new masterpiece!",
]

for i in range(1, 1000):
    count = randint(1, 100)
    while count > 0:
        space += ' '
        count -= 1
    if i % 10 == 0:
        print(space + '🎂Happy Birthday!')
        print(space + 'Tejas')  # Print the name "Tejas"
        print(space + wishes[randint(0, len(wishes) - 1)])  # Add a random birthday wish
    elif i % 9 == 0:
        print(space + "🎂")
    elif i % 5 == 0:
        print(space + "💛")
    elif i % 8 == 0:
        print(space + "🎉")
    elif i % 7 == 0:
        print(space + "🍫")
    elif i % 6 == 0:
        print(space + "Happy Birthday!💖")
    else:
        print(space + "🔸")
    space = ''
    time
