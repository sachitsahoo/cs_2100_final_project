class Params:
    def __init__(self, velocity: float, theta: float, azimuthal_angle: float, g: float, t_start: int, t_end: int, x0: float, y0: float, z0: float):
        self.velocity = velocity
        self.theta = theta
        self.azimuthal_angle = azimuthal_angle
        self.g = g
        self.t_start = t_start
        self.t_end = t_end
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

    def print_all(self):
        print(
            f"Velocity: {self.velocity}\n"
            f"Theta: {self.theta}\n"
            f"Azimuthal Angle: {self.azimuthal_angle}\n"
            f"Gravity (g): {self.g}\n"
            f"Start Time (t_start): {self.t_start}\n"
            f"End Time (t_end): {self.t_end}\n"
            f"Initial X (x0): {self.x0}\n"
            f"Initial Y (y0): {self.y0}\n"
            f"Initial Z (z0): {self.z0}"
        )


    