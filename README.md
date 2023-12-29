# Snake-Game
My First Python Project

# Problem Statement
Challenge Description: Elevating the Classic Snake Game

In the domain of timeless Snake Games, where players guide a snake to consume fruits and extend its length, a new dimension is being explored. This project aims to elevate the conventional Snake Game in Python by introducing an intriguing element— the inclusion of "unfavorable fruits" that present a unique challenge to the player.

Objective:
The primary goal of this endeavor is to enrich the Snake Game experience by incorporating adverse elements in the form of unfavorable fruits. Diverging from regular fruits, these fruits are to be avoided as their consumption will promptly result in the conclusion of the game. The challenge lies in navigating the snake through the expanding maze while strategically evading these disadvantageous elements.

Key Features:

1.	Unfavorable Fruits: Develop a distinctive class of fruits that, upon consumption, trigger the conclusion of the game.

2.	Dynamic Complexity: Investigate methods to dynamically vary the appearance rate of unfavorable fruits as the game unfolds, presenting a progressively demanding challenge.


3.	Visual Indicators: Enhance user interaction by integrating visual signals, such as distinct colors or animations, to differentiate unfavorable fruits from regular ones.

4.	Score Tracker: Integrate a scoring system that accounts for both regular and unfavorable fruits, allowing players to monitor their performance in the face of adversity.

# Methodology / Procedure/ Algorithm

1.	Define Game Rules and Mechanics:

•	Outline the basic rules of the Snake Game, including snake movement, fruit consumption, and game termination conditions.
•	Specify the mechanics for introducing and handling bad fruits, defining their impact on the game.

2.	Set Up Python Environment:

•	Ensure you have Python installed on your system.
•	Choose a suitable development environment or IDE for Python, such as VSCode, PyCharm, or Jupyter Notebook.

3.	Create Game Framework:

•	Set up the basic game framework using a Python script or module.
•	Implement the initial Snake Game without the addition of bad fruits to establish a baseline.

4.	Introduce Bad Fruits Class:

•	Define a new class for bad fruits, extending the existing fruit class or creating a separate class.
•	Include attributes such as position, appearance rate, and visual cues to distinguish bad fruits.

5.	Implement Dynamic Difficulty:

•	Introduce a mechanism to dynamically adjust the appearance rate of bad fruits as the game progresses.
•	Consider factors like snake length, elapsed time, or score to influence the difficulty level.

6.	Enhance Visual Feedback:

•	Implement visual cues to differentiate bad fruits from regular fruits.
•	Utilize distinct colors, animations, or other visual elements to enhance user experience.

7.	Update Game Logic:

•	Modify the game logic to handle the introduction, positioning, and consequences of bad fruits.
•	Implement conditions for detecting the collision of the snake with bad fruits, triggering game termination.

8.	Integrate Scoring System:

•	Enhance the scoring system to account for both regular and bad fruits.
•	Assign appropriate scores for each type of fruit and update the total score accordingly.

9.	Test and Debug:

•	Conduct thorough testing to ensure the proper functioning of the enhanced Snake Game.
•	Debug any issues related to the introduction of bad fruits, dynamic difficulty, or scoring.

# Modules of the proposed work

Turtle Graphics Setup:

turtle.Screen(): Creates the game window.
turtle.Turtle(): Creates turtles for the snake, fruit, bad fruit, and scoring.

Game Elements:

Snake: Controlled by the player's input (w, s, a, d keys).
Fruit: Eaten by the snake to increase the score.
Bad Fruit: Decreases the snake's length and score if eaten.
Old Fruit: Keeps track of the snake's previous positions.


Functions:

snake_go_up, snake_go_down, snake_go_left, snake_go_right: 
Change the snake's direction based on user input.
snake_move: Move the snake based on its current direction.

Collision Detection:

Check for collisions with the game borders, fruit, and bad fruit.
Update the score and handle game over scenarios.

Main Game Loop:
	
Continuously updates the game state, checks for input, and handles events.

Score Display:
	
Uses a turtle (scoring) to display the score.

Graphics and Styling:

Sets up the game window size, colors, and styling.

Closing the Game:

Uses screen.bye() to close the game window.

# Results/Screenshots

<img width="524" alt="image" src="https://github.com/Ghostkwebb/Snake-Game/assets/61558762/32a1df2c-3367-4376-aa73-8ab75f3f8600">

<img width="524" alt="image" src="https://github.com/Ghostkwebb/Snake-Game/assets/61558762/02c45c29-7796-41bb-9025-322bc4bd4d8a">

<img width="524" alt="image" src="https://github.com/Ghostkwebb/Snake-Game/assets/61558762/b4e71a45-e165-4d2b-8654-6c19d751fbc5">

# Conclusion

In summary, the evolution of the traditional Snake game has been an intriguing exploration into the domain of Python programming. By applying contemporary programming methodologies and libraries, we've successfully enhanced the classic Snake game, offering a more captivating and visually appealing user experience.

Throughout this project, we've not only refined our Python skills but also gained valuable insights into game development principles. The modular and object-oriented approach incorporated into the code enhances its readability, maintainability, and extensibility. Additionally, the integration of external libraries like Turtle has provided a robust foundation for crafting dynamic and interactive gaming experiences.

As technology advances, so do the opportunities to enhance classic games. Our journey in enhancing the Snake game illustrates the boundless potential for creativity and innovation within the programming realm. Whether for educational purposes or pure entertainment, the revitalized Snake game underscores the versatility and adaptability of Python in the field of game development.

# References

https://www.geeksforgeeks.org/ <br>
https://www.w3schools.com/  <br>
https://stackoverflow.com/ <br>
https://www.youtube.com/ <br>
https://www.programiz.com/ <br>
https://www.freecodecamp.org/ <br>
https://www.simplilearn.com/ <br>
https://www.educative.io/ <br>
https://www.scaler.com/ <br>
https://www.javatpoint.com/ <br>

