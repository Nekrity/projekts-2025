import pygame
import spritesheet
import RPGtext

pygame.init()
#parametrs
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_turn=False
pygame.display.set_caption('Asgore')

#intro text
intro_text_narator_line1=["*(A strange light fills the","*(Twilight is shining through",#27
                    "*(It seems your journey is","*(You're filled with",""]
intro_text_narator_line2=["room.)","the barrier.)",
                    "finally over.)","DETERMINATION.)",""]

#Spritesheets
sprite_sheet_heart_image = pygame.image.load('images/souls.png').convert_alpha()
sprite_sheet_heart = spritesheet.SpriteSheet_Player(sprite_sheet_heart_image)

sprite_sheet_buttons_image = pygame.image.load('images/buttons.png').convert_alpha()
sprite_sheet_buttons = spritesheet.SpriteSheet_Buttons(sprite_sheet_buttons_image)

sprite_sheet_asgore_image = pygame.image.load('images/asgore.png').convert_alpha()
sprite_sheet_asgore = spritesheet.SpriteSheet_Asgore(sprite_sheet_asgore_image)

sprite_sheet_textbubble_image = pygame.image.load('images/textbubble.png').convert_alpha()
sprite_sheet_textbubble = spritesheet.SpriteSheet_Textbubble(sprite_sheet_textbubble_image)

#colors
BACKGROUND = (50, 50, 50)
BLACK = (0, 0, 0)
PINK = (195,134,255)
PINK_2 = (255,102,255)
WHITE = (255,255,255)


#Getting soul images
player_default = sprite_sheet_heart.get_image(16, 16, BLACK)
player_menu = sprite_sheet_heart.get_image(16, 16, BLACK)

#changing window icon
pygame.display.set_icon(player_default)

#Getting button images
button_fight = sprite_sheet_buttons.get_image(110, 42, BACKGROUND,1)
button_act = sprite_sheet_buttons.get_image(110, 42, BACKGROUND,0)
button_item = sprite_sheet_buttons.get_image(110, 42, BACKGROUND,2)
button_mercy = sprite_sheet_buttons.get_image(110, 42, BACKGROUND,3)

buttons=[button_fight,button_act,button_item,button_mercy]

buttons_white=[button_fight.copy(),button_act.copy(),button_item.copy(),button_mercy.copy()]
for button in buttons_white:
    color_change = pygame.PixelArray(button)
    color_change.replace((0,0,0), (255,255,255))
    color_change.replace((255,127,39), (0,0,0))
    del color_change

button_fight_selected = sprite_sheet_buttons.get_image_selected(110, 42, BACKGROUND,1)
button_act_selected = sprite_sheet_buttons.get_image_selected(110, 42, BACKGROUND,0)
button_item_selected = sprite_sheet_buttons.get_image_selected(110, 42, BACKGROUND,2)

buttons_selected=[button_fight_selected,button_act_selected,button_item_selected]

#Getting asgore images

asgore_faces=[]
asgore_intro_anim=[]
for i in range(16):
    asgore_face = sprite_sheet_asgore.get_image((5+54*i), 23, 49, 54, PINK)
    asgore_faces.append(asgore_face)
for i in range(14):
    asgore_intro = sprite_sheet_asgore.get_image((5+290*(i%5)), (317+127*(i//5)), 285, 122, PINK)
    asgore_intro_anim.append(asgore_intro)
asgore_intro=asgore_intro_anim[0].copy()
color_change = pygame.PixelArray(asgore_intro)
color_change.replace((255,255,255), (0,0,0))
del color_change
asgore_intro_anim.append(asgore_intro)

asgore_intro_body=sprite_sheet_asgore.get_image(16, 193, 159, 100, BLACK)

asgore_flash=sprite_sheet_asgore.get_image(5, 716, 159, 113, PINK)

asgore_trident=sprite_sheet_asgore.get_image(295, 716, 240, 62, PINK)

asgore_cape_1=sprite_sheet_asgore.get_image(5, 885, 159, 82, PINK)

asgore_cape_2=sprite_sheet_asgore.get_image(169, 885, 159, 82, PINK)

asgore_cape=[asgore_cape_1,asgore_cape_2]

asgore_battle_face=sprite_sheet_asgore.get_image(333, 885, 47, 45, PINK)

asgore_upper_body=sprite_sheet_asgore.get_image(385, 885, 115, 55, PINK)

asgore_left_hand=sprite_sheet_asgore.get_image(505, 885, 20, 14, PINK)
asgore_left_hand=pygame.transform.rotate(asgore_left_hand,-25)

asgore_right_hand=sprite_sheet_asgore.get_image(530, 885, 20, 14, PINK)
asgore_right_hand=pygame.transform.rotate(asgore_right_hand,-25)

asgore_left_shoulder=sprite_sheet_asgore.get_image(580, 885, 22, 39, PINK)
asgore_right_shoulder=sprite_sheet_asgore.get_image(607, 885, 24, 42, PINK)

asgore_lower_body=sprite_sheet_asgore.get_image(636, 885, 65, 34, PINK)

asgore_legs=sprite_sheet_asgore.get_image(706, 885, 63, 28, PINK)

asgore_feet=sprite_sheet_asgore.get_image(774, 885, 85, 9, PINK)

asgore_left_forearm=sprite_sheet_asgore.get_image(555, 885, 20, 20, PINK)
asgore_right_forearm=sprite_sheet_asgore.get_image(555, 885, 20, 20, PINK)

asgore_left_forearm=pygame.transform.scale(asgore_left_forearm, (40, 40 * 1.3))
asgore_left_forearm=pygame.transform.rotate(asgore_left_forearm,-20)

asgore_right_forearm=pygame.transform.scale(asgore_right_forearm, (40, 40 * 1.1))
asgore_right_forearm=pygame.transform.rotate(asgore_right_forearm,-20)

color_change = pygame.PixelArray(asgore_trident)
color_change.replace((255,255,255), (255,26,3))
color_change.replace((100,100,100), (91,13,18))
del color_change
textbubble = sprite_sheet_textbubble.get_image(99, 108, PINK_2)
screen_flash = pygame.Surface((640,480)) 
screen_flash.set_alpha(0)    
screen_flash.fill((255,255,255))  


#font
font="fonts/8bitoperator_jve.ttf"

#soundefects
move = pygame.mixer.Sound("soundefects/snd_spearappear.wav")
trident = pygame.mixer.Sound("soundefects/blade.wav")
mercy_broken = pygame.mixer.Sound("soundefects/mercy_broken.wav")
menu_move_sound = pygame.mixer.Sound("soundefects/snd_squeak.wav")
menu_select_sound = pygame.mixer.Sound("soundefects/snd_select.wav")

def intro():
    #setting events
    narrator_current_text=0
    asgore_talking=False
    asgore_moving_left=False
    asgore_trident_appear=False
    asgore_moving_right=False
    trident_breaking_mercy=False
    fade_effect=False
    intro = True
    norepeat=False
    #asgore default
    current_asgore_face=asgore_faces[0]
    asgore_face_pos=[260,3]
    asgore_intro_body_pos=[144,55]
    trident_pos=[165,55]
    moveleft=0
    moveright=0
    trident_offset=-4.5
    trident_movement=0
    frame=0
    asgore_text_cur=0

    #cooldowns
    move_cooldown=25
    trident_appear_cooldown=60
    cooldown=750
    intro_cooldown=3000
    last_tick=0
    
    transparency=256

    #textlines
    text_line1 = RPGtext.Text(intro_text_narator_line1[narrator_current_text], font, 30, -10,False, 0.35)
    text_line2 = RPGtext.Text("", font, 30, 0,False, 0.35)
    text_line3 = RPGtext.Text("", font, 15, 0,False, 0.35)
    text_line4 = RPGtext.Text("", font, 15, 0,False, 0.35)
    centered=False

    #playing music
    pygame.mixer.music.load('music/bergentruckung.wav')
    pygame.mixer.music.play(1)

    #setting timer events
    next_text=pygame.USEREVENT
    freeze=pygame.USEREVENT+1
    next_line=pygame.USEREVENT+2
    asgore_text=pygame.USEREVENT+3
    asgore_next_line=pygame.USEREVENT+4
    asgore_next_line1=pygame.USEREVENT+5
    asgore_next_line2=pygame.USEREVENT+6
    pygame.time.set_timer(next_text,4150,4)
    pygame.time.set_timer(freeze,16000,1)
    pygame.time.set_timer(next_line,2000,1)
    pygame.time.set_timer(asgore_text,19000,1)
    while intro:
        current_tick=pygame.time.get_ticks()

        #update background
        if asgore_moving_right or trident_breaking_mercy:
            screen.fill(WHITE)
        else:
            screen.fill(BLACK)

        #loading images
        button_num=0
        if fade_effect==False:
            #loading buttons
            if asgore_moving_right or trident_breaking_mercy:
                for button in buttons_white:
                    screen.blit(button, ((32+button_num*152),432))
                    button_num+=1
            else:
                for button in buttons:
                    screen.blit(button, ((32+button_num*152),432))
                    button_num+=1

            if asgore_moving_left and moveleft==5 and current_tick-last_tick>=cooldown:
                asgore_trident_appear=True
                asgore_moving_left=False
            if asgore_moving_right and moveright==20 and current_tick-last_tick>=cooldown:
                asgore_moving_right=False
                trident_breaking_mercy=True
                norepeat=False
            if asgore_trident_appear:
                if norepeat==False: #playing trident sound
                    pygame.mixer.Sound.play(trident)
                    norepeat=True
                screen.blit(asgore_intro_anim[frame], (24,15))
                if current_tick-last_tick>=trident_appear_cooldown and frame<13:
                    frame+=1
                    last_tick=current_tick
            elif asgore_moving_right or trident_breaking_mercy:
                screen.blit(asgore_intro_anim[14], [asgore_intro_body_pos[0],15])
                screen.blit(trident_img, trident_pos)
            else:
                screen.blit(current_asgore_face, asgore_face_pos)
                screen.blit(asgore_intro_body, asgore_intro_body_pos)
            if asgore_moving_left and current_tick-last_tick>=move_cooldown and moveleft<5: #asgore moving left
                asgore_intro_body_pos[0]-=24
                asgore_face_pos[0]-=24
                last_tick=current_tick
                moveleft+=1
            if frame==13 and current_tick-last_tick>=cooldown and asgore_moving_right==False and trident_breaking_mercy==False:
                pygame.mixer.Sound.play(move)
                asgore_moving_right=True
                asgore_trident_appear=False

            if asgore_moving_right and current_tick-last_tick>=move_cooldown and moveright<20: #asgore moving right
                asgore_intro_body_pos[0]+=16
                trident_pos[0]+=16
                trident_pos[1]-=16
                trident_img=pygame.transform.rotate(asgore_trident,trident_offset)
                last_tick=current_tick
                trident_offset-=4.5
                moveright+=1
            if trident_breaking_mercy and current_tick-last_tick>=move_cooldown and trident_movement<9: #trident breaking mercy
                if norepeat==False: #playing mercy breaking sound
                    pygame.mixer.Sound.play(mercy_broken)
                    norepeat=True

                trident_pos[1]+=120
                last_tick=current_tick
                trident_movement+=1
            if narrator_current_text==3: #centering narrator's text
                centered=True
                text_line1.render(screen,(320, 285),centered)
                text_line2.render(screen,(350, 315),centered)
            elif asgore_talking: #asgore text
                screen.blit(textbubble, (440,90))
                text_line1.render(screen,(460, 100),centered)
                text_line2.render(screen,(460, 120),centered)
                text_line3.render(screen,(460, 140),centered)
                text_line4.render(screen,(460, 160),centered)
            else: #narrator's text
                centered=False
                text_line1.render(screen,(30, 285),centered)
                text_line2.render(screen,(50, 315),centered)

            #screen flashes
            if frame==2:
                screen_flash.set_alpha(128)
                screen.blit(screen_flash, (0,0))
            if frame==3:
                screen_flash.set_alpha(256)
                screen.blit(screen_flash, (0,0))
            if frame==4:
                screen_flash.set_alpha(128)
                screen.blit(screen_flash, (0,0))
            if trident_movement==4:
                screen_flash.set_alpha(64)
                screen.blit(screen_flash, (0,0))
            if trident_movement==5:
                screen_flash.set_alpha(128)
                screen.blit(screen_flash, (0,0))
            if trident_movement==6:
                screen_flash.set_alpha(192)
                screen.blit(screen_flash, (0,0))
            if trident_movement>=7:
                screen_flash.set_alpha(256)
                screen.blit(screen_flash, (0,0))
            if trident_movement==9 and current_tick-last_tick>=cooldown:
                fade_effect=True
                trident_breaking_mercy=False
        else:
            #fadeout effect
            if current_tick-last_tick>=move_cooldown and transparency>0:
                transparency-=16
                screen_flash.set_alpha(transparency)
                screen.blit(screen_flash, (0,0))
                last_tick=current_tick
            else:
                screen.blit(screen_flash, (0,0))
            if transparency==0 and current_tick-last_tick>=intro_cooldown:
                intro=False
        #event handler
        for event in pygame.event.get():
            if event.type == freeze:
                pygame.time.wait(2000)
            if event.type == pygame.QUIT:
                intro = False
            if event.type==next_text: #changing narrator's text
                narrator_current_text+=1
                text_line1 = RPGtext.Text(intro_text_narator_line1[narrator_current_text], font, 30, -10,False, 0.35)
                text_line2 = RPGtext.Text("", font, 30, 1,False, 0.35)
                if narrator_current_text==1:
                    pygame.time.set_timer(next_line,2400,1)
                else:
                    pygame.time.set_timer(next_line,2000,1)
            if event.type==next_line: #narrator's text second line
                text_line2 = RPGtext.Text(intro_text_narator_line2[narrator_current_text], font, 30, -10,False, 0.35)
            if event.type==asgore_text: #asgore 1 text
                asgore_talking=True
                text_line1 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>Human...', font, 15, -8,False, 0.35)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_z and asgore_talking:
                    asgore_text_cur+=1
                    if asgore_text_cur==1: #asgore 2 text 1 line
                        current_asgore_face=asgore_faces[1]
                        text_line1 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>It was', font, 15, -8,False, 0.35)
                        pygame.time.set_timer(asgore_next_line,500,1)
                    elif asgore_text_cur==2: #asgore 3 text
                        text_line2 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        text_line3 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        text_line4 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        current_asgore_face=asgore_faces[0]
                        text_line1 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>Goodbye.', font, 15, -8,False, 0.35)
                    else:
                        text_line1 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        current_asgore_face=asgore_faces[2]
                        last_tick=pygame.time.get_ticks()
                        asgore_talking=False
                        asgore_moving_left=True
                        pygame.mixer.Sound.play(move)
            if event.type==asgore_next_line: #asgore 2 text 2 line
                text_line2 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>nice to', font, 15, -8,False, 0.35)
                pygame.time.set_timer(asgore_next_line1,500,1)
            if event.type==asgore_next_line1: #asgore 2 text 3 line
                text_line3 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>meet', font, 15, -8,False, 0.35)
                pygame.time.set_timer(asgore_next_line2,500,1)
            if event.type==asgore_next_line2: #asgore 2 text 4 line
                text_line4 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>you.', font, 15, -8,False, 0.35)
        #FPS
        dt = clock.tick(30) / 1000
        pygame.display.update()

menu_text=["* ASGORE attacks!","* ..."]
fight_and_act_select_text="* ASGORE"
def battle():
    battle_start=False
    norepeat=True
    display_battle_asgore=False
    trident_img=pygame.transform.rotate(asgore_trident,-25)
    battle = True
    start_cooldown=1000
    font="fonts/8bitoperator_jve.ttf"
    selected=0
    player_turn=True
    cape_cooldown=325
    current_cape=0
    turn=1
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_menu_pos=[0,0]

    #asgore_healthbar=healthbar()

    #battle box
    battle_box_color=(255, 255, 255)
    battle_box_inside_color=(0, 0, 0)

    #textlines
    menu_textline_1 = RPGtext.Text(menu_text[0], font, 30, -15,False, 0.35)
    menu_textline_2 = RPGtext.Text("", font, 30, -15,False, 0.35)
    menu_textline_3 = RPGtext.Text("", font, 30, -15,False, 0.35)
    sub_menu_textline_1 = RPGtext.Text("", font, 30, -15,False)
    sub_menu_textline_2 = RPGtext.Text("", font, 30, -15,False)
    sub_menu_textline_3 = RPGtext.Text("", font, 30, -15,False)
    sub_menu_textline_4 = RPGtext.Text("", font, 30, -15,False)

    #menu selection(players turn)
    menu_select=True
    fight_select=False
    act_select=False
    act_action_select=False
    item_select=False

    #playing music
    pygame.mixer.music.load('music/ASGORE.wav')
    pygame.mixer.music.play(-1)
    last_tick=pygame.time.get_ticks()
    while battle:
        current_tick=pygame.time.get_ticks()
        if battle_start:
            #buttons
            if player_turn==False:
                menu_select=False
            #buttons
            for i in range(3):
                if selected==i and player_turn:
                    screen.blit(buttons_selected[i], ((32+i*152),432))
                else:
                    screen.blit(buttons[i], ((32+i*152),432))
            #Asgore battle sprite
            if display_battle_asgore:
                screen.blit(asgore_cape[current_cape], [160,71])
                screen.blit(asgore_right_shoulder, [376,78])
                screen.blit(asgore_left_shoulder, [222,78])
                screen.blit(asgore_upper_body, [208,42])
                screen.blit(asgore_battle_face, [276,17])
                screen.blit(asgore_legs, [262,164])
                screen.blit(asgore_lower_body, [258,141])
                screen.blit(asgore_feet, [240,216])
                screen.blit(asgore_right_forearm, [378,120])
                screen.blit(asgore_left_forearm, [200,86])

                screen.blit(trident_img, [149,10])
                screen.blit(asgore_right_hand, [369,147])
                
                screen.blit(asgore_left_hand, [214,73])

                #cape animation
                if current_tick-last_tick>=cape_cooldown:
                    current_cape+=1
                    if current_cape>1:
                        current_cape=0
                    last_tick=current_tick

            #battle box
            pygame.draw.rect(screen,battle_box_color , [32, 250, 575, 140], 5)
            pygame.draw.rect(screen,battle_box_inside_color , [37, 255, 565, 130], 0)
            #menu
            if player_turn:
                if menu_select:
                    sub_menu_textline_1 = RPGtext.Text("", font, 30, -15,False)
                    sub_menu_textline_2 = RPGtext.Text("", font, 30, -15,False)
                    sub_menu_textline_3 = RPGtext.Text("", font, 30, -15,False)
                    sub_menu_textline_4 = RPGtext.Text("", font, 30, -15,False)
                    player_menu_pos=[40+153*selected,446]
                    screen.blit(player_menu, player_menu_pos)
                    if turn>1 and norepeat:
                        menu_textline_1 = RPGtext.Text(menu_text[1], font, 30, -15,False, 0.35)
                        norepeat=False
                    elif norepeat:
                        menu_textline_1 = RPGtext.Text(menu_text[0], font, 30, -15,False, 0.35)
                        norepeat=False
                    
                    
                elif fight_select:
                    player_menu_pos=[64,278]
                    screen.blit(player_menu, player_menu_pos)
                    if norepeat:
                        sub_menu_textline_1 = RPGtext.Text(fight_and_act_select_text, font, 30, -15,False)
                        menu_textline_1 = RPGtext.Text("", font, 30, -15,False, 0.35)
                        norepeat=False
                elif act_select:
                    player_menu_pos=[64,278]
                    screen.blit(player_menu, player_menu_pos)
                    if norepeat:
                        sub_menu_textline_1 = RPGtext.Text(fight_and_act_select_text, font, 30, -15,False)
                        menu_textline_1 = RPGtext.Text("", font, 30, -15,False, 0.35)
                        norepeat=False
                elif act_action_select:
                    print("a")
                elif item_select:
                    print("a")
                menu_textline_1.render(screen,(52, 270),False)
                menu_textline_2.render(screen,(52, 304),False)
                sub_menu_textline_1.render(screen,(99, 270),False)
                sub_menu_textline_2.render(screen,(99, 304),False)
                sub_menu_textline_3.render(screen,(339, 270),False)
                sub_menu_textline_4.render(screen,(339, 304),False)
        #1 second delay to start with music
        if battle_start==False and current_tick-last_tick>=start_cooldown:
            battle_start=True
            display_battle_asgore=True
            last_tick=current_tick
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battle = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and player_turn:
                    if menu_select:
                        selected-=1
                        if selected<0:
                            selected=2
                        pygame.mixer.Sound.play(menu_move_sound)
                if event.key==pygame.K_RIGHT and player_turn:
                    if menu_select:
                        selected+=1
                        if selected>2:  
                            selected=0
                        pygame.mixer.Sound.play(menu_move_sound)
                if event.key==pygame.K_z and player_turn:
                    if menu_select:
                        if selected==0:
                            menu_select=False
                            fight_select=True
                            norepeat=True
                        elif selected==1:
                            menu_select=False
                            act_select=True
                            norepeat=True
                        else:
                            menu_select=False
                            item_select=True
                            norepeat=True
                    pygame.mixer.Sound.play(menu_select_sound)
                if event.key==pygame.K_x and player_turn:
                    if fight_select or act_select or item_select:
                        menu_select=True
                        fight_select=False
                        act_select=False
                        item_select=False
                        norepeat=True

                if event.key==pygame.K_p:
                    if player_turn==True:
                        player_turn=False
                        print(player_turn)
                    else:
                        turn+=1
                        player_turn=True
                        menu_select=True
                        norepeat=True
                        print(turn)
                        print(player_turn)

        #keys
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP] and player_turn==False:
            #player_pos.y -= 150 * dt
        #if keys[pygame.K_DOWN] and player_turn==False:
            #player_pos.y += 150 * dt
        #if keys[pygame.K_LEFT] and player_turn==False:
            #player_pos.x -= 150 * dt
        #if keys[pygame.K_RIGHT] and player_turn==False:
            #player_pos.x += 150 * dt
        #if keys[pygame.K_p]:
            #if player_turn==True:
                #player_turn=False
                #print(player_turn)
            #else:
                #player_turn=True
                #print(player_turn)
        dt = clock.tick(30) / 1000
        pygame.display.update()
def damage_taken(current_health, asgore_attack):
    if current_health==1:
        new_health=0
    elif current_health-asgore_attack<1:
        new_health=1
    else:
        new_health=current_health-asgore_attack
    return new_health
class healthbar():
    def __init__(self, x, y, width, height, current_hp,max_hp):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.current_hp = current_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.current_hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))
intro()
battle()
pygame.quit()