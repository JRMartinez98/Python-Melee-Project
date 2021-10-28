import PySimpleGUI as sg
import random as rd
import openpyxl as op

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

FrameData = {'-DR.MARIO-': 'Melee Project/Frame Data/Dr. Mario/',
                '-MARIO-' : 'Melee Project/Frame Data/Mario/',
                '-LUIGI-' : 'Melee Project/Frame Data/Luigi/',
                '-BOWSER-' : 'Melee Project/Frame Data/Bowser/',
                '-PEACH-' : 'Melee Project/Frame Data/Peach/',
                '-YOSHI-' : 'Melee Project/Frame Data/Yoshi/',
                '-DK-' : 'Melee Project/Frame Data/Donkey Kong/',
                '-FALCON-' : 'Melee Project/Frame Data/Captain Falcon/',
                '-GANON-' : 'Melee Project/Frame Data/Ganondorf/',
                '-FALCO-' : 'Melee Project/Frame Data/Falco/',
                '-FOX-' : 'Melee Project/Frame Data/Fox/',
                '-NESS-' : 'Melee Project/Frame Data/Ness/',
                '-ICE CLIMBERS-' : 'Melee Project/Frame Data/Ice Climbers/',
                '-KIRBY-' : 'Melee Project/Frame Data/Kirby/',
                '-SAMUS-' : 'Melee Project/Frame Data/Samus/',
                '-ZELDA-' : 'Melee Project/Frame Data/Zelda/',
                '-LINK-' : 'Melee Project/Frame Data/Link/',
                '-YLINK-' : 'Melee Project/Frame Data/Young Link/',
                '-PICHU-' : 'Melee Project/Frame Data/Pichu/',
                '-PIKACHU-' : 'Melee Project/Frame Data/Pikachu/',
                '-PUFF-' : 'Melee Project/Frame Data/Jigglypuff/',
                '-MEWTWO-' : 'Melee Project/Frame Data/Mewtwo/',
                '-G&W-' : 'Melee Project/Frame Data/Mr. Game & Watch/',
                '-MARTH-' : 'Melee Project/Frame Data/Marth/',
                '-ROY-' : 'Melee Project/Frame Data/Roy/',
                '-SHEIK-' : 'Melee Project/Frame Data/Sheik/'
}

ExcelCol = {'-DR.MARIO-': 'A',
                '-MARIO-' : 'B',
                '-LUIGI-' : 'C',
                '-BOWSER-' : 'D',
                '-PEACH-' : 'E',
                '-YOSHI-' : 'F',
                '-DK-' : 'G',
                '-FALCON-' : 'H',
                '-GANON-' : 'I',
                '-FALCO-' : 'J',
                '-FOX-' : 'K',
                '-NESS-' : 'L',
                '-ICE CLIMBERS-' : 'M',
                '-KIRBY-' : 'N',
                '-SAMUS-' : 'O',
                '-ZELDA-' : 'P',
                '-LINK-' : 'Q',
                '-YLINK-' : 'R',
                '-PICHU-' : 'S',
                '-PIKACHU-' : 'T',
                '-PUFF-' : 'U',
                '-MEWTWO-' : 'V',
                '-G&W-' : 'W',
                '-MARTH-' : 'X',
                '-ROY-' : 'Y',
                '-SHEIK-' : 'Z',      
}

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

# Re-roll the list for a new random order of characters.
def reroll(topRow ,bottomRow):
    rd.shuffle(charList)
    for i in range(len(charList)):
        print(charList[i])
    print()
    for i in range(0,2):

        for j in range(0, 9):
            topRow[i][j].Update(filename=charList[j + (i*9)][0])

    for i in range(0, 8):
        bottomRow[i+1].Update(filename = charList[i+18][0])



#----------------------------------------------------#
#                                                    #
#                 MAIN BEGINS HERE                   #
#                                                    #
#----------------------------------------------------#



charLayout = charSelectLayout('Button')


#----------------Excel testing-----------------------
path = "C:\\Users\\Jose\\Desktop\\Melee-Project.xlsx"

wb_obj = op.load_workbook(path)
sheet_obj = wb_obj.active


cell_obj = sheet_obj.cell(row = 1, column = 1)
#----------------------------------------------------


#This massive segment of code is for testing the layout for frame data windows and testing the use of excel.
window = sg.Window('Frame data', charLayout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event in FrameData:
        
        files = []
        paths = []
        
        i = 0
        for cell in sheet_obj[ExcelCol[event]]:
            if i > 0 and cell.value != None:
                files.append(cell.value)
            i = i + 1
        
        for img in files:
            paths.append(FrameData[event]+img)
        
        i = 0
        column = [[sg.Text('Ground Attacks', font=('Calibri', 36), justification='center')]]
        line = []
        for path in paths:
            if i % 4 == 3:
                column.append(line)
                line = []
            line.append(sg.Image(filename = path, key = '-gif' + str(i) + '-')) 
            i = i + 1

        
        column.append(line)

        print(event, FrameData[event])
        PATH = FrameData[event]+'/nair.gif'
        PATH2 = FrameData[event]+'/uair.gif'
        PATH3 = FrameData[event]+'/fair.gif'
        PATH4 = FrameData[event]+'/bair.gif'
        PATH5 = FrameData[event]+'/dair.gif'
        PATH6 = FrameData[event]+'/jab1.gif'
        PATH7 = FrameData[event]+'/jab2.gif'
        PATH8 = FrameData[event]+'/jab3.gif'
        PATH9 = FrameData[event]+'/utilt.gif'
        PATH10 = FrameData[event]+'/ftilt.gif'
        PATH11 = FrameData[event]+'/dtilt.gif'
        PATH12 = FrameData[event]+'/dattack.gif'
        PATH13 = FrameData[event]+'/fsmash.gif'
        PATH14 = FrameData[event]+'/dsmash.gif'
        PATH15 = FrameData[event]+'/usmash.gif'
        PATH16 = FrameData[event]+'/neutralb.gif'
        PATH17 = FrameData[event]+'/sideb.gif'
        PATH18 = FrameData[event]+'/upb.gif'
        
        #column = [ 
        #[sg.Image(filename=PATH, key = '-gif-'), sg.Image(filename=PATH2, key = '-gif1-'),sg.Image(filename=PATH3, key = '-gif2-'), sg.Image(filename=PATH4, key = '-gif3-'), sg.Image(filename=PATH5, key='-gif4-')],
        #[sg.Image(filename=PATH6, key = '-gif5-'), sg.Image(filename=PATH7, key = '-gif6-'),sg.Image(filename=PATH8, key = '-gif7-')],
        #[sg.Image(filename=PATH9, key = '-gif8-'), sg.Image(filename=PATH10, key = '-gif9-'), sg.Image(filename=PATH11, key = '-gif10-'), sg.Image(filename=PATH12, key = '-gif11-')],
        #[sg.Image(filename=PATH13, key = '-gif12-'), sg.Image(filename=PATH14, key = '-gif13-'),sg.Image(filename=PATH15, key = '-gif14-')],
        #[sg.Image(filename=PATH16, key = '-gif15-'), sg.Image(filename=PATH17, key = '-gif16-'),sg.Image(filename=PATH18, key = '-gif17-')]
        #] [sg.Text('Aerials', font=('Calibri', 36), justification='center')]

        layout = [ [sg.Column(column, scrollable = True,vertical_scroll_only=True,size=(1600,1000), key  = 'Column', element_justification='center')]]

        window2 = sg.Window(event, layout,grab_anywhere=False, element_justification='center')
        while True:

            event, values = window2.read(timeout=75)
            if event == sg.WIN_CLOSED:
                break

            for i in range(0, len(paths)):
                print(i)
                window2.Element('-gif' + str(i) + '-').UpdateAnimation(paths[i], time_between_frames = 16)
            
            #window2.Element('-gif0-').UpdateAnimation(PATH, time_between_frames=16)
            #window2.Element('-gif1-').UpdateAnimation(PATH2, time_between_frames=16)
            #window2.Element('-gif2-').UpdateAnimation(PATH3, time_between_frames=16)
            #window2.Element('-gif3-').UpdateAnimation(PATH4, time_between_frames=16)
            #window2.Element('-gif4-').UpdateAnimation(PATH5, time_between_frames=16)
            #window2.Element('-gif5-').UpdateAnimation(PATH6, time_between_frames=16)
            #window2.Element('-gif6-').UpdateAnimation(PATH7, time_between_frames=16)
            #window2.Element('-gif7-').UpdateAnimation(PATH8, time_between_frames=16)
            #window2.Element('-gif8-').UpdateAnimation(PATH9, time_between_frames=16)
            #window2.Element('-gif9-').UpdateAnimation(PATH10, time_between_frames=16)
            #window2.Element('-gif10-').UpdateAnimation(PATH11, time_between_frames=16)
            #window2.Element('-gif11-').UpdateAnimation(PATH12, time_between_frames=16)
            #window2.Element('-gif12-').UpdateAnimation(PATH13, time_between_frames=16)
            #window2.Element('-gif13-').UpdateAnimation(PATH14, time_between_frames=16)
            #window2.Element('-gif14-').UpdateAnimation(PATH15, time_between_frames=16)
            #window2.Element('-gif15-').UpdateAnimation(PATH16, time_between_frames=16)
            #window2.Element('-gif16-').UpdateAnimation(PATH17, time_between_frames=16)
            #window2.Element('-gif17-').UpdateAnimation(PATH18, time_between_frames=16)

    # layout = [ [sg.Text('Test', font = ('Times New Roman', 20))]]
    # window2 = sg.Window('Frame Data', layout)
    # event, values = window.read()
window.close()