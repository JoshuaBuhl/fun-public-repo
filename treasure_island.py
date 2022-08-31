print("Welcome to Treasure Island!\nWill you find the treasure or perish along the way?")
print("You stand at a crossroads one path leads left into a verdant vale "
      "the other one, to your right, climbs up a mountain.")

if (input("\nDo you go (left) into the valley or do you take the (right) path for a vantage point?\n").lower() == "left"):

    print("You wander into the deep forest in the vale. After a while you come across a slowly winding stream.\n")

    if (input("Do you try to (swim) through the water or (wait) among the looming trees for another opportunity?\n").lower() == "wait"):

        print("The giant branches spend some nice shade."
              "You choose to take a little nap leaning against one of the trees.\n"
              "You suddenly awake when you feel yourself gliding down a wooden slide.\n"
              "After a terrifying roller coaster ride in the dark."
              "the slide spits you out into a room with 3 coloured doors.\n")

        choice = (input("Do you enter the (red) one, the (blue) one or the (yellow) door?\n")).lower()
        if (choice == "yellow"):
            print("You push the massive yellow door open and step into the pitch black room.\n"
                  "The next moment the door snaps shut behind you and a bright flash of light blinds you.\n"
                  "A solid minute passes before you regain your eyesight and you gasp as a shining heap of gold comes into view.\n\n"
                  "Congratulations! You found the Treasure of the Island!\n")

        elif (choice == "blue"):
            print("The moment you touch the handle you realise your mistake, unfortunately a little too late.\n"
                  "Your hand is wrapped in slimy vines and with a jolt your body is lifted from your feet and thrown into a unknowable abyss.\n")

        elif (choice == "red"):
            print("As soon as you open the door tears fill your eye, 'You finally found it!!!' --- you think.\n"
                  "A huge golden pile lays at the other end of the room you storm into the room.\n"
                  "When suddenly the pile begins to move and the beautiful golden dragon lazily opens one of it's eyes.\n"
                  "The following burst of ghostly white flame leaves not even a flake of ash of your regrettably flammable body.\n")

        else:
            print("Apparently you didn't go unnoticed in this room, as suddenly a terrible voice cries 'die intruder!'\n"
                  "and the ground forms into another slide dropping you in a pit of spears.\n")

    else:
        print("The water is nice and warm. After about a minute of swimming you reach the other side of the stream.\n"
              "Then suddenly, when climbing out of the water, you get pulled under never to see the surface again.\n"
              "The peaceful river was hiding some sinister creature after all.\n")

else:
    print("After a few minutes the seemingly soild ground gives way under your feet.\n"
          "You fall into a deep hole and tragically don't survive the fall - the island claimed another victim.\n")
