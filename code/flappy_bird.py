import raylib as rl
from pyray import *
from os.path import join
import random

init_audio_device()
init_window(1280,720,'Dino project')
set_target_fps(40)

jump_sound = load_sound(join('audio','jump.wav'))
music = load_music_stream(join('audio','music.mp3'))
play_music_stream(music)


## Defining 
start_pos = Vector2(0,640)
end_pos = Vector2(1280,640)
score = 0

x_pos = 50
y_pos = 580
y_vel = 0 
g = 10 
time_el = 0

x_pos_c0 = 1281
x_pos_c1 = 1366
x_pos_c2 = 1480
x_pos_c3 = 1955

x_pos_cloud = 1300
x_pos1_cloud = 1350

dino_texture = load_texture(join('assets','dino','run0.png'))
dino_texture1 = load_texture(join('assets','dino','run1.png'))

cacti_texture = load_texture(join('assets','cactii', 'cactus0.png'))
cacti_texture1 = load_texture(join('assets','cactii', 'cactus1.png'))
cacti_texture2 = load_texture(join('assets','cactii', 'cactus2.png'))
cacti_texture3 = load_texture(join('assets','cactii', 'cactus3.png'))

cloud1 = load_texture(join('assets','clouds', 'cloud1.png'))
cloud2 = load_texture(join('assets','clouds', 'cloud2.png'))

## Basic building and Logic
while not window_should_close():
    rl.BeginDrawing()
    update_music_stream(music)
    clear_background(RAYWHITE)
    draw_line_ex(start_pos,end_pos,10,BLACK)
    if(time_el//4 == 0):
        draw_texture_ex(dino_texture,Vector2(x_pos,y_pos),0,1.5,RED)
    else:
        draw_texture_ex(dino_texture1,Vector2(x_pos,y_pos),0,1.5,RED)

    ## CLOUD ##
    x_pos_cloud = x_pos_cloud - 4
    x_pos1_cloud = x_pos1_cloud - 4
            
    if(x_pos_cloud<=0):
         x_pos_cloud = 1300
    if(x_pos1_cloud<=0):
         x_pos1_cloud = 1350

    
    ## CACTUS LOGIC ##
    # if (0<= x_pos_c0 <= 1400):
    #     x_pos_c0 -= 7
    #     if x_pos_c0<0:
    #         x_pos_c0 = 1300

    # draw_texture_ex(cacti_texture, Vector2(x_pos_c0, 580), 0, 2, GREEN)

    # if (0<= x_pos_c1 <= 1400):
    #     x_pos_c1 -= 7
    #     if x_pos_c1<0:
    #         x_pos_c1 = 1340

    # draw_texture_ex(cacti_texture1, Vector2(x_pos_c1, 580), 0, 2, GREEN)

    # if (0<= x_pos_c2 <= 1400):
    #     x_pos_c2 -= 7
    #     if x_pos_c2<0:
    #         x_pos_c2 = 1360

    # draw_texture_ex(cacti_texture2, Vector2(x_pos_c2, 580), 0, 2, GREEN)

    # if (0<= x_pos_c3 <= 1400):
    #     x_pos_c3 -= 7
    #     if x_pos_c3<0:
    #         x_pos_c3 = 1380
    # draw_texture_ex(cacti_texture3, Vector2(x_pos_c3, 580), 0, 2, GREEN)


    # draw_texture_ex(cloud1,Vector2(x_pos_cloud,330),0,2,WHITE)
    # draw_texture_ex(cloud2,Vector2(x_pos1_cloud,300),0,3,BLACK)


## CACTUS LOGIC ##

# Move all cacti
    x_pos_c0 -= 7
    x_pos_c1 -= 7
    x_pos_c2 -= 7
    x_pos_c3 -= 7

    # Reset each cactus after it leaves the screen
    if x_pos_c0 < -50:
        x_pos_c0 = 1300

    if x_pos_c1 < -50:
        x_pos_c1 = x_pos_c0 + random.randint(250, 450)

    if x_pos_c2 < -50:
        x_pos_c2 = x_pos_c1 + random.randint(250, 450)

    if x_pos_c3 < -50:
        x_pos_c3 = x_pos_c2 + random.randint(250, 450)

    # Draw cacti
    draw_texture_ex(cacti_texture, Vector2(x_pos_c0, 580), 0, 2, GREEN)
    draw_texture_ex(cacti_texture1, Vector2(x_pos_c1, 580), 0, 2, GREEN)
    draw_texture_ex(cacti_texture2, Vector2(x_pos_c2, 580), 0, 2, GREEN)
    draw_texture_ex(cacti_texture3, Vector2(x_pos_c3, 580), 0, 2, GREEN)


    ##


    # draw_rectangle(50,int(y_pos),dino_texture.width,dino_texture.height,GRAY)
    # draw_rectangle(x_pos1_c,580,cacti_texture.width,cacti_texture.height,RED)
    # ##initial settings
    

    ##Jump Logic
    if (is_key_down(rl.KEY_SPACE) and y_pos>=580):
        y_pos = 578
        y_vel = 2*g 

    if(y_pos<580):
        y_vel-=(g/8)
        y_pos-=(y_vel)/3

    ## Collision logic
    collision1 = check_collision_recs(
        Rectangle(50,int(y_pos),dino_texture.width,dino_texture.height),
        Rectangle(x_pos_c1,580,cacti_texture.width,cacti_texture.height)
    )
    collision2 = check_collision_recs(
        Rectangle(50,int(y_pos),dino_texture.width,dino_texture.height),
        Rectangle(x_pos_c0,580,cacti_texture.width,cacti_texture.height)
    )
    collision3 = check_collision_recs(
            Rectangle(50,int(y_pos),dino_texture.width,dino_texture.height),
            Rectangle(x_pos_c2,580,cacti_texture.width,cacti_texture.height)
    )
    collision4 = check_collision_recs(
            Rectangle(50,int(y_pos),dino_texture.width,dino_texture.height),
            Rectangle(x_pos_c3,580,cacti_texture.width,cacti_texture.height)
    )
    
    if(score<0):
        close_window()

    if(collision1 or collision2 or collision3 or collision4):
        score-=10

    score+=1
    
    if(time_el>=20):
        time_el = 0
    else:
        time_el+=0.5

    ## Tp
    if(is_key_pressed(rl.KEY_A)):
        close_window()
        play_sound(jump_sound) 

    ##text
    draw_text(f"Score: {int(score/10)}", 35, 100, 40, BLACK)
    
    rl.EndDrawing()
