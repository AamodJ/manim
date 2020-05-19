from manimlib.imports import *

class DoublePendulum(Scene):
    CONFIG = {
        'm1': 1,
        'dot1': Dot(),
        'line1': Line(),
        'l1': 1,
        'theta1': PI/2,
        'v1': 0,

        'm2': 2,
        'dot2': Dot(),
        'line2': Line(),
        'l2': 1,
        'theta2': PI/2,
        'v2': 0,
        'g': 1
    }
    def update(self):
        num1 = -self.g*(2*self.m1 + self.m2)*np.sin(self.theta1)
        num2 = -self.m2*self.g*np.sin(self.theta1 - 2*self.theta2)
        num3 = 2*np.sin(self.theta1 - self.theta2)*self.m2
        num4 = (self.v2 ** 2) * self.l2 + (self.v1 ** 2) * self.l1 * np.cos(self.theta1 - self.theta2)
        den = self.l1 * (2*self.m1 + self.m2 - self.m2*np.cos(2*(self.theta1 - self.theta2)))
        a1 = (num1 + num2 + num3 * num4) / den

        self.v1 += a1 * 0.001
        self.theta1 += self.v1

        self.dot1.move_to(RIGHT * self.l1 * np.sin(self.theta1) + DOWN * self.l1 * np.cos(self.theta1))
        self.line1.put_start_and_end_on(ORIGIN, self.dot1.get_center())
        self.dot2.move_to(self.dot1.get_center() + RIGHT * self.l2 * np.sin(self.theta2) + DOWN * self.l2 * np.cos(self.theta2))
        self.line2.put_start_and_end_on(self.dot1.get_center(), self.dot2.get_center())

    def construct(self):
        self.dot1.move_to(RIGHT * self.l1 * np.sin(self.theta1) + DOWN * self.l2 * np.cos(self.theta2))
        self.dot2.move_to(self.dot1.get_center() + RIGHT * self.l2 * np.sin(self.theta2) + DOWN * self.l2 * np.cos(self.theta2))

        self.line1.put_start_and_end_on(ORIGIN, self.dot1.get_center())
        self.line2.put_start_and_end_on(self.dot1.get_center(), self.dot2.get_center())

        self.add(self.dot1, self.dot2, self.line1, self.line2)
        self.wait(1)
        self.dot1.add_updater(lambda d: self.update())
        self.wait(5)
