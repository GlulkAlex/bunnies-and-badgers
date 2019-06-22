#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# 0 loop_fix branch

from __future__ import print_function
# 1 - Import library
import pygame
from pygame.locals import *
import math
import random
from collections import namedtuple
 
 
Game_Options = namedtuple(
    'Game_Options', 
    [ 'difficulty', 'num_arrows', 'healthvalue', 'enemy_Speed' ] )
# User can be presented 
# with three options: 
# easy, medium, and hard at start. 
# Parameters like 
# time, arrow count, etc. 
# can be set 
# according to the difficulty selected. 
def set_difficulty(
    # mandatory ? positional ?
    selected,
    # optional default
    config_options = {
        'difficulty': {
            'easy': { 'num_arrows': 300, 'healthvalue': 400, 'enemy_Speed': 1 }, 
            # default
            'medium': { 'num_arrows': 100, 'healthvalue': 194, 'enemy_Speed': 7 }, 
            'hard': { 'num_arrows': 50, 'healthvalue': 94, 'enemy_Speed': 10 }
        },
        # On / Off
        'is_Sound_Enabled': False,
    },
    *pos_args, **key_args
):
    """ helper
    """ 
    #if key_args is not None:
        
        #options = key_args#() = vars#locals#globals
        #print "Game difficulty was {}".format( options.get( 'difficulty' ) )
        #print "Setting game difficulty to {}".format( selected )
        #options['difficulty'] = selected
        
        #for key, value in config_options['difficulty'][selected].items():
            #print "setting {} to {}".format( key, value )
            #options[key] = value
    
    #>return Game_Options( selected, **config_options['difficulty'][selected] )#?, key_args
    return ( lambda difficulty, num_arrows, healthvalue, enemy_Speed, **rest: ( 
        difficulty, num_arrows, healthvalue, enemy_Speed, rest ) 
    )(
        difficulty = selected, 
        **config_options['difficulty'][selected] )
    
### @toDo: Add start game choose difficulty screen
def show_difficulty_options( 
    width, height, screen,
    difficulty = {
        'easy': { 'num_arrows': 300, 'healthvalue': 400, 'enemy_Speed': 1 }, 
        # default
        'medium': { 'num_arrows': 100, 'healthvalue': 194, 'enemy_Speed': 7 }, 
        'hard': { 'num_arrows': 50, 'healthvalue': 94, 'enemy_Speed': 10 }
    }
):
    """ helper

    returns:
    --------
    ( 
        difficulty: enum[ str ],
        num_arrows: int, healthvalue: int, enemy_Speed: int,
        is_Sound_Enabled: bool
    )
    """
    # pygame.display.set_caption()
    # Set the current window caption
    # set_caption(title, icontitle=None) -> None
    # If the display has a window title, 
    # this function will change the name on the window. 
    # Some systems support an alternate shorter title 
    # to be used for minimized displays.
    scale_Factor = 0.8
    screen_Center_X = width // 2
    screen_Center_Y = height // 2
    selected_Difficulty = 'medium'
    option_Box_Width = 200
    option_Box_Height = 40
    y_OffSet = option_Box_Height + 10#?height // 10
    
    #?pygame.font.init()
    font_24 = pygame.font.Font( None, 24 )
    font_32 = pygame.font.Font( None, 32 )
    
    pygame.display.set_caption("choose game options screen")
    pygame.mouse.set_cursor( 
        *pygame.cursors.tri_left#>diamond#>arrow 
    )
    
    # Color(name) -> Color
    # Color(r, g, b, a) -> Color
    # Color(rgbvalue) -> Color
    # 'rgbvalue' can be either 
    # a color name, 
    # an HTML color format string, 
    # a hex number string, 
    # or an integer pixel value.

    # Rect(left, top, width, height) -> Rect
    # Rect((left, top), (width, height)) -> Rect
    # Rect(object) -> Rect
    # pygame.Rect.contains	—	test if one rectangle is inside another
    # pygame.Rect.collidepoint	—	test if a point is inside a rectangle

    # rect(Surface, color, Rect, width=0) -> Rect
    # The width argument is the thickness to draw the outer edge. 
    # If width is zero then the rectangle will be filled.
    # fill Surface with a solid color
    # or use:
    # Surface.fill(color, rect=None, special_flags=0) -> Rect
    # Fill the Surface with a solid color. 
    # If no rect argument is given 
    # the entire Surface will be filled. 
    # The rect argument will limit the fill to a specific area. 
    # The fill will also be contained by the Surface clip area.
    #options_Box = pygame.draw.rect(
        #screen, 
        #( 0, 255, 255 ), 
        #( ( textx - 5, texty - 5 ), ( textx_size + 10, texty_size + 10 ) ) )
    
    options_Box = Rect( 
        #left = 
        #width // 10, 
        #50,
        0,
        #top = 
        #height // 10, 
        #40,
        0,
        #width = 
        int( width * scale_Factor ), 
        #400,
        #height = 
        int( height * scale_Factor ) 
        #300
    )
    options_Box.center = ( screen_Center_X, screen_Center_Y )
    screen.fill( 
        color = Color("red"), 
        # TypeError: Argument must be rect style object
        rect = options_Box )
    
    #for option in ( 'easy', 'medium', 'hard' ):
    #    pass
    
    # Rect.copy()
    # copy the rectangle
    # copy() -> Rect
    # Returns a new rectangle 
    # having the same position and size as the original.
    # Rect.move()
    # moves the rectangle
    # move(x, y) -> Rect
    # Returns a new rectangle 
    # that is moved by the given offset. 
    # The x and y arguments can be any integer value, positive or negative.
    option_Box = Rect( 
        #left = 
        #?width // 20, 
        0,
        #top = 
        #?height // 20, 
        0,
        #width = 
        #?int( width * 0.1 ), 
        option_Box_Width,
        #height = 
        #?int( height * 0.1 ) 
        option_Box_Height
    )
    
    option_Box_1 = option_Box.move( 0, options_Box.top + y_OffSet )
    option_Box_1.centerx = screen_Center_X
    option_Box_1 = screen.fill( 
        color = Color("green"), 
        rect = option_Box_1 )
    
    #option_Box_1.left: 32
    #print "option_Box_1.left:", option_Box_1.left
    #option_Box_1.bottomleft: (32, 72)
    #print "option_Box_1.bottomleft:", option_Box_1.bottomleft
    option_Box_2 = option_Box_1.move( 0, y_OffSet )
    #?option_Box_2 = 
    screen.fill( color = Color("green"), rect = option_Box_2 )
    option_Box_3 = option_Box_2.move( 0, y_OffSet )
    #?option_Box_3 = 
    screen.fill( color = Color("green"), rect = option_Box_3 )
    # TypeError: rect() takes no keyword arguments
    #>option_Box_3 = pygame.draw.rect( screen, Color("green"), option_Box_3, 10 )
    #?
    selection_Border = pygame.draw.rect( 
        screen, Color("gray"), option_Box_2, 10 
    )#.clamp( option_Box_2 )#.clip( option_Box_2 )
    #>selection_Border = option_Box_2.copy()
    selection_Border_Buffer = Rect( 
        selection_Border.left - 5, selection_Border.top - 5, 
        selection_Border.width + 10, selection_Border.height + 10
    )
    
    ### @Done?: Somehow remove | paint over extended border buffer 
    def mark_Option( 
        option_Box, 
        selection_Border = selection_Border,
        selection_Border_Buffer = selection_Border_Buffer,
        border_Width = 10
    ):
        """ helper """
        old_Border = selection_Border.copy()
        selection_Border_Buffer.center = old_Border.center
        #?
        pygame.draw.rect( screen, Color("red"), old_Border, border_Width )
        pygame.display.update( selection_Border_Buffer )
        #?pygame.draw.rect( screen, Color("red"), selection_Border_Buffer, 5 )
        pygame.draw.rect( screen, Color("green"), old_Border, border_Width )
        selection_Border.center = option_Box.center 
        selection_Border_Buffer.center = option_Box.center
        pygame.draw.rect( screen, Color("gray"), selection_Border, border_Width )
        # return 
        #pygame.display.update( old_Border )
        #pygame.display.update( option_Box )
        pygame.display.update( selection_Border_Buffer )
    
    mark_Option( option_Box_2 )
    
    rendered_text = font_32.render(
        "Select game difficulty level and audio option:", 
        True, Color("black"), Color( "white" )
    )
    text_box = rendered_text.get_rect()
    text_box.center = ( options_Box.center[0], options_Box.top + text_box.height )
    screen.blit( rendered_text, text_box )#options_Box )
    
    rendered_text = font_24.render(
        "easy", 
        True, Color("yellow"), Color( "black" )
    )
    text_box = rendered_text.get_rect()
    text_box.center = option_Box_1.center
    screen.blit( 
        rendered_text, 
        #option_Box_1 
        text_box
    )
    rendered_text = font_24.render(
        "medium", 
        True, Color("blue"), Color( "magenta" )
    )
    text_box = rendered_text.get_rect()
    text_box.center = option_Box_2.center
    screen.blit( 
        rendered_text, 
        #rendered_text.get_rect().clamp( option_Box_2 ) 
        #?option_Box_2.clamp( rendered_text.get_rect() )
        #option_Box_2.center# = (20,30)
        text_box
    )
    rendered_text = font_24.render(
        "hard", 
        True, Color("red"), Color( "yellow" )
    )
    text_box = rendered_text.get_rect()
    text_box.center = option_Box_3.center
    screen.blit( 
        rendered_text, 
        #option_Box_3 
        text_box
    )
    # (0,0,255) for blue
    # render(text, antialias, color, background=None) -> Surface
    rendered_text = font_24.render(
        "Audio options:", 
        True, Color("blue"), Color( "yellow" )
    )
    text_box = rendered_text.get_rect()
    #text_box.topright = [ width // 2, height * 0.5 ]
    text_box.topleft = ( option_Box_3.left, option_Box_3.bottom + 10 )
    
    #?screen.fill(0)
    
    # Surface.blit()
    # draw one image onto another
    # Surface.blit(source, dest, area=None, special_flags = 0) -> Rect
    # Draws a source Surface onto this Surface. 
    # The draw can be positioned with the `dest` argument. 
    # `Dest` can either be 
    # pair of coordinates representing the upper left corner of the `source`. 
    # A Rect can also be passed 
    # as the destination 
    # and the topleft corner of the rectangle 
    # will be used 
    # as the position for the blit. 
    # The size of the destination rectangle does not effect the blit.
    # An optional `area` rectangle can be passed as well. 
    # This represents 
    # a smaller portion of the source Surface to draw.
    screen.blit( 
        rendered_text, 
        #( option_Box_3.left, option_Box_3.bottom + 10 ) 
        text_box 
    )
    
    # type: bool
    is_Sound_Enabled = False
    is_Sound_Enabled_Box = Rect( 0, 0, option_Box_Height, option_Box_Height )
    #?is_Sound_Enabled_Box = option_Box_2.move( text_box.left, ... )
    #is_Sound_Enabled_Box.topleft = ( text_box.left, text_box.bottom + 10 )
    is_Sound_Enabled_Box.topleft = ( text_box.right + 20, text_box.top )
    #is_Sound_Enabled_Box = 
    screen.fill( color = Color("blue"), rect = is_Sound_Enabled_Box )
    
    def toggle_Sound( font_24, is_Sound_Enabled, is_Sound_Enabled_Box ):
        """ helper """
        rendered_text = font_24.render(
            "On" if is_Sound_Enabled else "Off",#'X',#'V',#"✔", 
            True, Color("black"), Color( "yellow" )
        )
        text_box = rendered_text.get_rect()
        #text_box_1.left = text_box.right + 20
        #text_box_1.top = text_box.top
        text_box.center = is_Sound_Enabled_Box.center
        screen.blit( rendered_text, text_box )
        # return
        # pygame.display.update(a rectangle or some list of rectangles)
        # This updates just the rectangular areas of the screen you specify.
        pygame.display.update( text_box )
        #?return not is_Sound_Enabled
    
    
    toggle_Sound( font_24, is_Sound_Enabled, is_Sound_Enabled_Box )
    
    exit_Button_Box = option_Box_1.inflate( -option_Box_Width // 2, 0 )#.move( -option_Box_Width // 2, 4 * y_OffSet )
    exit_Button_Box.topleft = ( text_box.left, text_box.top + y_OffSet  )
    screen.fill( color = Color("white"), rect = exit_Button_Box )
    rendered_text = font_24.render(
        "Exit", 
        True, Color("white"), Color( "black" )
    )
    text_box = rendered_text.get_rect()
    text_box.center = exit_Button_Box.center
    screen.blit( rendered_text, text_box )
    
    start_Button_Box = exit_Button_Box.copy()#move( y_OffSet, 0 )
    #?start_Button_Box.topright = ( option_Box_3.right, start_Button_Box.bottom )
    start_Button_Box.right = option_Box_3.right
    screen.fill( color = Color("green"), rect = start_Button_Box )
    rendered_text = font_24.render(
        "Start", 
        True, Color("white"), Color( "black" )
    )
    text_box = rendered_text.get_rect()
    text_box.center = start_Button_Box.center
    screen.blit( rendered_text, text_box )
    
    # return
    #pygame.display.update( text_box )
    #
    pygame.display.update( options_Box )
    #>pygame.display.flip()
    #pygame.time.delay(1500)
    
    collect_Config = ( 
        lambda difficulty, num_arrows, healthvalue, enemy_Speed, is_Sound_Enabled, **rest: ( 
        difficulty, num_arrows, healthvalue, enemy_Speed, is_Sound_Enabled, rest ) 
    )
    # handle user's input
    is_While_Condition = True
    while is_While_Condition:
        #pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif( 
                event.type == pygame.MOUSEBUTTONDOWN 
                # left mouse button pressed 
                and event.button == 1
            ):
                x, y = event.pos
                
                if exit_Button_Box.collidepoint( x, y ):
                    pygame.quit()
                    exit(0)
                
                if start_Button_Box.collidepoint( x, y ):
                    # selected_Difficulty
                    return collect_Config( 
                        difficulty = selected_Difficulty,
                        is_Sound_Enabled = is_Sound_Enabled,
                        **difficulty[ selected_Difficulty ]
                    )
                    
                if is_Sound_Enabled_Box.collidepoint( x, y ):
                    ### @toDo: do flip / switch inside function ?
                    is_Sound_Enabled = not is_Sound_Enabled
                    toggle_Sound( font_24, is_Sound_Enabled, is_Sound_Enabled_Box )
                
                # selected option detection
                # by x, y boundaries box / rectangle
                # Rect.collidepoint()
                # test if a point is inside a rectangle
                # collidepoint(x, y) -> bool
                # collidepoint((x,y)) -> bool
                # Returns true 
                # if the given point is inside the rectangle. 
                # Note: A point along the right or bottom edge 
                # is not considered to be inside the rectangle.
                if option_Box_1.collidepoint( x, y ):
                    #selected = 'easy'
                    #?set_difficulty( selected )
                    # ? is_Sound_Enabled
                    selected_Difficulty = 'easy'
                    ### @toDo: toggle | make visible selection 
                    mark_Option( option_Box_1 )
                    #return 'easy'
                    #return collect_Config( 
                        #difficulty = 'easy',
                        #is_Sound_Enabled = is_Sound_Enabled,
                        #**difficulty[ 'easy' ]
                    #)
                
                if option_Box_2.collidepoint( x, y ):
                    
                    selected_Difficulty = 'medium'
                    mark_Option( option_Box_2 )
                    #return 'medium'
                    #return collect_Config( 
                        #difficulty = 'medium',
                        #is_Sound_Enabled = is_Sound_Enabled,
                        #**difficulty[ 'medium' ]
                    #)
                
                if option_Box_3.collidepoint( x, y ):
                    
                    selected_Difficulty = 'hard'
                    mark_Option( option_Box_3 )
                    #selected = 'easy'
                    #?set_difficulty( selected )
                    #return 'hard'
                    #return collect_Config( 
                        #difficulty = 'hard',
                        #is_Sound_Enabled = is_Sound_Enabled,
                        #**difficulty[ 'hard' ]
                    #)
                
                #is_While_Condition = False
                #break
            
                # exit detected
                #if x >= text2x - 5 and x <= text2x + text2x_size + 5:
                    #if y >= text2y - 5 and y <= text2y + text2y_size + 5:
                        #pygame.quit()
                        #exit(0)
                #return 'medium'

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode( ( width, height ) )
pygame.mixer.init()
 
# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg=badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.set_volume(0.25)

 
# 4 - keep looping through
def main():
    keys = [ False, False, False, False ]
    
    difficulty = "medium"
    
    playerpos = [
        100, height // 2#100
    ]
    # shoots vs. hits
    acc = [ 0, 0 ]
    arrows = []
    # controls enemy spawn speed / frequency 
    badtimer = 100
    badtimer1 = 0
    badguys = [ [ width, 100 ] ]
    healthvalue = 194
    timestart = pygame.time.get_ticks()
    
    is_Sound_Enabled = False
    num_arrows = 100
    
    arrow_Height = 32
    arrow_Width = 26
    # towers spawn positions
    #castles_Ys = ( 30, 135, 240, 345 )
    castles_Ys = range( 30, height - 30, 105 )
    player_Speed = 5
    enemy_Speed = 5#7
    
    (
        difficulty, num_arrows, healthvalue, enemy_Speed, is_Sound_Enabled, _
    ) = show_difficulty_options( width, height, screen )#set_difficulty( 
        #show_difficulty_options( width, height, screen ),
        #**{ 'num_arrows': num_arrows, 'healthvalue': healthvalue, 'enemy_Speed': enemy_Speed }
    #)
    print( "Game difficulty is {}, is_Sound_Enabled: {}".format( difficulty, is_Sound_Enabled ) )
    if is_Sound_Enabled: pygame.mixer.music.play( -1, 0.0 );
    
    #def draw_Health_Bar
    class Health_Bar(  ):
        """ Custom component
        to draw and handle health changes
        ### it must show red background while | as green healthbar shrinks 
        ### overtime by taking damage 
        """
        def __init__( 
            self, 
            #scr, 
            max_Value = 100, 
            max_Width = 100,
            bar_Left_X = 5,
            bar_Top_Y = 5
        ):
            """
            ### @toDo: add position to place | draw on screen | parent container 
            """
            # screen
            #self.scr = scr
            self.max_Health = max_Value
            self.health_Left = max_Value
            self.max_Width = max_Width
            # HP: 100 -> bar: 200 => 1 HP -> 2 bar pixels 
            # HP: 200 -> bar: 100 => 1 HP -> 0.5 bar pixels 
            self.width_2_Health_Ratio = max_Width / max_Value
            self.bar_Left_X = bar_Left_X
            self.bar_Top_Y = bar_Top_Y
            self.background_Border_Box = Rect( 
                bar_Left_X,
                bar_Top_Y,
                max_Width + 4,
                16
            )
            self.damage_Box = Rect( 
                0,
                0,
                # initially it has to | might be invisible or "under" health_Box
                max_Width,
                10
            )
            self.damage_Box.center = self.background_Border_Box.center
            self.health_Box = Rect( 
                0,
                #?self.damage_Box.left,
                0,
                #?self.damage_Box.top,
                max_Width,
                8
            )
            self.health_Box.center = self.background_Border_Box.center
        
        def draw( 
            self, 
            screen = screen,
            display = pygame.display
        ):
            screen.fill( color = Color("black"), rect = self.background_Border_Box )
            #?
            screen.fill( color = Color("red"), rect = self.damage_Box )
            screen.fill( color = Color("green"), rect = self.health_Box )
            display.update( self.background_Border_Box )
    
        def take_Hit( 
            self, 
            damage,
            screen = screen,
            display = pygame.display
        ):
            """shrink health_Box to the left ( from the right )"""
            self.health_Left = max( 0, self.health_Left - damage )
            # translate damage to its view
            damage_Size = int( self.width_2_Health_Ratio * damage )
            health_Size = int( self.width_2_Health_Ratio * self.health_Left )
            
            if self.health_Left > 0 and damage_Size > 0:
                
                #self.damage_Box.width = self.damage_Box.width + damage_Size
                #self.damage_Box.right = self.health_Box.right
                #screen.fill( color = Color("red"), rect = self.damage_Box )
                
                #?self.health_Box.right = self.health_Box.left + self.health_Left
                self.health_Box.width = health_Size
                screen.fill( color = Color("green"), rect = self.health_Box )
                display.update( self.background_Border_Box )
    
    
    health_Bar = Health_Bar( 
        max_Value = healthvalue, 
        max_Width = 200, 
        bar_Top_Y = 25 
    )
    
    running = 1
    exitcode = 0
    while running:
        badtimer -= 1
        # 5 - clear the screen before drawing it again
        screen.fill(0)
        # 6 - draw the screen elements
        for x in range( width / grass.get_width() + 1 ):
            for y in range( height / grass.get_height() + 1 ):
                ### @toDo: replace magic number 100 with named constant
                screen.blit( grass, ( x * 100, y * 100 ) )
        
        for y in castles_Ys:
            screen.blit( castle, ( 0, y ) )
        
        # 6.1 - Set player position and rotation
        position = pygame.mouse.get_pos()
        angle = math.atan2(
            position[1] - ( playerpos[1] + arrow_Height ),
            position[0] - ( playerpos[0] + arrow_Width ) )
        ### @toDo: replace magic numbers 360 and 57.29 with named constants
        playerrot = pygame.transform.rotate( player, 360 - angle * 57.29 )
        playerpos1 = (
            playerpos[0] - playerrot.get_rect().width / 2, 
            playerpos[1] - playerrot.get_rect().height / 2 )
        screen.blit( playerrot, playerpos1 )
        # 6.2 - Draw arrows
        for bullet in list(arrows):
            ### @toDo: replace magic number 10 with named constant
            velx = math.cos( bullet[0] ) * 10
            vely = math.sin( bullet[0] ) * 10
            bullet[1] += velx
            bullet[2] += vely
            ### @toDo: replace magic number +/-64 with named constant
            if( 
                bullet[1]    < -64 
                or bullet[1] > width 
                or bullet[2] < -64 
                or bullet[2] > height
            ):
                arrows.remove(bullet)
                if num_arrows <= 0:
                    running = 0
        for projectile in arrows:
            arrow1 = pygame.transform.rotate( arrow, 360 - projectile[0] * 57.29 )
            screen.blit( arrow1, ( projectile[1], projectile[2] ) )
        ### @toDo: find out ( refactor ) 
        ### how often ( waves of ) badguys will be spawn 
        ### and adjust those Parameters to alter difficulty level 
        # 6.3 - Draw badgers
        if badtimer == 0:
            badguys.append( [ width, random.randint( 50, 430 ) ] )
            badtimer = 100 - ( badtimer1 * 2 )
            ### @toDo: replace magic number 35 with named constant
            if badtimer1 >= 35:
                badtimer1 = 35
            else:
                badtimer1 += 5
        for badguy in list( badguys ):
            if badguy[0] < -64:
                badguys.remove( badguy )
                continue
            badguy[0] -= enemy_Speed#7
            # 6.3.1 - Attack castle
            badrect = pygame.Rect( badguyimg.get_rect() )
            badrect.top = badguy[1]
            badrect.left = badguy[0]
            # collision detection
            if badrect.left < 64:
                if is_Sound_Enabled: hit.play();
                # compute damage
                damage = random.randint( 5, 20 )
                healthvalue -= damage
                
                health_Bar.take_Hit( damage = damage )
                
                badguys.remove( badguy )
            
            # 6.3.2 - Check for collisions
            for bullet in list( arrows ):
                bullrect = pygame.Rect( arrow.get_rect() )
                bullrect.left = bullet[1]
                bullrect.top = bullet[2]
                if badrect.colliderect( bullrect ):
                    if is_Sound_Enabled: enemy.play();
                    # hit count incremented
                    acc[0] += 1
                    ### @toDo: @FixIt
                    # ValueError: list.remove(x): x not in list
                    badguys.remove( badguy )
                    arrows.remove( bullet )
        
        # 6.3.3 - Next bad guy
        for badguy in badguys:
            screen.blit( badguyimg, badguy )
        
        # 6.4 - Draw clock
        font = pygame.font.Font( None, 24 )
        ### @toDo: replace magic number 90000 with named constant
        time_remaining = 90000 - ( pygame.time.get_ticks() - timestart )
        survivedtext = font.render(
            str( time_remaining / 60000 ) + ":" + 
            str( time_remaining / 1000 % 60 ).zfill(2), 
            True, ( 0, 0, 0 )
        )
        textRect = survivedtext.get_rect()
        textRect.topright=[ width - 5, 5 ]
        screen.blit( survivedtext, textRect )
        arrowstext = font.render(
            "Remaining arrows: " + str( num_arrows ), True, ( 0, 0, 0 ) )
        arrowsTextRect = arrowstext.get_rect()
        arrowsTextRect.topright = [ width - 5, 20]
        screen.blit( arrowstext, arrowsTextRect )
        
        # 6.5 - Draw health bar
        ### @toDo: adjust health bar width or damage size to healthvalue
        ### or replace them alltogether with painted rectangels inside board
        ### or use 
        ### # $ pip3 install tqdm
        ### from tqdm import tqdm
        ### for Progress Bar
        screen.blit( healthbar, ( 5, 5 ) )
        for health_bit in range( 0, healthvalue, 1 ):
            screen.blit( health, ( health_bit + 8, 8 ) )
        
        health_Bar.draw()
        #health_Bar.take_Hit( damage = healthvalue // 2 )
        
        # 7 - update the screen
        pygame.display.flip()
        
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button 
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit() 
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    keys[0] = True
                elif event.key == K_a:
                    keys[1] = True
                elif event.key == K_s:
                    keys[2] = True
                elif event.key == K_d:
                    keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys[0] = False
                elif event.key==pygame.K_a:
                    keys[1] = False
                elif event.key == pygame.K_s:
                    keys[2] = False
                elif event.key == pygame.K_d:
                    keys[3] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_Sound_Enabled: shoot.play();
                position = pygame.mouse.get_pos()
                # shoots count incremented 
                acc[1] += 1
                arrows.append(
                    [
                        math.atan2(
                            position[1] - ( playerpos1[1] + arrow_Height ),
                            position[0] - ( playerpos1[0] + arrow_Width ) ),
                        playerpos1[0] + arrow_Height,
                        playerpos1[1] + arrow_Height ] )
                num_arrows -= 1
        # 9 - Move player
        if keys[0]:
            playerpos[1] -= player_Speed#5
        elif keys[2]:
            playerpos[1] += player_Speed#5
        if keys[1]:
            playerpos[0] -= player_Speed#5
        elif keys[3]:
            playerpos[0] += player_Speed#5
        #10 - Win/Lose check
        timenow = pygame.time.get_ticks()
        if timenow - timestart >= 90000:
            # times up
            running = 0
            exitcode = 1
        if healthvalue <= 0:
            # nothing to protect
            running = 0
            exitcode = 0
        if acc[1] != 0:
            accuracy = round( acc[0] * 1.0 / acc[1] *100, 2 )
        else:
            # ?!?
            accuracy = 0
    # 11 - Win/lose display
    pygame.font.init()
    ### @toDo: not DRY
    font = pygame.font.Font( None, 24 )
    elapsedtime = pygame.time.get_ticks() - timestart / 1000

    game_over_message = ""
    if num_arrows <= 0:
        game_over_message = "You have run out of arrows!!! "
    ### @toDo: it can be replaced with string format
    game_over_message += (
        "Score: " + str( accuracy ) +
        "% (Accuracy) * " + str( elapsedtime / 1000 )+
        " (Time) = " + str( int( accuracy * elapsedtime / 1000 ) ) )
    text = font.render( game_over_message, True, ( 0, 255, 0 ) )

    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    if exitcode == 0:
        screen.blit( gameover, ( 0, 0 ))
    else:
        screen.blit( youwin, ( 0, 0 ) )
    screen.blit( text, textRect )
    pygame.display.flip()
    pygame.mixer.music.fadeout( 1500 )
    pygame.time.delay( 1500 )

    # draw replay/exit buttons
    global textx, texty, textx_size, texty_size
    global text2x, text2y, text2x_size, text2y_size
    
    bigfont = pygame.font.Font( None, 80 )
    text = bigfont.render('Play Again', 13, ( 0, 255, 0 ) )
    textx = width / 2 - text.get_width() / 2
    texty = height / 4 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(
        screen, 
        ( 0, 255, 255 ), 
        ( ( textx - 5, texty - 5 ), ( textx_size + 10, texty_size + 10 ) ) )

    screen.blit( 
        text, 
        ( width / 2 - text.get_width() / 2, height / 4 - text.get_height() / 2 ) )
    text2 = bigfont.render('Exit', 13, ( 255, 0, 0 ) )
    text2x = width / 2 - text2.get_width() / 2
    text2y = height * 3 / 4 - text2.get_height() / 2
    text2x_size = text2.get_width()
    text2y_size = text2.get_height()
    pygame.draw.rect(
        screen, 
        ( 0, 255, 255 ), 
        ( ( text2x - 5, text2y - 5 ), ( text2x_size + 10, text2y_size + 10 ) ) )

    screen.blit(
        text2, 
        ( width / 2 - text2.get_width() / 2, height * 3 / 4 - text2.get_height() / 2 ) )

    pygame.display.flip()

# play game
main()
# after game ends options screen 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if x >= textx - 5 and x <= textx + textx_size + 5:
                if y >= texty - 5 and y <= texty + texty_size + 5:
                    main()
                    break
            if x >= text2x - 5 and x <= text2x + text2x_size + 5:
                if y >= text2y - 5 and y <= text2y + text2y_size + 5:
                    pygame.quit()
                    exit(0)
