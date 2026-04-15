import py5
import pandas as pd
import numpy as np

class SPHY_Parquet_Viewer:
    def __init__(self, path):
        print("Carregando inteligência de campo via Parquet...")
        self.df = pd.read_parquet(path)
        self.max_frames = self.df['frame_id'].max()
        self.current_frame = 0
        self.zoom = -1200
        self.rot_x, self.rot_y = 0.5, 0.5
        self.offset_x, self.offset_y = 0, 0

    def get_frame_data(self, frame_id):
        # Filtro rápido colunar do Parquet
        return self.df[self.df['frame_id'] == frame_id]

def settings():
    py5.size(1200, 900, py5.P3D)
    py5.smooth(8)

def setup():
    py5.window_title("HarpiaOS - SPHY Parquet Inspector")
    py5.color_mode(py5.HSB, 360, 255, 255, 255)
    global viewer
    path = "datasets/sphy_field_evolution.parquet"
    try:
        viewer = SPHY_Parquet_Viewer(path)
    except:
        print("Dataset não encontrado. Rode o gerador primeiro!")
        py5.exit_sketch()

def draw():
    py5.background(0)
    frame_data = viewer.get_frame_data(viewer.current_frame)
    
    py5.translate(py5.width/2 + viewer.offset_x, py5.height/2 + viewer.offset_y, viewer.zoom)
    py5.rotate_x(viewer.rot_x)
    py5.rotate_y(viewer.rot_y)
    py5.rotate_z(py5.frame_count * 0.005)

    for _, row in frame_data.iterrows():
        R, r, n = row['R'], row['r'], row['iteration']
        
        hue = py5.remap(n, 0, 8, 240, 320)
        py5.stroke(hue, 200, 255, 200)
        py5.no_fill()
        
        # Renderização SPHY
        res = 25 # Resolução de visualização
        for i in range(res):
            py5.begin_shape(py5.LINE_STRIP)
            theta = py5.remap(i, 0, res, 0, py5.TWO_PI)
            for j in range(res + 1):
                phi = py5.remap(j, 0, res, 0, py5.TWO_PI)
                x = (R + r * py5.cos(theta)) * py5.cos(phi)
                y = (R + r * py5.cos(theta)) * py5.sin(phi)
                z = r * py5.sin(theta)
                py5.vertex(x, y, z)
            py5.end_shape()

    viewer.current_frame = (viewer.current_frame + 1) % (viewer.max_frames + 1)
    draw_ui()

def draw_ui():
    py5.hint(py5.DISABLE_DEPTH_TEST)
    py5.reset_matrix()
    py5.fill(200, 255, 255)
    py5.text(f"MODO DATASET PARQUET | FRAME: {viewer.current_frame}", 25, 40)
    py5.hint(py5.ENABLE_DEPTH_TEST)

def mouse_dragged():
    if py5.mouse_button == py5.LEFT:
        viewer.offset_x += (py5.mouse_x - py5.pmouse_x)
        viewer.offset_y += (py5.mouse_y - py5.pmouse_y)
    elif py5.mouse_button == py5.RIGHT:
        viewer.rot_y += (py5.mouse_x - py5.pmouse_x) * 0.01
        viewer.rot_x -= (py5.mouse_y - py5.pmouse_y) * 0.01

def mouse_wheel(event):
    viewer.zoom += event.get_count() * 60

if __name__ == "__main__":
    py5.run_sketch()
