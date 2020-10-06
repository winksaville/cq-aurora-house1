import os
import sys
import cadquery as cq
from math import sqrt
from typing import Tuple, cast


from utils import show, dbg, dbg_circle, set_ctx, scale_tuple

set_ctx(globals())

thickness = 2
width = 1
length = 1
height = 1
roof_height = sqrt(((6/8) ** 2) - ((width / 2) ** 2))
scale = 50 / (roof_height + height)
print(f"scale={scale}")
total_height = (roof_height + height) * scale
print(f"total_height={total_height}")


result = (
    cq.Workplane("front")
    .lineTo(0 * scale, height * scale)
    .lineTo((width / 2) * scale, (height + roof_height) * scale)
    .lineTo(width * scale, height * scale)
    .lineTo(width * scale, 0)
    .close()
    .extrude(length * scale)
)
show(result, "r")

dbg_circle(width / 2 * scale, (height + roof_height) * scale, 0.1, name="pt")

stl_tolerance = 0.001
directory: str = "generated/"
fname = f"house1.stl"
cq.exporters.export(result, os.path.join(directory, fname), tolerance=stl_tolerance)
dbg(f"{fname}")

