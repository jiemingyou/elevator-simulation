import PySimpleGUI as sg
import keyboard
from Elevator import Elevator
from Person import Person

sg.theme('Material2')



CANVAS_SIZE = (400, 600)
FLOORS = 10
FLOOR_HEIGHT = 50
BG_COLOR = "white"

# Initiate the class instance
elevator = Elevator(max_capacity=6, min_floor=1, max_floor=10)


def floor_selector(floors: int):
    # Show
    for i in range(floors):
        graph.TKCanvas.itemconfig(elevator_markers[i], fill = "lightgray")
        graph.TKCanvas.itemconfig(floor_markers[i], fill = "black")
        graph.TKCanvas.itemconfig(text_markers[i], fill = "black")
    # Hide
    for i in range(floors, FLOORS):
        graph.TKCanvas.itemconfig(elevator_markers[i], fill = "white")
        graph.TKCanvas.itemconfig(floor_markers[i], fill = "white")
        graph.TKCanvas.itemconfig(text_markers[i], fill = "white")


def current_floor(idx):
    """
    Displays the elevator's current location
    """
    graph.TKCanvas.itemconfig(elevator_markers[idx-1], fill = "SeaGreen2")

# Define the window's contents
GUI = [
        [sg.Graph(canvas_size = CANVAS_SIZE,
                graph_bottom_left = (0,0),
                graph_top_right = CANVAS_SIZE,
                background_color = BG_COLOR,
                key='graph')]
]

floor_slider    = sg.Slider((2,10), orientation='h', key="-FLOORS-", enable_events = True)
start_button    = sg.Button('Start', s=(5, 1.1), button_color="green")
up_button       = sg.Button('Up', s=(5, 1.1), button_color="gray", disabled=True)
stay_button     = sg.Button('Stay', s=(5, 1.1), button_color="gray", disabled=True)
down_button     = sg.Button('Down', s=(5, 1.1), button_color="gray", disabled=True)
quit_button     = sg.Button('Quit', s=(5, 1.1), button_color="red")


SETTINGS = [
    [sg.Text("FLOORS:"), floor_slider],
    [sg.HSeparator(pad=50)],
    [up_button],
    [stay_button],
    [down_button],
    [sg.HSeparator(pad=50)],
    [start_button],
    [quit_button]
]

layout = [
    [sg.pin(sg.Column(GUI)),
    sg.VSeperator(),
    sg.pin(sg.Column(SETTINGS, element_justification="c"))]
]

# Create the window
window = sg.Window('Elevator-Simulation', layout, finalize = True)

# Drawing the objects
graph = window['graph']

# Constrcting the GUI
floor_markers = []
elevator_markers = []
text_markers = []

for i in range(1,FLOORS+1):
    # Floors
    floor_markers.append(graph.DrawLine((0, FLOOR_HEIGHT*i), (CANVAS_SIZE[0] ,FLOOR_HEIGHT*i)))

    # Elevator markers
    elevator_markers.append(graph.DrawRectangle((2,2+FLOOR_HEIGHT*i),(52,48+FLOOR_HEIGHT*i),
        fill_color='lightgray', line_color="white"))
    
    # Texts
    text_markers.append(graph.DrawText(f"Floor {i}", location=(CANVAS_SIZE[0]-30, i*FLOOR_HEIGHT + FLOOR_HEIGHT/2)))


# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    
    # Display correct amount of floors
    floors = int(values["-FLOORS-"])
    floor_selector(floors)
    elevator._max_floor = floors

    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Start the simulation
    if event == 'Start':
        floor_slider.update(disabled=True, visible=False)
        start_button.update(disabled=True, visible=False)
        up_button.update(disabled=False, button_color=sg.theme_button_color())
        stay_button.update(disabled=False, button_color=sg.theme_button_color())
        down_button.update(disabled=False, button_color=sg.theme_button_color())

    if event == 'Up':
        elevator.move_up(error=False)
    
    if event == 'Down':
        elevator.move_down(error=False)

    if event == 'Stay':
        pass

    # Display current floor
    current_floor(elevator.floor())

# Finish up by removing from the screen
window.close()