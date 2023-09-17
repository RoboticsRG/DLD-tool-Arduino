from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *  # basic matrix operations
import time


# toque do suporte no centro do smartphone
# [   -54.000000,     0.000000,   210.000000,     0.000000,    90.000000,    -0.000000 ]

# home teste
# [  -100.000000,     0.000024,   209.999914,     0.000000,    90.000000,    -0.000000 ]

# home processamento de imagem
# [  -120.000000,  -180.000000,   210.000000,     0.000000,    90.000000,     0.000000 ]

class Cobotta:

    def __init__(self):

        self.resolution = [1920, 1080]
        self.smartphone = [165, 76, 10]
        self.ref_touch_center = [-54.000000, 0.000000, 210.000000]
        self.gap = 15
        self.smartphone_sup_left = [self.ref_touch_center[0] - self.gap,
                                    self.ref_touch_center[1] + (self.smartphone[1] / 2),
                                    self.ref_touch_center[2] - (self.smartphone[0] / 2)]
        self.smartphone_sup_right = [self.ref_touch_center[0] - self.gap,
                                     self.ref_touch_center[1] - (self.smartphone[1] / 2),
                                     self.ref_touch_center[2] - (self.smartphone[0] / 2)]
        self.smartphone_inf_left = [self.ref_touch_center[0] - self.gap,
                                    self.ref_touch_center[1] + (self.smartphone[1] / 2),
                                    self.ref_touch_center[2] + (self.smartphone[0] / 2)]
        self.smartphone_inf_right = [self.ref_touch_center[0] - self.gap,
                                     self.ref_touch_center[1] - (self.smartphone[1] / 2),
                                     self.ref_touch_center[2] + (self.smartphone[0] / 2)]

        self.joints_ref = [-50.000000, 25.000000, 125.000000, -55.000000, -72.000000,
                           25.000000]  # Valores dos angulos em graus para todos os eixos

        self.borda_scroll_up_down = 40
        self.borda_scroll_left_right = 10
        self.borda_touch = 0
        self.distance_screen = 10

        # Any interaction with RoboDK must be done through RDK:
        self.RDK = Robolink()
        # Select a robot (popup is displayed if more than one robot is available)
        self.robot = self.RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)
        if not self.robot.Valid():
            raise Exception('No robot selected or available')

        # get the current position of the TCP with respect to the reference frame:
        # (4x4 matrix representing position and orientation)
        target_ref = self.robot.Pose()
        pos_ref = target_ref.Pos()
        print("Drawing a polygon around the target: ", Pose_2_TxyzRxyz(target_ref))

        # move the robot to the first point:
        self.robot.MoveJ(target_ref)

        self.robot.MoveJ(joints_ref)

        # It is important to provide the reference frame and the tool frames when generating programs offline
        self.robot.setPoseFrame(self.robot.PoseFrame())
        self.robot.setPoseTool(self.robot.PoseTool())
        self.robot.setRounding(
            10)  # Set the rounding parameter (Also known as: CNT, APO/C_DIS, ZoneData, Blending radius, cornering, ...)
        self.robot.setSpeed(200)  # Set linear speed in mm/s

    def move_robot(self, pos_i):
        print(pos_i)
        target_i = self.robot.Pose()
        # target_i = Mat(target_ref_robot)
        target_i.setPos(pos_i)
        try:
            self.robot.MoveL(target_i)
        except TargetReachError as erro:
            print("\033[1;31m", erro, "\033[0;0m")
            self.move_robot([-64.000000, 0.000000, 210.000000])
            self.robot.MoveL(target_i)
        # print(target_i)
        time.sleep(1)

    def touch(self, x, y):
        # resolution = [1920, 1080]
        # smartphone = [165, 76, 10]
        # ref_touch_center = [-54.000000, 0.000000, 210.000000]
        # borda_touch = 5
        # ref_touch_center = [-54.000000, 0.000000, 210.000000]

        # bloqueia o x e y para as dimensoes do smartphone
        if x > self.smartphone[1]:
            x = self.smartphone[1]
        if y > self.smartphone[0]:
            y = self.smartphone[0]

        if x > self.smartphone[1] / 2:
            x0_y0 = [self.ref_touch_center[1] + self.smartphone[1] / 2 + self.borda_touch,
                     self.ref_touch_center[2] - self.smartphone[0] / 2 + self.borda_touch]
            start = [self.ref_touch_center[0] - self.distance_screen, x0_y0[0] - x, x0_y0[1] + y]
            touch_smartphone = [self.ref_touch_center[0], x0_y0[0] - x, x0_y0[1] + y]
            end = [self.ref_touch_center[0] - self.distance_screen, x0_y0[0] - x, x0_y0[1] + y]
            print("aaaaaa")
        else:
            x0_y0 = [self.ref_touch_center[1] + self.smartphone[1] / 2 - self.borda_touch,
                     self.ref_touch_center[2] - self.smartphone[0] / 2 + self.borda_touch]
            start = [self.ref_touch_center[0] - self.distance_screen, x0_y0[0] - x, x0_y0[1] + y]
            touch_smartphone = [self.ref_touch_center[0], x0_y0[0] - x, x0_y0[1] + y]
            end = [self.ref_touch_center[0] - self.distance_screen, x0_y0[0] - x, x0_y0[1] + y]
            print("bbbbbbb")
            print(
                self.ref_touch_center[1], self.smartphone[1] / 2, self.borda_touch, self.ref_touch_center[2],
                self.smartphone[0] / 2, self.borda_touch)

        print(x, y)
        print(x0_y0)
        print(start)
        print(touch_smartphone)
        self.move_robot(start)
        self.move_robot(touch_smartphone)
        self.move_robot(end)

    # def scroll_left():
    #     touch_left = ref_touch_center[1] + smartphone[1] / 2 - borda_scroll_left_right
    #     touch_right = ref_touch_center[1] - smartphone[1] / 2 + borda_scroll_left_right
    #
    #     start = [ref_touch_center[0] - distance_screen, touch_right, ref_touch_center[2]]
    #     move_robot(start)
    #
    #     touch_right_smartphone = [ref_touch_center[0], touch_right, ref_touch_center[2]]
    #     move_robot(touch_right_smartphone)
    #
    #     touch_left_smartphone = [ref_touch_center[0], touch_left, ref_touch_center[2]]
    #     move_robot(touch_left_smartphone)
    #
    #     end = [ref_touch_center[0] - distance_screen, touch_left, ref_touch_center[2]]
    #     move_robot(end)
    #
    # def scroll_right():
    #     touch_left = ref_touch_center[1] + smartphone[1] / 2 - borda_scroll_left_right
    #     touch_right = ref_touch_center[1] - smartphone[1] / 2 + borda_scroll_left_right
    #
    #     start = [ref_touch_center[0] - distance_screen, touch_left, ref_touch_center[2]]
    #     move_robot(start)
    #
    #     touch_right_smartphone = [ref_touch_center[0], touch_left, ref_touch_center[2]]
    #     move_robot(touch_right_smartphone)
    #
    #     touch_left_smartphone = [ref_touch_center[0], touch_right, ref_touch_center[2]]
    #     move_robot(touch_left_smartphone)
    #
    #     end = [ref_touch_center[0] - distance_screen, touch_right, ref_touch_center[2]]
    #     move_robot(end)
    #
    # def move_touch_home():
    #     robot.MoveJ(joints_ref)
    #
    # def move_touch_center():
    #     move_robot(ref_touch_center)
    #
    # def scroll_up():
    #     touch_down = ref_touch_center[2] + smartphone[0] / 2 - borda_scroll_up_down
    #     touch_up = ref_touch_center[2] - smartphone[0] / 2 + borda_scroll_up_down
    #     start = [ref_touch_center[0] - distance_screen, ref_touch_center[1], touch_down]
    #     move_robot(start)
    #
    #     touch_down_smartphone = [ref_touch_center[0], ref_touch_center[1], touch_down]
    #     move_robot(touch_down_smartphone)
    #
    #     touch_up_smartphone = [ref_touch_center[0], ref_touch_center[1], touch_up]
    #     move_robot(touch_up_smartphone)
    #
    #     end = [ref_touch_center[0] - distance_screen, ref_touch_center[1], touch_up]
    #     move_robot(end)
    #
    # def scroll_down():
    #     touch_down = ref_touch_center[2] + smartphone[0] / 2 - borda_scroll_up_down
    #     touch_up = ref_touch_center[2] - smartphone[0] / 2 + borda_scroll_up_down
    #     start = [ref_touch_center[0] - distance_screen, ref_touch_center[1], touch_up]
    #     move_robot(start)
    #
    #     touch_down_smartphone = [ref_touch_center[0], ref_touch_center[1], touch_up]
    #     move_robot(touch_down_smartphone)
    #
    #     touch_up_smartphone = [ref_touch_center[0], ref_touch_center[1], touch_down]
    #     move_robot(touch_up_smartphone)
    #
    #     end = [ref_touch_center[0] - distance_screen, ref_touch_center[1], touch_down]
    #     move_robot(end)
    #
    # def double_rotation():
    #     robot.MoveJ(joints_ref)
    #     portrait = [-50.000000, 25.000000, 125.000000, -55.000000, -72.000000, 25.000000]
    #     landscape = [-50.000000, 25.000000, 125.000000, -55.000000, -72.000000, -65.000000]
    #
    #     robot.MoveJ(portrait)
    #     robot.MoveJ(landscape)
    #     time.sleep(2)
    #     robot.MoveJ(portrait)
    #
    # # positions = [[-66.008406, -44.500000, 357.0, 0.0, 90.000000, 0.0],
    # #              [-66.008395, -44.500000, 212.124424, 0.0, 90.000000, 0.0],
    # #              [-66.008382, 1.744865, 212.124423, 0.0, 90.000000, 0.0],
    # #              [-47.304185, 1.744865, 212.124423, 0.0, 90.000000, 0.0],
    # #              [-66.008382, 1.744865, 212.124423, 0.0, 90.000000, 0.0],
    # #              [-66.008395, -44.500000, 212.124424, 0.0, 90.000000, 0.0],
    # #              [-66.008406, -44.500000, 357.0, 0.0, 90.000000, 0.0]]
    #
    # positions = [[-66.008406, -44.500000, 357.008131],
    #              [-66.008395, -44.500000, 212.124424],
    #              [-66.008382, 1.744865, 212.124423],
    #              [-47.304185, 1.744865, 212.124423],
    #              [-66.008382, 1.744865, 212.124423],
    #              [-66.008395, -44.500000, 212.124424],
    #              [-66.008406, -44.500000, 357.008113]]
    #
    # # [   -66.008406,   -44.500000,   357.000000,     0.000000,    90.000000,     0.000000 ]
    #
    # positions = [smartphone_sup_left, smartphone_sup_right, smartphone_inf_left, smartphone_inf_right]
    # positions = [smartphone_sup_right, smartphone_inf_left, smartphone_inf_right, smartphone_sup_left]

    # print(smartphone_sup_left)
    # print(smartphone_sup_right)
    # print(smartphone_inf_left)
    # print(smartphone_inf_right)
    # print('/////////////////////////')
    # for pos in positions:
    #     print(pos)
    #     move_robot(pos)
    #     time.sleep(3)

    # move_robot(smartphone_sup_left)
    # move_robot(smartphone_sup_right)
    # move_robot(smartphone_inf_left)
    # move_robot(smartphone_inf_right)

    # scroll_up()
    # robot.MoveJ(joints_ref)
    # time.sleep(2)
    # scroll_down()
    # robot.MoveJ(joints_ref)

    # double_rotation()
    # move_touch_home()
    # robot.MoveJ(joints_ref)
    # move_touch_center()

    # touch(0, 165)

    # touch(75, 0)

    # touch(0, 165)

    # touch(75, 165)

    # scroll_right()
    # scroll_left()


if __name__ == '__main__':
    robot_cobotta = Cobotta()
    robot_cobotta.touch(0, 165)
