import cadquery as cq


def make_stator():
    d_outer = 52
    d_inner = 24
    width = 29
    rv = (cq.Workplane()
    .center((d_outer-d_inner)/4+d_inner/2,0)
    .rect((d_outer-d_inner)/2, width)
    .center(-(d_outer-d_inner)/4-d_inner/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv

def make_rotor():
    d_outer = 58.6
    d_inner = 52.6
    width = 25
    rv = (cq.Workplane()
    .center((d_outer-d_inner)/4+d_inner/2,0)
    .rect((d_outer-d_inner)/2, width)
    .center(-(d_outer-d_inner)/4-d_inner/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv

def make_rim():
    d_motor = 58.6
    r_motor = d_motor/2
    d_bearing = 62
    r_bearing = d_bearing/2
    d_outer = 70
    r_outer = d_outer/2
    width_motor = 29
    width_bearing = 6
    width = width_motor + 2*width_bearing
    points = [(r_motor, 0),
              (r_motor, width_motor/2),
              (r_bearing, width_motor/2),
              (r_bearing, width/2),
              (r_outer, width/2),
              (r_outer, 0),
              ]
    rv = (cq.Workplane()
    #.center((d_outer-d_motor)/4+d_motor/2,0)
    #.rect((d_outer-d_inner)/2, width)
    .polyline(points)
    .mirrorX()
    #.center(-(d_outer-d_motor)/4-d_motor/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv

def make_shaft():
    diameter_motor = 24
    diameter_hole = 15
    width_motor = 29
    width_bearing = 6
    width_bracket = 5
    length = width_motor+2*width_bearing+2*width_bracket
    length_hole = length/2+5
    rv = (
        cq.Workplane("XZ")
        .cylinder(length, diameter_motor/2)
        .faces("<Y")
        .hole(diameter_hole, length_hole)
    )
    return rv

def make_statdistring():
    d_inner = 24
    d_outer = 50
    width_bearing = 6
    width = width_bearing + 1

    rv = (cq.Workplane()
    )
    return rv

def make_bearing():
    d_inner = 50
    d_outer = 62
    width = 6
    rv = (cq.Workplane()
    .center((d_outer-d_inner)/4+d_inner/2,0)
    .rect((d_outer-d_inner)/2, width)
    .center(-(d_outer-d_inner)/4-d_inner/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv


# Render the solid

motor = ( cq.Assembly()
        #.add(make_stator(), name="stator", color=cq.Color("darkgoldenrod1"))
        .add(make_rotor(), name="rotor", color=cq.Color("gray60"))
        .add(make_rim(), name="rim", color=cq.Color("green"))
        .add(make_bearing(), name="left_bearing", color=cq.Color("red"), loc=cq.Location(cq.Vector(0, +(29/2 + 6/2), 0), cq.Vector(1, 0, 0), 0))
        .add(make_bearing(), name="right_bearing", color=cq.Color("red"), loc=cq.Location(cq.Vector(0, -(29/2 + 6/2), 0), cq.Vector(1, 0, 0), 0))
        .add(make_shaft(), name="shaft", color=cq.Color("pink"))
         )

show_object(motor)
