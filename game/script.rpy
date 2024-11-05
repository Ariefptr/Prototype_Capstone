image hutan = im.Scale("hutan.jpg",1280,720)

init python:
    
    def piece_dragged(drags, drop):
        
        if not drop:
            return
        
        p_x = drags[0].drag_name[0]
        p_y = drags[0].drag_name[1]
        t_x = drop.drag_name[0]
        t_y = drop.drag_name[1]
        
        if p_x == t_x and p_y == t_y:
            renpy.music.play("click.ogg", channel="sound")
            my_x = int(p_x)*100+25
            my_y = int(p_y)*100+25
            drags[0].snap(my_x,my_y)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(6):
                for j in range(4):
                    if placedlist[i,j] == False:
                        return
            return True
        return

screen minigames:

    draggroup:

        for i in range(6):
            for j in range(4):
                $ name = "%s%s"%(i,j)
                $ my_x = i*100+50
                $ my_y = j*100+50
                drag:
                    drag_name name
                    child "blank1_space.png"
                    draggable False
                    xpos my_x ypos my_y
            
            
        for i in range(6):
            for j in range(4):
                $ name = "%s%s piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]

label puzzle:
    call screen minigames
    jump menangbro

# The game starts here.

label start:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    jump plolog_lah

label plolog_lah:
    scene envi_mom
    show larasati2 at left:
        zoom 0.31 yalign 0.76
    larasati "[text_prolog_larasati[0]]"

label mainkan_bro:
    larasati "[text_prolog_larasati[1]]"
    hide larasati 
    with dissolve
    image whole = "bulungmitos.jpg"
    play music "musike.mp3"
    scene hutan
    python:
        pajel = im.Composite((650, 450),(25, 25), "bulungmitos.jpg")
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        for i in range(6):
            for j in range(4):
                piecelist[i,j] = [renpy.random.randint(0, 600)+600, renpy.random.randint(0, 480)]
                tempimage = im.AlphaMask(pajel,"pazel_pieces/%s_%s.png"%(j+1,i+1))
                imagelist[i,j] =im.Crop(tempimage, i*100,j*100, 150, 150)
                placedlist[i,j] = False
    jump puzzle

label menangbro:
    scene black
    show whole at Position(xalign=0.5,yalign=0.5)
    stop music
    play sound "yay.mp3"
    "PUZZLE BERHASIL TERPECAHKAN"
    menu:
        "Main lagi?"
        
        "Ya":
            jump start
            
        "Tidak":
            return
# This ends the game.

