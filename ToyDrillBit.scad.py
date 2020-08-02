#!/usr/bin/env python3

'''
Toy drill bit for "Think Gizmos take apart racing car".
'''

import numpy as np

import solid


def bit(hex_dia, hex_depth, drive_fin_dia, drive_fin_width, bevel=1):
    block = solid.cylinder(d=hex_dia*2/np.sqrt(3), h=hex_depth, segments=6)
    taper = solid.cylinder(d1=hex_dia*2/np.sqrt(3), d2=0, h=hex_depth*3/2, segments=6)
    taper = solid.translate([0,0,hex_depth])(taper)
    block += taper

    fin = solid.cube([drive_fin_dia, drive_fin_width, 3*hex_depth], center=True)
    # block += solid.translate([0,0,hex_depth])(
        # solid.cylinder(d1=hex_dia*2/np.sqrt(3), d2=drive_fin_dia, h=hex_depth, segments=6))
    fin = solid.cube([drive_fin_dia-2*bevel, drive_fin_width, 3*hex_depth], center=True)
    fin += solid.cube([drive_fin_dia, drive_fin_width, 3*hex_depth-2*bevel], center=True)
    fin = solid.hull()(fin)
    fin = solid.translate([0,0,1.5*hex_depth])(fin)
    fin += solid.rotate([0,0,90])(fin)
    block += fin
    return block


if __name__ == '__main__':
    hex_dia = 14  # 25.4*9/16=14.2875
    hex_depth = 25.4/2
    drive_fin_dia = 9.5  # 25.4*3/8=9.525
    drive_fin_width = 1.5  # 25.4/16=1.5875
    final = bit(hex_dia, hex_depth, drive_fin_dia, drive_fin_width)
    print(solid.scad_render(final))
