controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(mySprite, 55, 55)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile4`, function (sprite, location) {
    game.setDialogTextColor(1)
    game.gameOver(true)
    game.setGameOverMessage(true, "You Escaped....... For now")
})
controller.A.onEvent(ControllerButtonEvent.Released, function () {
    controller.moveSprite(mySprite, 37, 37)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    game.gameOver(false)
})
let mySprite: Sprite = null
game.splash("Wonderer In A Maze Of Death: No Way Is Safe")
game.splash("Controlls: Q= A = Sprint WASD = Move")
game.splash("You: Whats Going On. How Did I Get Here")
game.splash("Thing: M     U     R     D     E     R           Y     O     U     !")
game.splash("You: What is that thing? I need to get out of here as soon as posible")
game.splash("Goal: Get Out As Fast As Posible(Or as slow as posible. the slower you go the more points you get) Have Fun -Justin")
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 37, 37)
let eneimy = sprites.create(img`
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
    `, SpriteKind.Enemy)
tiles.setCurrentTilemap(tilemap`Map1`)
tiles.placeOnRandomTile(mySprite, assets.tile`Door0`)
tiles.placeOnRandomTile(eneimy, assets.tile`myTile22`)
eneimy.follow(mySprite, 37)
scene.cameraFollowSprite(mySprite)
game.onUpdateInterval(1000, function () {
    info.changeScoreBy(1)
})
