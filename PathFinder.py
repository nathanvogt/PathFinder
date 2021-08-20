import pygame as py
import time

class screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def initialize(self):
        self.dimensions = (self.width, self.height)
        #py.display.init()
        self.screen = py.display.set_mode(self.dimensions)
        self.screen.fill((255, 255, 255))
        py.display.set_caption('PathFinder')
        py.display.flip()

    def updateFrame(self, cell):
        #self.screen.fill((255, 255, 255))
        cell.draw(self.screen)
        py.display.update()

    def get_screen(self):
        return self.screen

class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border_color = (0, 0, 0)
        self.inner_color = (0, 255, 0)
        self.cell_border = ((x), (y), 12, 12)
        self.cell_inner = (x+1, y+1, 10, 10)

    def draw(self, screen):
        py.draw.rect(screen, self.border_color, self.cell_border)
        py.draw.rect(screen, self.inner_color, self.cell_inner)

    def check_in_bounds(self, x, y):
        if x <= (self.x + 11) and x >= (self.x + 1)and \
                y >= (self.y + 1) and y <= (self.y + 11):
            return True

    def set_cell_color(self, border_color, inner_color):
        self.border_color = border_color
        self.inner_color = inner_color

class array:
    def __init__(self):
        c = cell(0, 0)
        self.array = [c]
        self.y = 0
        self.x_cord = 0
        self.array.pop(0)
        for x in range((40*40)):
            if x != 0:
                self.x_cord += 1

            if self.x_cord > 39:
                self.y += 1
                self.x_cord = 0

            self.temp_cell = cell((self.x_cord*11), (self.y*11)+50)
            self.array.append(self.temp_cell)

    def get_array_element(self, x):
        return self.array[x]

#Functions-----------
marker = 0

def draw_obstacles(screen):
    pos = (30, 20)
    py.draw.circle(screen, (255, 0, 0), pos, 10)
    py.display.update()

    run = True
    while run:
        mouse_x, mouse_y = py.mouse.get_pos()

        mouse1, trash1, trash2 = py.mouse.get_pressed()

        for x in range((40 * 40) ):
            cell = a.get_array_element(x)

            if cell.check_in_bounds(mouse_x, mouse_y) and mouse1:
                black = (0, 0, 0)
                red = (255, 0, 0)
                cell.set_cell_color(black, red)
                obstacle_array[x] = True
                s.updateFrame(cell)

        keys = py.key.get_pressed()
        if keys[py.K_q]:
            pos = (30, 20)
            py.draw.circle(screen, (255, 255, 255), pos, 10)
            py.display.update()
            run = False


        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit()

def place_start():

    global start_point_placed
    global placed_start_index

    if start_point_placed:
        abstract_array[placed_start_index] = False
        black = (0, 0, 0)
        green = (0, 255, 0)
        a.get_array_element(placed_start_index).set_cell_color(black, green)
        cell = a.get_array_element(placed_start_index)
        s.updateFrame(cell)


    pos = (60, 20)
    py.draw.circle(s.get_screen(), (100, 100, 0), pos, 10)
    py.display.update()

    run = True
    while run:

        mouse_x, mouse_y = py.mouse.get_pos()

        mouse1, trash1, trash2 = py.mouse.get_pressed()

        keys = py.key.get_pressed()

        if keys[py.K_q]:
            pos = (60, 20)
            py.draw.circle(s.get_screen(), (255, 255, 255), pos, 10)
            py.display.update()
            run = False

        for x in range((40 * 40) ):
            global marker
            marker = x
            cell = a.get_array_element(x)

            if cell.check_in_bounds(mouse_x, mouse_y) and mouse1:
                black = (0, 0, 0)
                red = (0, 255, 255)
                cell.set_cell_color(black, red)
                abstract_array[marker] = True
                placed_start_index = marker
                start_point_placed = True
                s.updateFrame(cell)

                pos = (60, 20)
                py.draw.circle(s.get_screen(), (255, 255, 255), pos, 10)
                py.display.update()
                run = False

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit()

def place_finish():

    global end_point_placed
    global placed_end_index

    if end_point_placed:
        abstract_array[placed_end_index] = False
        black = (0, 0, 0)
        green = (0, 255, 0)
        a.get_array_element(placed_end_index).set_cell_color(black, green)
        cell = a.get_array_element(placed_end_index)
        s.updateFrame(cell)


    pos = (90, 20)
    py.draw.circle(s.get_screen(), (0, 100, 100), pos, 10)
    py.display.update()

    run = True
    while run:

        mouse_x, mouse_y = py.mouse.get_pos()

        mouse1, trash1, trash2 = py.mouse.get_pressed()

        keys = py.key.get_pressed()

        if keys[py.K_q]:
            pos = (90, 20)
            py.draw.circle(s.get_screen(), (255, 255, 255), pos, 10)
            py.display.update()
            run = False

        for x in range((40 * 40) ):
            global marker
            marker = x
            cell = a.get_array_element(x)
            if cell.check_in_bounds(mouse_x, mouse_y) and mouse1:
                black = (0, 0, 0)
                red = (255, 0, 255)
                cell.set_cell_color(black, red)
                abstract_array[marker] = True
                placed_end_index = marker
                end_point_placed = True
                s.updateFrame(cell)

                pos = (90, 20)
                py.draw.circle(s.get_screen(), (255, 255, 255), pos, 10)
                py.display.update()
                run = False

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit()


#----------------------
#------


#Important Stuff
abstract_array = [False]
abstract_array.pop(0)



for x in range((40*40)):
    abstract_array.append(False)

#Obstacle array
obstacle_array = [False]
obstacle_array.pop(0)

for x in range((40*40)):
    obstacle_array.append(False)



#track placed start point
start_point_placed = False
placed_start_index = None

#track placed end point
end_point_placed = False
placed_end_index = None

#initialize screen and array
width = (12*40)-50+50
height = (12*40)-28+50
s = screen(width, height)
a = array()
s.initialize()
#c.draw(s.get_screen())

#draw squares
for x in range((40*40)):
    cell = a.get_array_element(x)
    s.updateFrame(cell)
#---------



#close
run = True
mouseDown = False

#Draw points
while run:

    keys = py.key.get_pressed()

    if keys[py.K_d]:
        draw_obstacles(s.get_screen())
    elif keys[py.K_s]:
        place_start()
    elif keys[py.K_f]:
        place_finish()
    elif keys[py.K_RETURN]:
        break




    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()

#Find Path-------------


class spawner:
    def __init__(self):
        #print("made")
        pass
    def first_embrio(self, index, path):
        global womb
        embrio = index, path
        womb.append(embrio)
    def hatch(self):
        global path_run
        global womb
        global global_link
        while True:
            ref = womb[:]
            #print(ref, 'reference womb')
            womb.clear()
            #print(self.womb, "womb")
            iterate_block(ref)
            #print(womb, 'womb after it')

            '''if len(womb) <= 0:
                print('broken')
                break'''
            if len(successful_paths) >= 1:
                clean_womb()
                break
            if len(womb) <= 0:
                break





class block:
    def __init__(self, index, link, spath):
        self.index = index
        self.link = link
        #self.path = path[:]
        self.adj = []

    def find_adj(self):
        global global_link
        #Lock global_link
        self.link = global_link
#check above
        if self.index > 39:
            linked = False
            if not obstacle_array[self.index - 40]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index - 40):
                        linked = True
                if not linked:
                    self.adj.append(self.index - 40)
#check below
        if self.index < 1560:
            linked = False
            if not obstacle_array[self.index +40]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index + 40):
                        linked = True
                if not linked:
                    self.adj.append(self.index + 40)
#check left
        if self.index != 0 and (self.index % 40) != 0:
            linked = False
            if not obstacle_array[self.index -1]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index - 1):
                        linked = True
                if not linked:
                    self.adj.append(self.index -1)
#Check right
        if (self.index%40) != 39:
            linked = False
            if not obstacle_array[self.index + 1]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index + 1):
                        linked = True
                if not linked:
                    self.adj.append(self.index + 1)
#check up-left
        if (self.index > 39) and (self.index%40) != 0:
            linked = False
            if not obstacle_array[(self.index -41)]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index - 41):
                        linked = True
                if not linked:
                    cleared = True
                    if obstacle_array[self.index-40] and \
                        obstacle_array[self.index -1]:
                            cleared = False
                    if cleared:
                        self.adj.append(self.index - 41)

#check up-right
        if (self.index > 39) and (self.index%40) != 39:
            linked = False
            if not obstacle_array[self.index - 39]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index - 39):
                        linked = True
                if not linked:
                    cleared = True
                    if obstacle_array[self.index - 40] and \
                            obstacle_array[self.index + 1]:
                        cleared = False
                    if cleared:
                        self.adj.append(self.index - 39)

#check bottom-left
        if (self.index<1560) and (self.index % 40) != 0:
            linked = False
            if not obstacle_array[self.index+39]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index +39):
                        linked = True
                if not linked:
                    cleared = True
                    if obstacle_array[self.index + 40] and \
                            obstacle_array[self.index - 1]:
                        cleared = False
                    if cleared:
                        self.adj.append(self.index + 39)

#check bottom-right
        if (self.index<1560) and (self.index % 40) != 39:
            linked = False
            if not obstacle_array[self.index +41]:
                for x in range(len(self.link)):
                    if self.link[x] == (self.index +41):
                        linked = True
                if not linked:
                    cleared = True
                    if obstacle_array[self.index + 40] and \
                            obstacle_array[self.index + 1]:
                        cleared = False
                    if cleared:
                        self.adj.append(self.index + 41)

    def check_for_end(self, spath):
        global found
        ends = []
        global placed_end_index
        global successful_paths
        for x in range(len(self.adj)):
            if self.adj[x] == placed_end_index and not found:
                #self.path.append(self.index)
                #self.path.append(placed_end_index)
                #print("appending to succ")
                spath.append(self.index)
                successful_paths.append(spath)
                ends.append(True)
                paint_path(successful_paths)
                found = True
            else:
                ends.append(False)
        for x in range(len(ends)):
            if not ends[x]:
                '''print("not a path...pregnant")'''

    def birth(self, spath):
        global womb
        #Lock global_link
        global global_link
#Remove adj repeats
        for x in range(len(global_link)):
            for y in range(len(self.adj)):
                if self.adj[y] == global_link[x]:
                    self.adj.pop(y)
#Update link
        for x in range(len(self.adj)):
            global_link.append(self.adj[x])

#Add self to path
        spath.append(self.index)
#Add adjacent embrios to womb
        for x in range(len(self.adj)):
            global womb
            embrio = (self.adj[x], spath)
            womb.append(embrio)
        #print(womb)
        #print('check womb')

    def die(self):
        global a
        global s
        cell = a.get_array_element(self.index)
        black = (0, 0, 0)
        indicate = (150, 150, 150)
        cell.set_cell_color(black, indicate)
        s.updateFrame(cell)

    def clear_adj(self):
        self.adj.clear()



def clean_womb():
    global womb
    for x in range(len(womb)):
        try:
            womb.pop(x)
        except:
            pass

def iterate_block(womb_plant):
    global found
    global global_link

    for index, path in womb_plant:
        spath = path[:]
        #print(index, 'index')
        #print(path, "path")
        current_block = block(index, global_link, spath)
        current_block.find_adj()
        current_block.check_for_end(spath)
        current_block.birth(spath)
        if not found:
            current_block.die()
            continue
        current_block.clear_adj()
        #time.sleep(.5)

def refine_succ_paths(raw_paths, champs):
    for x in range(len(raw_paths)):
        tester = raw_paths[x]
        victorious = True
        for y in range(len(raw_paths)):
            if len(tester) > len(raw_paths[y]):
                vicorious = False
        if victorious:
            champs.append(tester)

def paint_path(best_paths):
    print(best_paths)
    for x in range(len(best_paths)):
        path = best_paths[x]
        for y in range(len(path)):
            cell = a.get_array_element(path[y])
            black = (0, 0, 0)
            indicate = (255, 192, 203)
            cell.set_cell_color(black, indicate)
            s.updateFrame(cell)

def womb_ref(womb):
    womb_ref = []
    for index, path in womb:
        #print(index, "index")
        #print(path, "path")
        embrio = index, path
        womb_ref.append(embrio)
    return womb_ref








#Global components------------
found = False

path_run = True
global_link = []
womb = []
successful_paths = []

best_paths = []

#embrios = (index, path)------

#Objects----
initial_path = []
spaw = spawner()
spaw.first_embrio(placed_start_index, initial_path)
global_link.append(placed_start_index)
spaw.hatch()
#paint_path(successful_paths)

#print(len(successful_paths), "paths")

#refine_succ_paths(successful_paths, best_paths)


#print(best_paths)
















fin_run = True
while fin_run:
    for event in py.event.get():
        if event.type == py.QUIT:
            fin_run = False
            py.quit()