import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PySide6.QtWidgets import QWidget, QVBoxLayout

class Visualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255, 120)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 40
        layout.addWidget(self.w)

        for cfg in [
            ("x", 90, 0, 1, 0, -10, 0, 0),
            ("y", 90, 1, 0, 0, 0, -10, 0),
            ("z", 0, 0, 0, 0, 0, 0, -10),
        ]:
            name, ang, ax, ay, az, tx, ty, tz = cfg
            grid = gl.GLGridItem()
            grid.rotate(ang, ax, ay, az)
            grid.translate(tx, ty, tz)
            self.w.addItem(grid)

        self.line = None

    def update_plot(self, v, theta_deg, azimuth_deg, g, t_range, x0, y0, z0):
        theta = np.radians(theta_deg)
        azimuth = np.radians(azimuth_deg)

        t_start, t_end = t_range
        t = np.linspace(t_start, t_end, 800)

        x = x0 + v * np.cos(theta) * t * np.cos(azimuth)
        y = y0 + v * np.cos(theta) * t * np.sin(azimuth)
        z = z0 + v * np.sin(theta) * t - 0.5 * g * t**2

        pts = np.vstack([x, y, z]).T

        if self.line is not None:
            self.w.removeItem(self.line)

        self.line = gl.GLLinePlotItem(
            pos=pts,
            color=pg.glColor(self.color),
            width=3,
            antialias=True
        )
        self.w.addItem(self.line)
