# AI Formula 1 Racing
### Team
 * Popa Filip-Andrei
 * Militaru Ionut-Marius
 * Baranga Roxana 


## Project description

This project is an AI-based Formula 1 racing simulation using NEAT
(NeuroEvolution of Augmenting Topologies) and Pygame. The AI controls 
multiple cars to navigate a racing track, and a user-controlled car can 
also participate in the simulation.

## Features

* AI-controlled cars using NEAT for evolving neural networks.
* User-controlled car with keyboard inputs.
* Collision detection and respawn functionality.
* Real-time simulation with adjustable speed and display options.
* Multiple maps for varied simulation environments.
* Kepping the best generation for each map to ensure the 
AI model is better trained.


## Link Github and Youtube Demo
* https://github.com/pofian/AI-Formula1-Racing
* https://youtu.be/y-U3_HziniQ

## Implementation
#### Languages/Technologies Used

- Python
- Pygame
- NEAT-Python

#### Usage instructions
* for user car use the following keyboard inputs to control the user car:
    - `W` - Speed up
    - `A` - Turn left
    - `D` - Turn right
    - `S` - speed down
* Additional keyboard inputs for the game/simulation to work:
    - `O` - Toggle speedup on/off
    - `P` - Toggle display on/off
    - `ESC` - Exit the simulation

#### Functionality of Generated Cars
- The AI-controlled cars are generated using NEAT, which evolves neural 
networks to control the cars.
- Each car receives inputs from its environment and makes 
decisions based on its neural network.
- The cars aim to navigate the track as efficiently as possible, 
avoiding collisions and maximizing their performance.

#### Collision Handling
- Both AI-controlled and user-controlled cars have 
collision detection.
- When a car collides with a white zone (representing an obstacle or boundary),
it will stop drawing and, if it's the user car, it will respawn 
at the starting position.

#### Saving Car Rankings
- At the end of each simulation, the performance of each 
car is evaluated.
- The cars are ranked based on their performance, 
and the rankings are saved.
- To save the ranking of each car at the finish line, the simulation records the
fitness score of each car, which reflects its performance during the race.
- The ranking of each car is displayed after each simulation.

## Team Contributions

### Filip
- Implemented the NEAT algorithm for evolving neural networks.
- Developed the `training_main.py` script to run the simulation 
and handle user inputs.
- Developed the `Game` class to handle the game environment, including 
updating the display and handling events.
- Implemented collision detection and functions to 
update the positions of each car.

### Roxana
- Developed model simulation logic in the `AICar` class to define the behavior for AI-driven cars in training and in the game against the user
- Built a performance evaluation system to assess and select the best performing AI model
- Integrated the best performing AI genome and the user controlled car into the main game, enabling competition

### Marius
- Implemented user car controls using keyboard inputs.
- Added functionality for the user car to respawn at the starting 
position if it touches the track boundaries.
- Created multiple maps for varied simulation environments.
- Implemented the functionality to save and load the NEAT population,
each map has at least 80 generation that have run.
- Created the README and demonstration video.

## Difficulties
- It was quite challenging to make the cars function properly on 
the track, both the ones generated by NEAT and the user-controlled car.
- Saving the best generation correctly was a bit challenging, and if we saved it incorrectly, we had to retrain the cars.
- Resolving merge conflicts on GitHub was also a challenging task.

## Project Structure

- `training_main.py`: Main script to run the NEAT simulation and handle user inputs.
- `ai_car.py` class which defines the behavior of AI-controlled and user-controlled cars, class that extends the class car
- `car.py`: Contains a class that defines the attributes and behavior of a car.
- `game.py`: Contains the `Game` class which handles the game environment,
including updating the display and handling events.
- `maps`: Directory containing map images and car sprites.
- `saved`: Directory to save and load the NEAT population.
- `main` : Contains the code for our game, user car vs best Ai car generated.
- `config.txt`: Configuration file for NEAT parameters.

