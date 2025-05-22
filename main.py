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

intro_text_narator_line1=["*(A strange light fills the","*(Twilight is shining through",#27
                    "*(It seems your journey is","*(You're filled with",""]
intro_text_narator_line2=["room.)","the barrier.)",
                    "finally over.)","DETERMINATION.)",""]
intro_text_asgore=["Human...","It was nice to meet you.","Goodbye."]

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
BG = (50, 50, 50)
BLACK = (0, 0, 0)
PINK = (195,134,255)
PINK2 = (255,102,255)
WHITE = (255,255,255)


#Getting soul images
player_default = sprite_sheet_heart.get_image(16, 16, BLACK)

#Getting button images
button_fight = sprite_sheet_buttons.get_image(110, 42, BG,1)
button_act = sprite_sheet_buttons.get_image(110, 42, BG,0)
button_item = sprite_sheet_buttons.get_image(110, 42, BG,2)
button_mercy = sprite_sheet_buttons.get_image(110, 42, BG,3)
buttons=[button_fight,button_act,button_item,button_mercy]

#Getting asgore images
asgore_faces=[]
asgore_intro_anim=[]
for i in range(16):
    asgore_face = sprite_sheet_asgore.get_image((5+54*i), 23, 49, 54, PINK)
    asgore_faces.append(asgore_face)
for i in range(14):

    asgore_intro = sprite_sheet_asgore.get_image((5+290*(i%5)), (317+127*(i//5)), 285, 122, PINK)
    asgore_intro_anim.append(asgore_intro)

asgore_intro_body=sprite_sheet_asgore.get_image(16, 193, 159, 100, BLACK)

asgore_flash=sprite_sheet_asgore.get_image(5, 716, 159, 113, PINK)

textbubble = sprite_sheet_textbubble.get_image(99, 108, PINK2)

#soundefects
move = pygame.mixer.Sound("soundefects/snd_spearappear.wav")
trident = pygame.mixer.Sound("soundefects/blade.wav")

def intro():
    a=0
    b=False
    c=False
    d=False
    intro = True
    norepeat=False
    current_asgore_face=asgore_faces[0]
    asgore_face_pos=[260,3]
    asgore_intro_body_pos=[144,55]
    last_tick=0
    move_cooldown=30
    trident_appear_cooldown=50
    cooldown=750
    moveleft=0
    moveright=0
    e=False
    frame=0
    font="fonts/8bitoperator_jve.ttf"
    text_line1 = RPGtext.Text(intro_text_narator_line1[a], font, 30, -10,False, 0.35)
    text_line2 = RPGtext.Text("", font, 30, 0,False, 0.35)
    text_line3 = RPGtext.Text("", font, 15, 0,False, 0.35)
    text_line4 = RPGtext.Text("", font, 15, 0,False, 0.35)
    asgore_text_cur=0
    pygame.mixer.music.load('music/bergentruckung.wav')
    pygame.mixer.music.play(1)
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
    #pygame.time.set_timer(text_over,20000,1)
    centered=False
    while intro:
        #update background
        if e:
            screen.fill(WHITE)
        else:
            screen.fill(BLACK)

        #loading images
        #screen.blit(player_default, player_pos)
        current_tick=pygame.time.get_ticks()
        button_num=0
        for button in buttons:
            screen.blit(button, ((32+button_num*152),432))
            button_num+=1

        if c and moveleft==5 and current_tick-last_tick>=cooldown:
            d=True
            c=False
        if d:
            if norepeat==False:
                pygame.mixer.Sound.play(trident)
                norepeat=True
            screen.blit(asgore_intro_anim[frame], (24,15))
            if current_tick-last_tick>=trident_appear_cooldown and frame<13:
                frame+=1
                last_tick=current_tick
        elif e:
            screen.blit(asgore_flash, asgore_intro_body_pos)
        else:
            screen.blit(current_asgore_face, asgore_face_pos)
            screen.blit(asgore_intro_body, asgore_intro_body_pos)
        if c and current_tick-last_tick>=move_cooldown and moveleft<5:
            asgore_intro_body_pos[0]-=24
            asgore_face_pos[0]-=24
            last_tick=current_tick
            moveleft+=1
        if frame==13 and current_tick-last_tick>=cooldown and e==False:
            pygame.mixer.Sound.play(move)
            e=True
            d=False
            #20
        if e and current_tick-last_tick>=move_cooldown and moveright<20:
            asgore_intro_body_pos[0]+=15
            last_tick=current_tick
            moveright+=1
        
        if a==3:
            centered=True
            text_line1.render(screen,(320, 285),centered)
            text_line2.render(screen,(350, 315),centered)
        elif b:
            screen.blit(textbubble, (440,90))
            text_line1.render(screen,(460, 100),centered)
            text_line2.render(screen,(460, 120),centered)
            text_line3.render(screen,(460, 140),centered)
            text_line4.render(screen,(460, 160),centered)
        else:
            centered=False
            text_line1.render(screen,(30, 285),centered)
            text_line2.render(screen,(50, 315),centered)
        #event handler
        for event in pygame.event.get():
            if event.type == freeze:
                pygame.time.wait(2000)
            if event.type == pygame.QUIT:
                intro = False
            if event.type==next_text:
                a+=1
                print(a)
                text_line1 = RPGtext.Text(intro_text_narator_line1[a], font, 30, -10,False, 0.35)
                text_line2 = RPGtext.Text("", font, 30, 1,False, 0.35)
                if a==1:
                    pygame.time.set_timer(next_line,2400,1)
                else:
                    pygame.time.set_timer(next_line,2000,1)
            if event.type==next_line:
                text_line2 = RPGtext.Text(intro_text_narator_line2[a], font, 30, -10,False, 0.35)
            if event.type==asgore_text:
                print("Asgore text")
                b=True
                text_line1 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>Human...', font, 15, -8,False, 0.35)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_z and b:
                    asgore_text_cur+=1
                    if asgore_text_cur==1:
                        current_asgore_face=asgore_faces[1]
                        text_line1 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>It was', font, 15, -8,False, 0.35)
                        pygame.time.set_timer(asgore_next_line,500,1)
                    elif asgore_text_cur==2:
                        text_line2 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        text_line3 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        text_line4 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        current_asgore_face=asgore_faces[0]
                        text_line1 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>Goodbye.', font, 15, -8,False, 0.35)
                    else:
                        text_line1 = RPGtext.Text("", font, 15, -8,False, 0.35)
                        current_asgore_face=asgore_faces[2]
                        last_tick=pygame.time.get_ticks()
                        b=False
                        c=True
                        pygame.mixer.Sound.play(move)
            if event.type==asgore_next_line:
                text_line2 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>nice to', font, 15, -8,False, 0.35)
                pygame.time.set_timer(asgore_next_line1,500,1)
                #text.render(screen,(30, 300),False)
            if event.type==asgore_next_line1:
                text_line3 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>meet', font, 15, -8,False, 0.35)
                pygame.time.set_timer(asgore_next_line2,500,1)
            if event.type==asgore_next_line2:
                text_line4 = RPGtext.Text(r'<"font": {"color": [0, 0, 0]}>you.', font, 15, -8,False, 0.35)
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
intro()
pygame.quit()