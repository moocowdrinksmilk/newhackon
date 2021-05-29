from sqlalchemy import insert

engine = create_engine('sqlite:///hackon.db')

activities = [
    {
        "id": 1,
        "title": "JUGGLING",
        "content": "Juggling is a challenging but rewarding hobby; studies show that people who learn to juggle increase their brains' grey matter! While juggling may seem and be difficult to master at first, it becomes easier once you've learned the basics and practiced it.\n https://www.wikihow.com/Juggle",
        "category": "solo",
        "prompt": "How well have you been juggling your responsibilities? What are some struggles that you have?"
    },
    {
        "id": 2,
        "title": "MEDITATE",
        "content": "Meditation is a simple practice available to all, which can reduce stress, increase calmness and clarity and promote happiness. Learning how to meditate is straightforward, and the benefits can come quickly. https://www.mindful.org/how-to-meditate/"
        "category": "solo",
        "prompt": "How did you feel after the activity? What causes you undue stress?"
    },
    {
        "id": 3,
        "title": "HAIKU",
        "content": "Haiku is a form of Japanese poetry made of short, unrhymed lines that evoke natural imagery. Haiku can come in a variety of different formats of short verses, though the most common is a three-line poem with a 5-7-5 syllable pattern.\n Writing haiku might seem simple: or that all it takes to make one is to hit a certain syllable count. To gain a richer understanding of this ancient art form, and even try your hand at writing a few, read more about its deep history and origins below.\n https://www.masterclass.com/articles/how-to-write-a-haiku-in-4-easy-steps",
        "category": "solo",
        "prompt": "What do we often forget to appreciate in life? What made you smile and laugh recently?"
    },
    {
        "id": 4,
        "title": "LEARN ANOTHER LANGUAGE",
        "content": "“Language is the road map of a culture.  It tells you where its people come from and where they are going” ‒ Rita Mae Brown\n Taking the time to learn a new language can help you appreciate another culture and greatly improve the quality of connections you can make with others. Learn some simple words and phrases of that language you always wanted to learn below!\n https://www.duolingo.com/",
        "category": "solo",
        "prompt": "How do we respond to differences around us? How can we be more inclusive and accepting of others?"
    },
    {
        "id": 5,
        "title": "WRITE A LETTER TO A YOUR FUTURE SELF",
        "content": "Is there anything you want to always remember? Why would you write a letter to your future self? Does it seem silly and childish? Actually, this exercise can bring much value to your life. Whether you’re hoping to achieve specific goals, follow up on bucket list items, or give words of affirmation, your future self will be grateful to receive a letter no matter what. \nhttps://www.futureme.org/",
        "category": "solo",
        "prompt": "What choices have you made in the last five years that you’d thank yourself for making?"
    },
    {
        "id": 6,
        "title": "DESERT ISLAND",
        "content": "Your cruise to the Bahamas sank and you were stranded on a deserted island. On your way out of the ship, you are able to grab 3 of the following items. The items available are: \n 1) A bag of fruit and vegetable seeds \n2) A pocket knife \n3) A 100 ft rope \n4) A bedsheet \n5) A bucket \n6) 2 liters of kerosene \n7 A pen and paper  \n\n Which 3 items did you choose and why? How would they help you survive and escape the island?",
        "category": "solo",
        "prompt": "What’s something enjoyable you get to experience every day that you’ve come to take for granted?"
    },
    {
        "id": 7,
        "title": "HAIKU",
        "content": "Haiku is a form of Japanese poetry made of short, unrhymed lines that evoke natural imagery. Haiku can come in a variety of different formats of short verses, though the most common is a three-line poem with a 5-7-5 syllable pattern. Writing haiku might seem simple: or that all it takes to make one is to hit a certain syllable count. To gain a richer understanding of this ancient art form, and even try your hand at writing a few, read more about its deep history and origins below. \nhttps://www.masterclass.com/articles/how-to-write-a-haiku-in-4-easy-steps",
        "category": "solo",
        "prompt": "Share your haiku and what inspiration you drew! What have you seen in nature recently that made you feel happy, peaceful, or free?"
    },
    {
        "id": 8,
        "title": "GUESS THE WORK DESK",
        "content": "Everyone is to send a picture of your desk/workstation at home to a designated person. The designated person is to reveal each picture one-by-one and everyone is to guess who the picture belongs to. Don't tidy up your desk last minute! Have fun guessing who's desk is the messiest! \nhttps://www.sessionlab.com/methods/guess-the-desk",
        "category": "solo",
        "prompt": "Share what is the favourite thing on your desk and why it brings you joy!"
    },
    {
        "id": 9,
        "title": "WHAT ARE YOU EATING",
        "content": "Have you ever wondered what the food you eat everyday can tell you about where you come from? Have you ever wondered why people from different parts of the world eat different types of food? Do you ever ask yourself why certain foods or culinary traditions are so important to your culture? There is more of a connection between food and culture than you may think. \nShare a picture of the food you are eating and about its culture/origin! \nhttps://freelymagazine.com/2017/01/07/what-food-tells-us-about-culture/",
        "category": "solo",
        "prompt": "Share something interesting and unique about your culture and background"
    },
    {
        "id": 10,
        "title": "DINNER SANTA",
        "content": "Everyone has participated in a Secret-Santa gift exchange at least once in their life (or at least heard about it). This activity adds a twist to the traditional game. Instead of sending a gift, everyone orders food delivery to the address of the person that they have been randomly assigned. Then, an hour or so later, or when everyone's food has arrived, the virtual dinner party and catch-up time begins. This is a great way to lighten up everyone's mood during quarantine and feel a bit more connected emotionally while being physically isolated. \nhttps://holidappy.com/party-planning/Secret-Santa-During-Quarantine",
        "category": "solo",
        "prompt": "Send a dish recommendation or a recipe that the someone else should try!"
    },
]

