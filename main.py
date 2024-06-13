import numpy as np
import moderngl_window as mglw


class Example(mglw.WindowConfig):
    gl_version = (4, 1)
    title = "ModernGL Example"
    window_size = (1920, 1080)
    aspect_ratio = 16 / 9
    resizable = True
    fullscreen = False


class SimpleColorTriangle(Example):
    gl_version = (3, 3)
    aspect_ratio = 16 / 9
    title = "Simple Color Triangle"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open("./shaders/vert.glsl", "r") as f:
            vertex_shader = f.read()

        with open("./shaders/frag.glsl", "r") as f:
            fragment_shader = f.read()

        self.prog = self.ctx.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader,
        )

        # Point coordinates are put followed by the vec3 color values
        vertices = np.array(
            [
                # x, y, red, green, blue
                0.0,
                0.8,
                1.0,
                0.0,
                0.0,
                -0.6,
                -0.8,
                0.0,
                1.0,
                0.0,
                0.6,
                -0.8,
                0.0,
                0.0,
                1.0,
            ],
            dtype="f4",
        )

        self.vbo = self.ctx.buffer(vertices)

        # We control the 'in_vert' and `in_color' variables
        self.vao = self.ctx.vertex_array(
            self.prog,
            [
                # Map in_vert to the first 2 floats
                # Map in_color to the next 3 floats
                self.vbo.bind("in_vert", "in_color", layout="2f 3f"),
            ],
        )

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.0, 0.0, 0.0)
        self.vao.render()
    def on_mouse_position_event(self, x, y, dx, dy):
        self.mouse_position_event(x, y, dx, dy)

    def on_mouse_drag_event(self, x, y, dx, dy):
        self.mouse_drag_event(x, y, dx, dy)

    def on_mouse_scroll_event(self, x_offset, y_offset):
        self.mouse_scroll_event(x_offset, y_offset)

    def on_mouse_press_event(self, x, y, button):
        self.mouse_press_event(x, y, button)

    def on_mouse_release_event(self, x, y, button):
        self.mouse_release_event(x, y, button)

    #defining mouse

    def mouse_position_event(self, x, y, dx, dy):
        print("Mouse position:", x, y, dx, dy)

    def mouse_drag_event(self, x, y, dx, dy):
        print("Mouse drag:", x, y, dx, dy)

    def mouse_scroll_event(self, x_offset: float, y_offset: float):
        print("Mouse wheel:", x_offset, y_offset)

    def mouse_press_event(self, x, y, button):
        print("Mouse button {} pressed at {}, {}".format(button, x, y))

    def mouse_release_event(self, x: int, y: int, button: int):
        print("Mouse button {} released at {}, {}".format(button, x, y))

if __name__ == "__main__":
    SimpleColorTriangle.run()
