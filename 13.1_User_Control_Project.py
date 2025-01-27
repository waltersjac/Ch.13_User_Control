'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Move through maze to get to the top right corner.

'''
import arcade

SW=500
SH=400
point_list=((100,90),(120,90),(120,200),(60,200),(60,340),(270,340),(270,400),(250,400),(250,360),(40,360)
            ,(40,240),(40,180),(60,180),(100,180))
point_list2=((450,0),(450,60),(430,60),(350,60),(350,360),(330,360),(330,280),(120,280),(120,260),(200,260),(200,140)
             ,(280,140),(280,160),(220,160),(220,260),(330,260),(330,40),(430,40),(430,0))

class player:
    def __init__(self,x,y,dx,dy,r,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.c=c
        self.laser_sound = arcade.load_sound("explosion.mp3")
    def draw_player(self):
        arcade.draw_triangle_filled(self.x,self.y,self.x-10,self.y-20,self.x+10,self.y-20,self.c)

    def update_player(self):
        self.x+= self.dx
        self.y+= self.dy


        if self.x < 10:
            self.dx = 0
            self.x = 10
            arcade.play_sound(self.laser_sound,5)
        elif self.x > SW:
            self.dx = 0
            self.x = SW-10
            arcade.play_sound(self.laser_sound,5)
        if self.y < 20:
            self.dy = 0
            self.y = 20
            arcade.play_sound(self.laser_sound,5)
        elif self.y > SH:
            self.dy = 0
            self.y = SH
            arcade.play_sound(self.laser_sound,5)

        if self.x>=430 and self.y>=380:
            print("You win")

        if self.x>=180 and self.x-10<=200 and self.y>=0 and self.y-20<=80:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        if self.x>=100 and self.x<=120 and self.y>=100 and self.y-20<=200:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=40 and self.x<=100 and self.y>=180 and self.y-20<=200:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=40 and self.x<=60 and self.y>=200 and self.y-20<=360:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=40 and self.x<=270 and self.y>=340 and self.y-20<=360:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=250 and self.x<=270 and self.y>=360 and self.y-20<=400:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        if self.x>=420 and self.x<=450 and self.y>=100 and self.y-20<=400:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        if self.x>=430 and self.x<=450 and self.y>=0 and self.y-20<=60:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=330 and self.x<=430 and self.y>=40 and self.y-20<=60:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=330 and self.x<=350 and self.y>=60 and self.y-20<=360:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=120 and self.x<=330 and self.y>=260 and self.y-20<=280:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=200 and self.x<=220 and self.y>=140 and self.y-20<=260:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)
        elif self.x>=200 and self.x<=280 and self.y>=140 and self.y-20<=260:
            self.x=20
            self.y=30
            arcade.play_sound(self.laser_sound, 5)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.player = player(20,30,0,0,15,arcade.color.ARMY_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.player.draw_player()
        arcade.draw_polygon_filled(point_list,arcade.color.BLACK)
        arcade.draw_rectangle_filled(430,250,20,300,arcade.color.BLACK)
        arcade.draw_polygon_filled(point_list2,arcade.color.BLACK)
        arcade.draw_rectangle_filled(190,40,20,80,arcade.color.BLACK)

    def on_update(self, dt):
        self.player.update_player()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.dx=-4
        elif key ==arcade.key.RIGHT:
            self.player.dx=4
        elif key == arcade.key.UP:
            self.player.dy=4
        elif key == arcade.key.DOWN:
            self.player.dy=-4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.dy = 0


def main():
    window = MyGame(SW, SH, "Mouse control")
    arcade.run()


if __name__ == "__main__":
    main()