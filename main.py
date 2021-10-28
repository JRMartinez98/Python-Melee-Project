import PySimpleGUI as sg
import random as rd
import time
import threading

#Both charList and FrameData are organized by order of appearance in the character select screen of Melee.
charList = [('Melee Project/Icons/Dr Mario.png', '-DR.MARIO-'),         
                ('Melee Project/Icons/Mario.png', '-MARIO-'),        
                ('Melee Project/Icons/Luigi.png', '-LUIGI-'),        
                ('Melee Project/Icons/Bowser.png', '-BOWSER-'),
                ('Melee Project/Icons/Peach.png', '-PEACH-'),               
                ('Melee Project/Icons/Yoshi.png', '-YOSHI-'),        
                ('Melee Project/Icons/DK.png','-DK-'),               
                ('Melee Project/Icons/Captain Falcon.png', '-FALCON-'),
                ('Melee Project/Icons/Ganondorf.png', '-GANON-'),           
                ('Melee Project/Icons/Falco.png', '-FALCO-'),        
                ('Melee Project/Icons/Fox.png', '-FOX-'),            
                ('Melee Project/Icons/Ness.png', '-NESS-'), 
                ('Melee Project/Icons/Ice Climbers.png', '-ICE CLIMBERS-'), 
                ('Melee Project/Icons/Kirby.png', '-KIRBY-'),        
                ('Melee Project/Icons/Samus.png', '-SAMUS-'),        
                ('Melee Project/Icons/Zelda.png', '-ZELDA-'), 
                ('Melee Project/Icons/Link.png', '-LINK-'),                 
                ('Melee Project/Icons/YoungLink.png', '-YLINK-'),    
                ('Melee Project/Icons/Pichu.png','-PICHU-'),         
                ('Melee Project/Icons/Pikachu.png', '-PIKACHU-'), 
                ('Melee Project/Icons/Jigglypuff.png', '-PUFF-'),           
                ('Melee Project/Icons/Mewtwo.png', '-MEWTWO-'),      
                ('Melee Project/Icons/Mr Game & Watch.png', '-G&W-'),
                ('Melee Project/Icons/Marth.png', '-MARTH-'), 
                ('Melee Project/Icons/Roy.png', '-ROY-'),                   
                ('Melee Project/Icons/Sheik.png', '-SHEIK-')]

FrameData = {'-DR.MARIO-': 'Melee Project/Frame Data/Dr. Mario',
                '-MARIO-' : 'Melee Project/Frame Data/Mario',
                '-LUIGI-' : 'Melee Project/Frame Data/Luigi',
                '-BOWSER-' : 'Melee Project/Frame Data/Bowser',
                '-PEACH-' : 'Melee Project/Frame Data/Peach',
                '-YOSHI-' : 'Melee Project/Frame Data/Yoshi',
                '-DK-' : 'Melee Project/Frame Data/Donkey Kong',
                '-FALCON-' : 'Melee Project/Frame Data/Captain Falcon',
                '-GANON-' : 'Melee Project/Frame Data/Ganondorf',
                '-FALCO-' : 'Melee Project/Frame Data/Falco',
                '-FOX-' : 'Melee Project/Frame Data/Fox',
                '-NESS-' : 'Melee Project/Frame Data/Ness',
                '-ICE CLIMBERS-' : 'Melee Project/Frame Data/Ice Climbers',
                '-KIRBY-' : 'Melee Project/Frame Data/Kirby',
                '-SAMUS-' : 'Melee Project/Frame Data/Samus',
                '-ZELDA-' : 'Melee Project/Frame Data/Zelda',
                '-LINK-' : 'Melee Project/Frame Data/Link',
                '-YLINK-' : 'Melee Project/Frame Data/Young Link',
                '-PICHU-' : 'Melee Project/Frame Data/Pichu',
                '-PIKACHU-' : 'Melee Project/Frame Data/Pikachu',
                '-PUFF-' : 'Melee Project/Frame Data/Jigglypuff',
                '-MEWTWO-' : 'Melee Project/Frame Data/Mewtwo',
                '-G&W-' : 'Melee Project/Frame Data/Mr. Game & Watch',
                '-MARTH-' : 'Melee Project/Frame Data/Marth',
                '-ROY-' : 'Melee Project/Frame Data/Roy',
                '-SHEIK-' : 'Melee Project/Frame Data/Sheik'
}
ExcelCol = {'-DR.MARIO-': 'Melee Project/Frame Data/Dr. Mario',
                '-MARIO-' : 'Melee Project/Frame Data/Mario',
                '-LUIGI-' : 'Melee Project/Frame Data/Luigi',
                '-BOWSER-' : 'Melee Project/Frame Data/Bowser',
                '-PEACH-' : 'Melee Project/Frame Data/Peach',
                '-YOSHI-' : 'Melee Project/Frame Data/Yoshi',
                '-DK-' : 'Melee Project/Frame Data/Donkey Kong',
                '-FALCON-' : 'Melee Project/Frame Data/Captain Falcon',
                '-GANON-' : 'Melee Project/Frame Data/Ganondorf',
                '-FALCO-' : 'Melee Project/Frame Data/Falco',
                '-FOX-' : 'Melee Project/Frame Data/Fox',
                '-NESS-' : 'Melee Project/Frame Data/Ness',
                '-ICE CLIMBERS-' : 'Melee Project/Frame Data/Ice Climbers',
                '-KIRBY-' : 'Melee Project/Frame Data/Kirby',
                '-SAMUS-' : 'Melee Project/Frame Data/Samus',
                '-ZELDA-' : 'Melee Project/Frame Data/Zelda',
                '-LINK-' : 'Melee Project/Frame Data/Link',
                '-YLINK-' : 'Melee Project/Frame Data/Young Link',
                '-PICHU-' : 'Melee Project/Frame Data/Pichu',
                '-PIKACHU-' : 'Melee Project/Frame Data/Pikachu',
                '-PUFF-' : 'Melee Project/Frame Data/Jigglypuff',
                '-MEWTWO-' : 'Melee Project/Frame Data/Mewtwo',
                '-G&W-' : 'Melee Project/Frame Data/Mr. Game & Watch',
                '-MARTH-' : 'Melee Project/Frame Data/Marth',
                '-ROY-' : 'Melee Project/Frame Data/Roy',
                '-SHEIK-' : 'Melee Project/Frame Data/Sheik'
}


#Method for generating a layout for the character select screen. This method is to avoid redundancy and due to the fact that PySimpleGUI requires that layouts are remade every time you make a new window.
def charSelectLayout(ElemType):
    layout = []
    if ElemType == 'Button':
        topRow = []

        # Nested loop that makes Buttons for the first two rows of characters.
        for i in range(0,2):
            rowList = [] 
            
            for j in range (0, 9): 
                rowList.append(sg.Button(image_filename=charList[j + (i*9)][0], key = charList[j + (i*9)][1]))
            
            topRow.append(rowList)

        bottomRow = []

        # Makes the third row of characters.
        bottomRow.append(sg.Text('            ')) 
        for i in range (18, 26):
            bottomRow.append(sg.Button(image_filename=charList[i][0], key = charList[i][1]))

        layout = topRow + [bottomRow]

    
    return layout
    
#Creates window for displaying the players Slippi stats. Currently not working for stats, only displays a character selector.
def statsWindow(event):
    statsLayout = charSelectLayout('Button')

    window = sg.Window('Stats for Player', statsLayout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
           break
    
    window.close()

def frameDataWindow():
    charLayout = charSelectLayout('Button')

    window = sg.Window('Stats for Player', charLayout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
           break
        elif event in FrameData:
            print(event, FrameData[event])
            PATH = FrameData[event]+'/jab1.gif'
            PATH2 = FrameData[event]+'/jab2.gif'
            PATH3 = FrameData[event]+'/jab3.gif'
            PATH4 = FrameData[event]+'/utilt.gif'
            PATH5 = FrameData[event]+'/ftilt.gif'
            PATH6 = FrameData[event]+'/dtilt.gif'
            PATH7 = FrameData[event]+'/dattack.gif'
            PATH8 = FrameData[event]+'/fsmash.gif'
            PATH9 = FrameData[event]+'/usmash.gif'
            PATH10 = FrameData[event]+'/dsmash.gif'
            PATH11 = FrameData[event]+'/nair.gif'
            PATH12 = FrameData[event]+'/uair.gif'
            PATH13 = FrameData[event]+'/fair.gif'
            PATH14 = FrameData[event]+'/bair.gif'
            PATH15 = FrameData[event]+'/dair.gif'
            PATH16 = FrameData[event]+'/neutralb.gif'
            PATH17 = FrameData[event]+'/sideb.gif'
            PATH18 = FrameData[event]+'/upb.gif'
            PATH19 = FrameData[event]+'/downb.gif'

            #Layout for column Element. Separation into multiple lines is for better visualization and understanding of how it's organized.
            column = [ [sg.Text('Ground Attacks', font=('Calibri', 36), justification='center')] , 
            [sg.Image(filename=PATH, key = '-gif-'), sg.Image(filename=PATH2, key = '-gif1-'),sg.Image(filename=PATH3, key = '-gif2-')], 
            [sg.Image(filename=PATH4, key = '-gif3-'), sg.Image(filename=PATH5, key='-gif4-'), sg.Image(filename=PATH6, key = '-gif5-'), sg.Image(filename=PATH7, key = '-gif6-')],
            [sg.Image(filename=PATH8, key = '-gif7-'), sg.Image(filename=PATH9, key = '-gif8-'), sg.Image(filename=PATH10, key = '-gif9-')],
            [sg.Text('Aerial Attacks', font=('Calibri', 36), justification = 'center')], 
            [sg.Image(filename=PATH11, key = '-gif10-'), sg.Image(filename=PATH12, key = '-gif11-'), sg.Image(filename=PATH13, key = '-gif12-'), sg.Image(filename=PATH14, key = '-gif13-'),sg.Image(filename=PATH15, key = '-gif14-')],
            [sg.Text('Special Attacks', font=('Calibri', 36), justification = 'center')],
            [sg.Image(filename=PATH16, key = '-gif15-'), sg.Image(filename=PATH17, key = '-gif16-'),sg.Image(filename=PATH18, key = '-gif17-'),sg.Image(filename=PATH19, key = '-gif18-')]
            ]

            #Layout for the GIFs.
            layout = [ [sg.Column(column, scrollable = True,vertical_scroll_only=True,size=(1600,800), key  = 'Column', element_justification='center')],
            # [sg.Image(filename=PATH, key = '-gif-'), sg.Image(filename=PATH2, key = '-gif1-'),sg.Image(filename=PATH3, key = '-gif2-'), sg.Image(filename=PATH4, key = '-gif3-'), sg.Image(filename=PATH5, key='-gif4-') ],
            # [sg.Image(filename=PATH6, key = '-gif5-'), sg.Image(filename=PATH7, key = '-gif6-'),sg.Image(filename=PATH8, key = '-gif7-')],
            # [sg.Image(filename=PATH9, key = '-gif8-'), sg.Image(filename=PATH10, key = '-gif9-'), sg.Image(filename=PATH11, key = '-gif10-'), sg.Image(filename=PATH12, key = '-gif11-')],
            # [sg.Image(filename=PATH13, key = '-gif12-'), sg.Image(filename=PATH14, key = '-gif13-'),sg.Image(filename=PATH15, key = '-gif14-')],
            # [sg.Image(filename=PATH16, key = '-gif15-'), sg.Image(filename=PATH17, key = '-gif16-'),sg.Image(filename=PATH18, key = '-gif17-')]
            ]
            window2 = sg.Window(event, layout, grab_anywhere=False, element_justification='center')
            while True:

                event, values = window2.read(timeout=75)
                if event == sg.WIN_CLOSED:
                    break
                window2.Element('-gif-').UpdateAnimation(PATH, time_between_frames=16)
                window2.Element('-gif1-').UpdateAnimation(PATH2, time_between_frames=16)
                window2.Element('-gif2-').UpdateAnimation(PATH3, time_between_frames=16)
                window2.Element('-gif3-').UpdateAnimation(PATH4, time_between_frames=16)
                window2.Element('-gif4-').UpdateAnimation(PATH5, time_between_frames=16)
                window2.Element('-gif5-').UpdateAnimation(PATH6, time_between_frames=16)
                window2.Element('-gif6-').UpdateAnimation(PATH7, time_between_frames=16)
                window2.Element('-gif7-').UpdateAnimation(PATH8, time_between_frames=16)
                window2.Element('-gif8-').UpdateAnimation(PATH9, time_between_frames=16)
                window2.Element('-gif9-').UpdateAnimation(PATH10, time_between_frames=16)
                window2.Element('-gif10-').UpdateAnimation(PATH11, time_between_frames=16)
                window2.Element('-gif11-').UpdateAnimation(PATH12, time_between_frames=16)
                window2.Element('-gif12-').UpdateAnimation(PATH13, time_between_frames=16)
                window2.Element('-gif13-').UpdateAnimation(PATH14, time_between_frames=16)
                window2.Element('-gif14-').UpdateAnimation(PATH15, time_between_frames=16)
                window2.Element('-gif15-').UpdateAnimation(PATH16, time_between_frames=16)
                window2.Element('-gif16-').UpdateAnimation(PATH17, time_between_frames=16)
                window2.Element('-gif18-').UpdateAnimation(PATH19, time_between_frames=16)

        # layout = [ [sg.Text('Test', font = ('Times New Roman', 20))]]
        # window2 = sg.Window('Frame Data', layout)
        # event, values = window.read()
    window.close()

# Re-roll the list for a new random order of characters.
def reroll(topRow ,bottomRow):
    newList = charList.copy()
    rd.shuffle(newList)
    for i in range(len(newList)):
        print(newList[i])
    print()
    for i in range(0,2):

        for j in range(0, 9):
            topRow[i][j].Update(filename=newList[j + (i*9)][0])

    for i in range(0, 8):
        bottomRow[i+1].Update(filename = newList[i+18][0])

# Function responsible for the Iron Man Generator window. Provides a random list every re-roll.
def ironManGenerator():

    newList = charList.copy()
    rd.shuffle(newList)
    for i in range(len(newList)):
        print(newList[i])
    print()

    layout = []
    topRow = []

    # Nested loop that makes Images for the first two rows of characters.
    for i in range(0,2):
        rowList = [] 
        
        for j in range (0, 9): 
            rowList.append(sg.Image(filename=newList[j + (i*9)][0], key = newList[j + (i*9)][1]))
        
        topRow.append(rowList)

    bottomRow = []

    # Makes the third row of characters.
    bottomRow.append(sg.Text('            ')) 
    for i in range (18, 26):
        bottomRow.append(sg.Image(filename=newList[i][0], key = newList[i][1]))

    layout = topRow + [bottomRow]
    
    layout.append([sg.Button('Re-roll')])
    window = sg.Window('Test', layout, element_justification = 'center')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Re-roll':
            reroll(topRow, bottomRow)

    window.close()
    
if __name__ == '__main__':
    sg.theme('Dark Blue 3')   # Add a touch of color

    layout = [  [sg.Text('Welcome to the [MELEE PROJECT]', font=('Times New Roman', 20) ) ],
                [sg.Text('What would you like to do?')],
                [sg.Button(button_text='Stats'), sg.Button(button_text='Frame Data'), sg.Button('Iron Man')],
                [sg.Button(button_text='Options'), sg.Button(button_text='About')] ]

    window = sg.Window('Melee Project', layout, element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Stats':
            statsWindow(event)
        elif event == 'Iron Man':
            ironManGenerator()
        elif event == 'Frame Data':
            frameDataWindow()
        print(event, values)
        #sg.Popup(event)

    window.close()

