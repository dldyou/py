from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False
toggle_run = False
run_t1 = 0
run_t2 = 0

player = FirstPersonController()
player.speed *= 1.5
player.jump_duration = 0.3
player.air_time = 0.5
player.jump_height = 1
player.original_speed = player.speed
player.gravity = 0.5
Sky(texture='/assets/sky')
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.95, 1.0)),
            highlight_color = color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=(self.position + mouse.normal))
            if key == 'right mouse down':
                destroy(self)
    
for z in range(10):
    for x in range(10):
        voxel = Voxel(position=(x, 0, z))

def input(key):
    global run_t1, run_t2
    if key == 'shift':
        player.speed = player.original_speed * 1.5
    elif key == 'shift up':
        player.speed = player.original_speed
        

def update(): 
    global run_t1, run_t2
    if player.y < -50:
        player.position = (0, 0, 0)
        
app.run()