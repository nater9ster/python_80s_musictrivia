import random

print("\n--- 80's Music Trivia Guessing Game --- \n\n"
      "Welcome back to the 1980's!\n\n"
      "The goal of this game is:\n"
      "1. Guess which music artist sang the lyric shown.\n"
      "2. Get to 1000 points to win the game!\n\n"
      "If you guess correctly you get 100 points!\n\nIf you are incorrect we will give you a lifeline, showing you a list of 3 artists to choose from!\n"
      "Correctly guess out of the 3 artists and you will receive 50 points!\n"
      "If you guess incorrectly you receive no points and the next lyric will be shown.\n\n"
      "Ready to begin?\n")

# user chooses whether to start the game or not
score = 0


class Question:
    def __init__(self, lyrics, correct_answer, options):
        self.lyrics = lyrics
        self.correct_answer = correct_answer
        self.options = options


questions = [Question("I want to know what love is, I want you to show me...", "Foreigner", ["Journey", "U2", "Foreigner"]),
             Question("You spin me right round, baby, right round, like a record baby, right round right round...",
                      "Dead or Alive", ["Dead or Alive", "Rick Astley", "INXS"]),
             Question("Never gonna give you up, never gonna let you down...", "Rick Astley", [
                      "The Outfield", "Rick Astley", "Simple Minds"]),
             Question("Where do we go, where do we go now, where do we go, where do we go now",
                      "Guns n Roses", ["Metallica", "Guns n Roses", "Duran Duran"]),
             Question("I'm hot, sticky sweet. From my head, to my feet yeah!", "Def Leppard", [
                      "Def Leppard", "Hall and Oates", "Judas Priest"]),
             Question("Wish I knew what you were looking for...Might have known what you would find..",
                      "The Church", ["Def Leppard", "The Church,", "Prince"]),
             Question("And I ran...I ran so far away...I just ran..I ran all night and day...I couldn't get away",
                      "Flock of Seagulls", ["Men at Work", "Simple Minds", "Flock of Seagulls"]),
             Question("I just wanna use your love, tonight...I don't wanna lose your love, tonight!",
                      "The Outfield", ["Tears for Fears", "The Outfield", "Metallica"]),
             Question("She got she wanted, cuz she's heart and soul, she's hot and cold, she's got it all",
                      "Huey Lewis", ["Huey Lewis", "Toad the Wet Sprocket", "Bryan Adams"]),
             Question("You might think I'm foolish, but baby its not true, you might think I'm crazy, all I want is you", "The Cars", [
                      "Depeche Mode", "The Rolling Stones", "The Cars"]),
             Question("Don't. Don't you want me. You I don't believe you when you say that you don't need me",
                      "The Human League", ["The Human League", "Simple Minds", "Depeche Mode"]),
             Question("In the name of love. What more in the name of love?", "U2", [
                      "INXS", "Prince", "U2"]),
             Question("It hurts so good. Come on baby make it hurt so good, sometimes love don't feel like it should..",
                      "John Mellencamp", ["John Mellencamp", "Bryan Adams", "Huey Lewis"]),
             Question("Shout. Shout. Let it all out. These are the things we can do without, come on. I'm talking to you.",
                      "Tears for Fears", ["Mr. Mister", "Flock of Seagulls", "Tears for Fears"]),
             Question("I wear my sunglasses at night, so I can, so I can, watch you weave then breathe your story lines",
                      "Corey Hart", ["Corey Hart", "Depeche Mode", "Duran Duran"]),
             Question("Smell like I sound, I'm lost in a crowd, And I'm hungry like the wolf",
                      "Duran Duran", ["Depeche Mode", "Huey Lewis", "Duran Duran"]),
             Question("We're flying high, we're watching the world pass us by..Never want to come down, never want to put my feet back down on the ground",
                      "Depeche Mode", ["Depeche Mode", "Metallica", "U2"]),
             Question("Darkness, imprisoning me. All that I see, absolute horror · I cannot live, I cannot die. Trapped in myself, body my holding cell",
                      "Metallica", ["Nine Inch Nails", "Metallica", "Flock of Seagulls"]),
             Question("This one goes out to the one I love, This one goes out to the one I've left behind. A simple prop to occupy my time, This one goes out to the one I love", "R.E.M.", [
                      "R.E.M", "U2", "The Church"]),
             Question("So slide over here and give me a moment, Your moves are so raw, I've got to let you know..I've got to let you know-You're one of my kind",
                      "INXS", ["Bryan Adams", "Motley Crue", "INXS"]),
             Question("Tonight, tonight! I'm on my way, just set me free, home sweet home",
                      "Motley Crue", ["Motley Crue", "Def Leppard", "Depeche Mode"]),
             Question("In a West End town, a dead end world. The East End boys and West End girls...West End girls",
                      "Pet Shop Boys", ["U2", "The Church", "Pet Shop Boys"]),
             Question("Here I go again on my own, Going down the only road I've ever known, Like a drifter, I was born to walk alone", "Whitesnake", ["Whitesnake", "Eurythmics", "Scorpions"])]

while True:
    answer = input("Choose 1 to start/continue or 2 to exit the game: \n")
    if answer == "1":
        print(f"\nRadical! Here we go!\n")
    else:
        print(f"\nCatch you later, dude!\n")
        exit()

    random.shuffle(questions)
    for Question in questions:
        lyrics = Question.lyrics
        correct_answer = Question.correct_answer
        options = Question.options
        print(lyrics)
        answer = input(f"\nWhat 80's artist sang these lyrics?\n")
        if answer.lower() == correct_answer.lower():
            print(f"\nThat is correct! You have scored 100 points!")
            score += 100
            print(f"\nYou have", score, "points!\n")
            if score >= 1000:
                print(f"\nCongratulations! You have won the game!")
                break
        else:
            print("\nThat is incorrect. Here are 3 artists to choose from, guess the right one and score 50 points!\n")
            print(Question.options)
            answer = input(f"\nWhich one of these 3 do you choose?")
            if answer.lower() == correct_answer.lower():
                print(f"\nThat's right! You have scored 50 points")
                score += 50
                print(f"\nYou have ", score, "points!\n")
            elif answer.lower() != correct_answer.lower():
                print(f"\nThat is incorrect. No points scored on this one.")
            if score >= 1000:
                print("Congratulations! You have won the game!\n")
                break


# initiate the 1st random question

# check the value of the answer to the correct answer

# if correct assign 100pts and move on to the next question

# if false give player 3 answers to choose from, including the correct answer

# if correct assign 50 pts and move on to next question

# if false, no pts assigned and move on to next question

# once player reaches 1000 pts = "You have won the game, you rule the 80's!"

# ask if player wants to play again or exit
