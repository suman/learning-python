from turtle import Turtle, Screen
screen = Screen()
# screen.setup(width=800, height=600)
image = 'blank_states_img.gif'
screen.addshape(image)

us_map = Turtle()
us_map.shape(image)

import pandas as pd
data = pd.read_csv('50_states.csv')

all_states = data.to_dict('records')
# print(all_states)

all_states_len = len(all_states)
score = 0
all_guess = []

# print(data[data['x'] == True])

while len(all_guess) != all_states_len:
    answer_state = screen.textinput(f'{score}/{all_states_len} is correct', 'What is the other state\'s name ?')
    answer_state = answer_state.title()
    if answer_state == 'Exit':
        break
    else:
        for state in all_states:
            if state['state'] == answer_state:
                state_text = Turtle()
                state_text.penup()

                state_text.goto(state['x'], state['y'])
                state_text.write(state['state'])
                score += 1
                all_guess.append(state)
                state_text.hideturtle()
                all_states.remove(state)



 # {state : ohio, x : 0, y: 2}

if len (all_states) > 0:
    new_frame = pd.DataFrame(all_states)
    new_frame.to_csv('50_states_unanswered.csv', index=False)
