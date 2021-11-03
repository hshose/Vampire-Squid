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
    d_inner = 58.6
    d_outer = 70
    width = 50
    rv = (cq.Workplane()
    .center((d_outer-d_inner)/4+d_inner/2,0)
    .rect((d_outer-d_inner)/2, width)
    .center(-(d_outer-d_inner)/4-d_inner/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv

def make_statdistring():
    d_inner = 24
    d_outer = 32
    width = 2
    rv = (cq.Workplane()
    .center((d_outer-d_inner)/4+d_inner/2,0)
    .rect((d_outer-d_inner)/2, width)
    .center(-(d_outer-d_inner)/4-d_inner/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv

def make_bearing():
    d_inner = 35
    d_outer = 62
    width = 9
    rv = (cq.Workplane()
    .center((d_outer-d_inner)/4+d_inner/2,0)
    .rect((d_outer-d_inner)/2, width)
    .center(-(d_outer-d_inner)/4-d_inner/2,0)
    .revolve(360, (0,0,0),(0,-1,0))
    )
    return rv

def make_shaft():
    do = 24
    pts = [(0, l/2),(do/2, l/2), (do/2, l/2)]
    rv = ( cq.Workplane()
      )


# Render the solid

motor = ( cq.Assembly()
         .add(make_stator(), name="stator", color=cq.Color("darkgoldenrod1"))
         .add(make_rotor(), name="rotor", color=cq.Color("gray60"))
         .add(make_rim(), name="rim", color=cq.Color("gray90"))
         .add(make_bearing(), name="left_bearing", color=cq.Color("red"))
          .add(make_bearing(), name="right_bearing", color=cq.Color("red"))
         )

show_object(motor)