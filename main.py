def on_a_pressed():
    controller.move_sprite(mySprite, 55, 55)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    game.set_dialog_text_color(1)
    game.game_over(True)
    game.set_game_over_message(True, "You Escaped....... For now")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile)

def on_a_released():
    controller.move_sprite(mySprite, 37, 37)
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(sprite2)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

mySprite: Sprite = None
game.splash("Wonderer In A Maze Of Death: No Way Is Safe")
game.splash("Controlls: Q= A = Sprint WASD = Move")
game.splash("You: Whats Going On. How Did I Get Here")
game.splash("Thing: M     U     R     D     E     R           Y     O     U     !")
game.splash("You: What is that thing? I need to get out of here as soon as posible")
game.splash("Goal: Get Out As Fast As Posible(Or as slow as posible. the slower you go the more points you get) Have Fun -Justin")
mySprite = sprites.create(img("""
        . . . . . 7 7 7 7 7 7 7 7 7 7 .
            . . . . 7 7 2 7 7 2 7 7 7 2 7 7
            . . . 7 7 7 7 7 2 7 7 7 7 2 7 7
            . . . . d d d d d d d d d d d d
            . . . . d d f f d d 2 d f f d d
            . . . . d 2 f f d d d d f f d d
            . . . . d d d d d d d d d d d 2
            . . d 2 d d f f f f f f f f d d
            . d 2 d d f d d 2 d d d d d f d
            d 2 d . f d d d d 2 d d d d d f
            d d . . d d d 2 d d d d d 2 d d
            2 2 . . f f f f 5 f f 5 f f f f
            d d . . 8 8 8 8 8 8 8 8 8 8 8 8
            d d . . 2 2 8 f 8 2 2 8 8 f 8 8
            2 1 . . 8 2 8 8 8 8 2 2 8 2 2 8
            1 2 . . 8 2 . . . . . . . . 8 8
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 37, 37)
eneimy = sprites.create(img("""
        . . . . 7 7 7 7 7 . . . . . . .
            f . . . 7 7 7 7 7 7 7 7 . . . f
            . f . . 2 5 5 5 2 2 2 5 2 . f .
            . . f . 5 2 2 5 5 5 2 5 . f . .
            . . 5 f 5 2 d 2 2 2 5 5 f 5 . .
            . 5 5 . f 5 2 2 d 2 5 f . 5 5 .
            2 2 . . 5 f 5 5 2 5 f 5 . . 2 2
            2 . . . 2 5 f 5 5 f 5 2 . . . 2
            . . . . 5 2 5 f f 5 2 2 . . . .
            . . . . 8 2 8 8 2 8 2 2 . . . .
            . . . . 8 2 2 8 8 2 8 2 . . . .
            . . . . 2 8 8 2 8 2 2 2 . . . .
            . . . . 8 . . . . . . 8 . . . .
            . . . 8 2 . . . . . . 2 8 . . .
            . . . 2 8 . . . . . . 8 2 . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
tiles.set_current_tilemap(tilemap("""
    Map1
"""))
tiles.place_on_random_tile(mySprite, assets.tile("""
    Door0
"""))
tiles.place_on_random_tile(eneimy, assets.tile("""
    myTile22
"""))
eneimy.follow(mySprite, 37)
scene.camera_follow_sprite(mySprite)
