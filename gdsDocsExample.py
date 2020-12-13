# Layer/datatype definitions for each step in the fabrication
ld_fulletch = {"layer": 1, "datatype": 3}
ld_partetch = {"layer": 2, "datatype": 3}
ld_liftoff = {"layer": 0, "datatype": 7}

p1 = gdspy.Rectangle((-3, -3), (3, 3), **ld_fulletch)
p2 = gdspy.Rectangle((-5, -3), (-3, 3), **ld_partetch)
p3 = gdspy.Rectangle((5, -3), (3, 3), **ld_partetch)
p4 = gdspy.Round((0, 0), 2.5, number_of_points=6, **ld_liftoff)

contact = gdspy.Cell("CONTACT")
contact.add([p1, p2, p3, p4])

# Create a cell with the complete device
device = gdspy.Cell("DEVICE")
device.add(cutout)
# Add 2 references to the component changing size and orientation
ref1 = gdspy.CellReference(contact, (3.5, 1), magnification=0.25)
ref2 = gdspy.CellReference(contact, (1, 3.5), magnification=0.25, rotation=90)
device.add([ref1, ref2])

# The final layout has several repetitions of the complete device
main = gdspy.Cell("MAIN")
main.add(gdspy.CellArray(device, 3, 2, (6, 7)))

lib.write_gds('example.gds')
gdspy.LayoutViewer()
