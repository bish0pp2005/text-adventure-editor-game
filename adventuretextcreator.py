import json
def getDefaultGame():
    defaultGame = {
        "start": [ 
            "Do you want to win or lose?",
            "I want to win",
            "win",
            "I'd rather lose",
            "lose",
            ],
        "win": [ 
            "You win!",
            "Start over",
            "start",
            "Quit",
            "quit",
            ],
        "lose": [
            "You lose!",
            "Start over",
            "start",
            "Quit",
            "quit"
        ]
    }
    return defaultGame
def printMenu():
    print("0) Exit")
    print("1) Load default game")
    print("2) Load a game file")
    print("3) Save the current game")
    print("4) Edit or add a node")
    print("5) Play the current game!")
def saveGame(): 
    with open("gameNode.json", "w") as file:
        json.dump(gameNode, file, indent=3)
def loadGame():
    try: 
        with open("gameNode.json", "r") as file:
            gameNode = json.load(file)
            return gameNode
    except FileNotFoundError:
            print("This save file does not exist")
            return None
def editField(field_name, current_value):
    print(f"{field_name} ({current_value}): ")
    new_value = input()
    return new_value if new_value else current_value
def editNode(gameNode):
    # I ended up googling this specific node. I was pretty confused
    print("create or edit a node")
    current_node = list(gameNode.keys())
    print("Current nodes:", ", ".join(current_node))
    node_name = input("Choose a node to edit, or create a new node")
    if node_name in current_node:
        new_node = {node_name: gameNode[node_name]}
    else:
        new_node = {node_name: ["", "", "", "", ""]}  # Initialize with empty data

    new_node[node_name][0] = editField("Description", new_node[node_name][0])
    new_node[node_name][1] = editField("Menu A", new_node[node_name][1])
    new_node[node_name][2] = editField("Node A", new_node[node_name][2])
    new_node[node_name][3] = editField("Menu B", new_node[node_name][3])
    new_node[node_name][4] = editField("Node B", new_node[node_name][4])

    return {**gameNode, **new_node}
def playNode(gameNode, node):
    print("\n".join(gameNode[node]))

    while True:
        try:
            user_choice = int(input("\nYour choice: "))
            next_node = gameNode[node][2 * user_choice + 1]
            return next_node
        except (ValueError, IndexError):
            print("This choice was invalid. Try again maybe?")
def playGame(gameNode):
    current_node = "start"

    while current_node != "quit":
        current_node = playNode(gameNode, current_node)
def getMenuChoice():
    try:
        choice1 = int(input("What is your choice [1-5]"))
        return choice1 
    except ValueError:
        print("Invalid input. Please input a number 0-5")
def main():
        gameNode =  getDefaultGame()
        keepGoing = True 
        while keepGoing == True:
            printMenu()
            response = getMenuChoice()
            if response == 1:
                keepGoing = False
            elif response == 2:
                gameNode =  loadGame()
            elif response == 3: 
                saveGame(gameNode)
            elif response == 4:
                gameNode = editNode(gameNode)
            elif response == 5:
                playGame(gameNode)
            else: 
                print("Please input a number 0-5")