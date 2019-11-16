# GlowScript 2.7 VPython
from vpython import *


def Head():
    head = sphere(pos=vector(0, 4, 0), radius=1,
                  texture="https://farm5.staticflickr.com/4855/46098387042_fc66d2185f_b.jpg")
    return head


def Torso():
    torso = box(pos=vector(0, 1.25, 0),
                axis=vector(1, -10, 0), length=2,
                height=3, width=2, up=vector(0, 3, 1),
                texture="https://c1.staticflickr.com/3/2032/2344934553_09829bd59c_b.jpg")
    return torso


def Leftarm():
    leftarm = cylinder(pos=vector(0.9, 2.2, 1),
                       axis=vector(1, -3, 0), radius=0.5,
                       texture="https://c1.staticflickr.com/3/2032/2344934553_09829bd59c_b.jpg")
    return leftarm


def Rightarm():
    rightarm = cylinder(pos=vector(-1, 2.5, 0),
                        axis=vector(-1, -3, -0.5), radius=0.5,
                        texture="https://c1.staticflickr.com/3/2032/2344934553_09829bd59c_b.jpg")
    return rightarm


def Leftleg():
    leftleg = cylinder(pos=vector(0.5, -0.25, -0.5),
                       axis=vector(0, -4, -1), radius=0.6,
                       texture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQluZghTkuwfJZy_UsZrUaPePlr0CDM2gSK7Gzk3pn2J8EEeVeh")
    return leftleg


def Rightleg():
    rightleg = cylinder(pos=vector(-0.75, -0.25, -0.5),
                        axis=vector(0, -4, -1), radius=0.6,
                        texture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQluZghTkuwfJZy_UsZrUaPePlr0CDM2gSK7Gzk3pn2J8EEeVeh")
    return rightleg


def Step1(h, t, la, ra, ll, rl):
    i = 0
    dy = 0.2
    while i <= 10:
        # step 2: he does a split -- down motion
        rate(50)
        h.pos.y -= dy
        t.pos.y -= dy
        ll.pos.y -= dy
        rl.pos.y -= dy
        ra.pos.y -= dy
        la.pos.y -= dy
        ll.rotate(angle=(-pi) / 25, axis=vec(0, 0, -5))
        rl.rotate(angle=(pi) / 20, axis=vec(0, 0, -5))
        ra.rotate(angle=(pi) / 20, axis=vec(0, 0, -5))
        la.rotate(angle=(-pi) / 50, axis=vec(0, 0, 5))
        i += 1


def Step2(h, t, la, ra, ll, rl):
    k = 10
    dy = 0.2
    while k >= 0:
        # step 3: he returns to position
        rate(50)  # rate = 50
        h.pos.y += dy
        t.pos.y += dy
        ll.pos.y += dy
        rl.pos.y += dy
        ra.pos.y += dy
        la.pos.y += dy
        k -= 1
        ll.rotate(angle=(pi) / 25, axis=vec(0, 0, -5))
        rl.rotate(angle=(-pi) / 20, axis=vec(0, 0, -5))
        ra.rotate(angle=(-pi) / 20, axis=vec(0, 0, -5))
        la.rotate(angle=(pi) / 50, axis=vec(0, 0, 5))


def Step3(h, t, la, ra, ll, rl):
    i = 0
    while i < 10:
        # step 4: he raises left arm, steps to side
        rate(50)  # rate = 50
        ra.pos.y -= 0.05
        ra.pos.z += 0.05
        ra.pos.x += 0.02
        ll.pos.x += 0.08
        h.pos.y -= 0.01
        h.pos.x -= 0.03
        t.pos.x += 0.03
        ll.rotate(angle=(-pi) / 75, axis=vec(0, 0, -5))
        rl.pos.x += 0.05
        t.rotate(angle=-pi / 150, axis=vec(0, 0, -5))
        la.rotate(angle=(-pi) / 13, axis=vec(0, 1, -5))
        ra.rotate(angle=(pi) / 100, axis=vec(0, 0, -5))
        rl.rotate(angle=(pi) / 100, axis=vec(0, 0, -5))
        h.rotate(angle=-pi / 50, axis=vec(0, 5, 0))

        i += 1


def Step4(h, t, la, ra, ll, rl):
    i = 10
    while i >= 0:
        # step 5: he returns to position
        rate(50)
        ra.pos.y += 0.05
        ra.pos.z -= 0.05
        ra.pos.x -= 0.02
        ll.pos.x -= 0.08
        h.pos.y += 0.01
        h.pos.x += 0.03
        t.pos.x -= 0.03
        ll.rotate(angle=(pi) / 90, axis=vec(0, 0, -5))
        rl.pos.x -= 0.05
        t.rotate(angle=pi / 150, axis=vec(0, 0, -5))
        la.rotate(angle=(pi) / 13, axis=vec(0, 1, -5))
        ra.rotate(angle=(-pi) / 100, axis=vec(0, 0, -5))
        rl.rotate(angle=(-pi) / 130, axis=vec(0, 0, -5))
        h.rotate(angle=pi / 50, axis=vec(0, 5, 0))

        i -= 1


def Step5(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 6: he raises right arm
        rate(50)  # rate = 50
        h.pos.x += 0.05
        h.pos.y -= 0.02
        ll.pos.x += 0.01
        ll.pos.z += 0.03
        ll.pos.y -= 0.01
        rl.pos.x -= 0.02
        t.pos.x += 0.01
        la.pos.y -= 0.01
        la.pos.x += 0.01
        ra.pos.x += 0.01
        rl.rotate(angle=(pi) / 100, axis=vec(0, 0, -5))
        ll.rotate(angle=(-pi) / 110, axis=vec(0, 0, -5))
        t.rotate(angle=(pi) / 230, axis=vec(0, 0, -5))
        ra.rotate(angle=(pi) / 13, axis=vec(0, 0, -5))
        la.rotate(angle=(-pi) / 100, axis=vec(0, 0, -5))
        h.rotate(angle=(pi) / 50, axis=vec(0, 5, 0))

        i += 1


def Step6(h, t, la, ra, ll, rl):
    i = 10
    while i >= 0:
        # he returns to position
        rate(50)  # rate = 50
        h.pos.x -= 0.05
        h.pos.y += 0.02
        ll.pos.x -= 0.01
        ll.pos.z -= 0.03
        ll.pos.y += 0.01
        rl.pos.x += 0.02
        t.pos.x -= 0.01
        la.pos.y += 0.01
        la.pos.x -= 0.01
        ra.pos.x -= 0.01
        rl.rotate(angle=(-pi) / 100, axis=vec(0, 0, -5))
        ll.rotate(angle=(pi) / 110, axis=vec(0, 0, -5))
        t.rotate(angle=(-pi) / 230, axis=vec(0, 0, -5))
        ra.rotate(angle=(-pi) / 13, axis=vec(0, 0, -5))
        la.rotate(angle=(pi) / 100, axis=vec(0, 0, -5))
        h.rotate(angle=(-pi) / 50, axis=vec(0, 5, 0))
        i -= 1


def Step7(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        rate(40)  # rate = 40
        h.pos.x += 0.05
        h.pos.y -= 0.02
        ll.pos.x += 0.01
        ll.pos.z += 0.03
        ll.pos.y -= 0.01
        rl.pos.x -= 0.02
        t.pos.x += 0.01
        la.pos.y -= 0.01
        la.pos.x += 0.01
        ra.pos.x += 0.01
        rl.rotate(angle=(pi) / 100, axis=vec(0, 0, -5))
        ll.rotate(angle=(-pi) / 110, axis=vec(0, 0, -5))
        t.rotate(angle=(pi) / 230, axis=vec(0, 0, -5))
        ra.rotate(angle=(pi) / 15, axis=vec(0, 0, -5))
        la.rotate(angle=(-pi) / 100, axis=vec(0, 0, -5))
        h.rotate(angle=(pi) / 50, axis=vec(0, 15, 0))

        i += 1


def Step8(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 7 in diagram
        rate(40)  # rate = 40
        h.pos.x -= 0.02
        h.pos.y -= 0.02
        h.pos.z += 0.1
        t.pos.x += 0.02
        ll.pos.x += 0.025
        rl.pos.x += 0.05
        la.pos.x += 0.01
        ra.pos.x += 0.01
        ll.pos.y += 0.01
        rl.pos.y += 0.01
        t.rotate(angle=(pi) / 200, axis=vec(0, 0, 5))
        ll.rotate(angle=(pi) / 150, axis=vec(0, 0, -5))
        rl.rotate(angle=(-pi) / 150, axis=vec(0, 0, -5))
        ra.rotate(angle=(pi) / 50, axis=vec(0, 8, -10))
        la.rotate(angle=(-pi) / 13, axis=vec(0, 1, -5))
        # torso.pos.x
        i += 1


def Step9(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 8 in diagram
        rate(40)  # rate = 40
        t.pos.y -= 0.02
        t.pos.x -= 0.01
        t.rotate(angle=(pi) / 100, axis=vec(0, 0, -5))
        rl.pos.y -= 0.01
        rl.pos.x -= 0.05
        rl.rotate(angle=(-pi) / 150, axis=vec(0, 0, -5))
        ll.pos.y -= 0.02
        ll.pos.x -= 0.04
        ll.rotate(angle=(-pi) / 150, axis=vec(0, 0, -5))
        ra.rotate(angle=(-pi) / 14, axis=vec(0, 0, -5))
        ra.pos.x += 0.03
        ra.pos.y += 0.01
        la.rotate(angle=(pi) / 28, axis=vec(0, 1, -5))
        la.pos.y -= 0.05
        h.pos.y -= 0.02
        h.pos.x += 0.04
        h.pos.z -= 0.03

        i += 1


def Step10(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 9
        rate(40)  # rate = 40
        t.rotate(angle=(-pi) / 55, axis=vec(0, 0, -5))
        t.pos.x += 0.01
        t.pos.y -= 0.02
        ll.pos.x += 0.08
        ll.pos.y -= 0.01
        ll.rotate(angle=(pi) / 85, axis=vec(0, 0, -5))
        rl.pos.x += 0.09
        rl.pos.y -= 0.04
        rl.rotate(angle=(pi) / 140, axis=vec(0, 0, -5))
        la.pos.x -= 0.03
        la.pos.y += 0.02
        ra.pos.z -= 0.01
        ra.pos.x -= 0.04
        ra.pos.y -= 0.08
        h.pos.y -= 0.02
        h.pos.x -= 0.09

        i += 1


def Step11(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 10
        rate(40)  # rate = 40
        t.rotate(angle=(pi) / 55, axis=vec(0, 0, -5))
        t.pos.x -= 0.01
        t.pos.y += 0.02
        ll.pos.x -= 0.08
        ll.pos.y += 0.01
        ll.rotate(angle=(-pi) / 85, axis=vec(0, 0, -5))
        rl.pos.x -= 0.09
        rl.pos.y += 0.04
        rl.rotate(angle=(-pi) / 140, axis=vec(0, 0, -5))
        la.pos.x += 0.03
        la.pos.y -= 0.02
        ra.pos.z += 0.01
        ra.pos.x += 0.04
        ra.pos.y += 0.08
        h.pos.y += 0.02
        h.pos.x += 0.09

        i += 1


def Step12(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 11
        rate(40)  # rate = 40
        t.rotate(angle=(-pi) / 60, axis=vec(0, 0, -5))
        t.pos.x += 0.01
        t.pos.y -= 0.01
        ra.pos.x -= 0.04
        ra.pos.y -= 0.05
        ra.pos.z += 0.05
        ra.rotate(angle=pi / 10, axis=vec(-20, -5, 15))
        la.pos.x -= 0.02
        la.pos.y += 0.035
        la.rotate(angle=pi / 100, axis=vec(0, 0, -5))
        rl.pos.x += 0.08
        rl.pos.y -= 0.02
        rl.pos.z += 0.02
        rl.rotate(angle=pi / 100, axis=vec(0, 0, -5))
        ll.pos.x += 0.08
        ll.pos.z += 0.02
        ll.rotate(angle=pi / 100, axis=vec(0, 0, -5))
        h.pos.x -= 0.09
        h.pos.y -= 0.01
        h.rotate(angle=(-pi) / 50, axis=vec(0, 15, 0))

        i += 1


def Step13(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 12
        rate(30)  # rate = 30
        t.pos.x += 0.1
        t.rotate(angle=(pi) / 80, axis=vec(0, 0, -5))
        t.rotate(angle=(pi) / 10, axis=vec(0, 15, 7))
        h.pos.x += 0.18
        h.pos.y += 0.01
        h.rotate(angle=(pi) / 12, axis=vec(0, 5, 0))
        la.pos.x -= 0.04
        la.pos.y += 0.01
        la.pos.z -= 0.02
        la.rotate(angle=(pi) / 10, axis=vec(0, 10, 5))
        ra.rotate(angle=(pi) / 10, axis=vec(0, 5, 5))
        ra.pos.x += 0.333
        ll.pos.x -= 0.05
        ll.pos.y -= 0.01
        ll.rotate(angle=(pi) / 20, axis=vec(0, 10, 0))
        rl.pos.x += 0.2
        rl.pos.y -= 0.03
        rl.pos.z -= 0.02
        rl.rotate(angle=(pi) / 15, axis=vec(0, 10, 0))

        i += 1


def Step14(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 13
        rate(50)  # rate = 40
        t.rotate(angle=(pi) / 85, axis=vec(0, 0, 5))
        t.pos.x += 0.05
        la.rotate(angle=(-pi) / 150, axis=vec(0, 0, -5))
        la.pos.y -= 0.04
        la.pos.x += 0.015
        la.pos.z += 0.02
        # rightarm.rotate(angle=(-pi)/100, axis=vec(0,0,5))
        ra.pos.x += 0.01
        ra.pos.y += 0.015
        ra.pos.z += 0.01
        ll.pos.x += 0.08
        ll.pos.y -= 0.01
        ll.rotate(angle=(-pi) / 170, axis=vec(0, 0, 5))
        rl.pos.x += 0.08
        rl.pos.y -= 0.02
        rl.pos.z -= 0.02
        rl.rotate(angle=(-pi) / 150, axis=vec(0, 0, 5))
        h.pos.x -= 0.05
        h.pos.y -= 0.005

        i += 1


def Step15(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 14 --returns to position at step 12
        rate(40)  # rate = 40
        t.rotate(angle=(-pi) / 85, axis=vec(0, 0, 5))
        t.pos.x -= 0.05
        la.rotate(angle=(pi) / 150, axis=vec(0, 0, -5))
        la.pos.y += 0.04
        la.pos.x -= 0.015
        la.pos.z -= 0.02
        # rightarm.rotate(angle=(-pi)/100, axis=vec(0,0,5))
        ra.pos.x -= 0.01
        ra.pos.y -= 0.015
        ra.pos.z -= 0.01
        ll.pos.x -= 0.08
        ll.pos.y += 0.01
        ll.rotate(angle=(pi) / 170, axis=vec(0, 0, 5))
        rl.pos.x -= 0.08
        rl.pos.y += 0.02
        rl.pos.z += 0.02
        rl.rotate(angle=(pi) / 150, axis=vec(0, 0, 5))
        h.pos.x += 0.05
        h.pos.y += 0.005

        i += 1


def Step16(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        # step 15
        rate(40)  # rate = 40
        t.pos.x += 0.2
        t.rotate(angle=(pi) / 11.5, axis=vec(0.75, 15, 3.5))
        la.pos.x += 0.35
        la.rotate(angle=(pi) / 11.5, axis=vec(0, 10, 0))
        ra.pos.x -= 0.03
        ra.rotate(angle=(pi) / 11, axis=vec(0.5, 10, 3.5))
        h.pos.x += 0.15
        h.rotate(angle=(pi) / 11, axis=vec(0, 10, 1))
        ll.pos.x += 0.333
        ll.rotate(angle=(pi) / 11.5, axis=vec(0, 10, 0))
        rl.pos.x += 0.1
        rl.rotate(angle=(pi) / 15, axis=vec(0.5, 10, -2))

        i += 1


def Step17(h, t, la, ra, ll, rl):
    sleep(0.3)
    i = 0
    while i <= 5:
        rate(10)  # rate = 10
        if h.pos.x < 3:
            h.pos.x += 0.4
            h.pos.y += 0.04
        else:
            h.pos.x -= 0.25
            h.pos.y -= 0.01
        i += 1


def Step18(h, t, la, ra, ll, rl):
    sleep(0.05)
    i = 0
    while i <= 10:
        # step 16
        rate(25)  # rate = 25
        t.pos.y -= 0.2
        t.pos.x += 0.1
        t.rotate(angle=(pi) / 30, axis=vec(-3, 0, 10))
        la.pos.y -= 0.15
        la.pos.x -= 0.065
        la.pos.z -= 0.02
        la.rotate(angle=(pi) / 150, axis=vec(0, 0, 10))
        ra.rotate(angle=(pi) / 150, axis=vec(0, 0, 5))
        ll.pos.y -= 0.06
        ll.pos.x += 0.2
        ll.rotate(angle=(pi) / 50, axis=vec(0, 0, 10))
        rl.pos.x += 0.26
        rl.pos.y -= 0.16
        rl.rotate(angle=(pi) / 40, axis=vec(0, 0, 10))
        ra.pos.x += 0.05
        ra.pos.y -= 0.35
        ra.rotate(angle=(pi) / 14, axis=vec(-1, 0, 10))
        h.pos.y -= 0.333
        h.pos.x -= 0.1
        h.pos.z -= 0.01
        h.rotate(angle=(pi) / 70, axis=vec(0, 0, 10))

        i += 1


def Step19(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        rate(35)
        t.pos.x -= 0.1
        t.pos.y += 0.08
        t.rotate(angle=(pi) / 30, axis=vec(-3, 0, 10))
        la.pos.x -= 0.15
        la.pos.y -= 0.05
        la.pos.z -= 0.03
        la.rotate(angle=(pi) / 12, axis=vec(0, -3, 10))
        h.pos.y -= 0.14
        h.pos.x -= 0.07
        h.pos.z -= 0.06
        h.rotate(angle=(pi) / 20, axis=vec(0, -3, 10))
        ll.pos.x -= 0.22
        ll.pos.y += 0.2
        ll.rotate(angle=(pi) / 11, axis=vec(0, 0, 10))
        rl.pos.x -= 0.08
        rl.pos.y += 0.25
        rl.rotate(angle=(pi) / 55, axis=vec(0, -3, 10))

        i += 1


def Step20(h, t, la, ra, ll, rl):
    # sleep(1)
    i = 0
    while i <= 10:
        rate(20)
        # t.pos.x -= 0.07
        # t.pos.y += 0.02
        # t.rotate(angle=(pi)/10.5, axis=vec(0,10,-0.5))
        t.rotate(angle=(pi) / 5.5, axis=vec(0, 10, 0), origin=vec(3.1, -1.5, 0))
        h.rotate(angle=pi / 5.5, axis=vec(0, 10, 0), origin=vec(3, 0, 0))
        rl.rotate(angle=(pi) / 5.5, axis=vec(0, 10, 0), origin=vec(3, 0, 0))
        ll.rotate(angle=(pi) / 5.5, axis=vec(0, 10, 0), origin=vec(3, 0, 0))
        la.rotate(angle=(pi) / 5.5, axis=vec(0, 10, 0), origin=vec(3, 0, 0))
        ra.rotate(angle=pi / 5.5, axis=vec(0, 10, 0))

        i += 1


def Step21(h, t, la, ra, ll, rl):
    sleep(0.1)
    i = 0
    while i <= 10:
        rate(40)
        t.rotate(angle=pi / 100, axis=vec(0, 0, 10), origin=vec(1, 0, 0))
        t.pos.y -= 0.05
        t.pos.x -= 0.05
        ll.rotate(angle=-pi / 150, axis=vec(0, 0, 10), origin=vec(3, 5, 0))
        rl.rotate(angle=pi / 25, axis=vec(0, 0, 10), origin=vec(4.5, 0, 0))
        la.rotate(angle=-pi / 40, axis=vec(0, 0, 10), origin=vec(0.4, -0.08, 0))
        la.pos.y += 0.05
        h.rotate(angle=pi / 150, axis=vec(0, 0, 10), origin=vec(4, -1, 0))

        i += 1


def Step22(h, t, la, ra, ll, rl):
    sleep(0.05)
    i = 0
    while i <= 10:
        rate(45)
        ll.rotate(angle=-pi / 35, axis=vec(0, 0, 10))
        ra.rotate(angle=-pi / 100, axis=vec(0, 0, 10))
        la.rotate(angle=pi / 40, axis=vec(0, 0, 10))
        h.rotate(angle=-pi / 100, axis=vec(5, 0, 10))

        i += 1


def Step23(h, t, la, ra, ll, rl):
    # sleep(1.5)
    i = 0
    while i <= 10:
        rate(45)
        t.rotate(angle=-pi / 13, axis=vec(-3.8, 0, 10), origin=vec(5, -0.5, 0))
        rl.rotate(angle=-pi / 11.333, axis=vec(0, 0, 10), origin=vec(5.5, -0.5, 0))
        ll.rotate(angle=-pi / 13.333, axis=vec(0, 0, 10), origin=vec(5.75, -0.7, 0))
        ll.pos.x += 0.0333
        ll.pos.y -= 0.155
        ra.rotate(angle=-pi / 15, axis=vec(0, 0, 10), origin=vec(5, -0.75, 0))
        la.rotate(angle=-pi / 13.333, axis=vec(0, 0, 10), origin=vec(5.25, -0.7, 0))
        h.rotate(angle=-pi / 13, axis=vec(-3.8, 0, 10), origin=vec(5, -0.5, 0))
        # ra.pos.x += 0.3
        # ra.pos.y -= 0.025

        i += 1


def Step24(h, t, la, ra, ll, rl):
    sleep(0.1)
    i = 0
    while i <= 10:
        rate(40)
        la.rotate(angle=pi / 40, axis=vec(0, 0, 10))
        h.rotate(angle=pi / 70, axis=vec(-2, 5, 5))
        ll.rotate(angle=-pi / 135, axis=vec(0, 0, 10))
        # ll.pos.x += 0.01

        i += 1


def Step25(h, t, la, ra, ll, rl):
    sleep(0.1)
    while t.pos.x > 0:
        rate(15)
        t.pos.x -= 0.8
        h.pos.x -= 0.8
        la.pos.x -= 0.95
        la.pos.z += 0.225
        la.pos.y -= 0.01
        ra.pos.x -= 0.85
        ra.pos.z += 0.05
        ll.pos.x -= 0.9
        ll.pos.z += 0.1
        rl.pos.x -= 0.95
        rl.pos.z += 0.1
        t.rotate(angle=-pi / 3.9, axis=vec(0, 10, 0.5))
        h.rotate(angle=-pi / 3.9, axis=vec(0, 10, 0.5))
        la.rotate(angle=pi / 20, axis=vec(2, 5, 0))
        ra.rotate(angle=pi / 3.9, axis=vec(0, 10, 0.5))
        ll.rotate(angle=-pi / 2, axis=vec(0, 10, 0.5))
        rl.rotate(angle=-pi / 3.9, axis=vec(0, 10, 0.5))


def Step26(h, t, la, ra, ll, rl):
    i = 0
    while i <= 10:
        rate(25)
        h.rotate(angle=pi / 50, axis=vec(0, 10, 0.5))
        t.rotate(angle=pi / 100, axis=vec(0, 10, 0.5))
        rl.rotate(angle=pi / 100, axis=vec(0, -10, 0))
        rl.pos.x += 0.02
        la.rotate(angle=-pi / 15, axis=vec(0, 0, 10))
        la.pos.x += 0.02
        ra.rotate(angle=pi / 15, axis=vec(0, 0, 10))

        i += 1


head = Head()
torso = Torso()
leftarm = Leftarm()
rightarm = Rightarm()
leftleg = Leftleg()
rightleg = Rightleg()

sleep(2)
Step1(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.05)
Step2(head, torso, leftarm, rightarm, leftleg, rightleg)
Step3(head, torso, leftarm, rightarm, leftleg, rightleg)
Step4(head, torso, leftarm, rightarm, leftleg, rightleg)
Step5(head, torso, leftarm, rightarm, leftleg, rightleg)
Step6(head, torso, leftarm, rightarm, leftleg, rightleg)
Step3(head, torso, leftarm, rightarm, leftleg, rightleg)
Step4(head, torso, leftarm, rightarm, leftleg, rightleg)
Step5(head, torso, leftarm, rightarm, leftleg, rightleg)
Step6(head, torso, leftarm, rightarm, leftleg, rightleg)
Step7(head, torso, leftarm, rightarm, leftleg, rightleg)
Step8(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.1)
Step9(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.2)
Step10(head, torso, leftarm, rightarm, leftleg, rightleg)
Step11(head, torso, leftarm, rightarm, leftleg, rightleg)
Step10(head, torso, leftarm, rightarm, leftleg, rightleg)
Step11(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.1)
Step12(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.2)
Step13(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.1)
Step14(head, torso, leftarm, rightarm, leftleg, rightleg)
Step15(head, torso, leftarm, rightarm, leftleg, rightleg)
Step14(head, torso, leftarm, rightarm, leftleg, rightleg)
Step15(head, torso, leftarm, rightarm, leftleg, rightleg)
Step14(head, torso, leftarm, rightarm, leftleg, rightleg)
Step15(head, torso, leftarm, rightarm, leftleg, rightleg)
Step14(head, torso, leftarm, rightarm, leftleg, rightleg)
Step15(head, torso, leftarm, rightarm, leftleg, rightleg)
sleep(0.1)
Step16(head, torso, leftarm, rightarm, leftleg, rightleg)
Step17(head, torso, leftarm, rightarm, leftleg, rightleg)
# from now on, functions have sleep built into them
Step18(head, torso, leftarm, rightarm, leftleg, rightleg)
Step19(head, torso, leftarm, rightarm, leftleg, rightleg)
Step20(head, torso, leftarm, rightarm, leftleg, rightleg)
Step20(head, torso, leftarm, rightarm, leftleg, rightleg)
Step20(head, torso, leftarm, rightarm, leftleg, rightleg)
Step21(head, torso, leftarm, rightarm, leftleg, rightleg)
Step22(head, torso, leftarm, rightarm, leftleg, rightleg)
Step23(head, torso, leftarm, rightarm, leftleg, rightleg)
Step24(head, torso, leftarm, rightarm, leftleg, rightleg)
Step25(head, torso, leftarm, rightarm, leftleg, rightleg)
Step26(head, torso, leftarm, rightarm, leftleg, rightleg)