import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
from cone.cone import blue_cone, yellow_cone

# Paths to the files used
map_2d_path = 'utils/nurburgring_map_2D.jpg'
csv_nurbur_path = 'data/nurbur_data.csv'

background_image = mpimg.imread(map_2d_path)

blue_cones = []
yellow_cones = []

with open(csv_nurbur_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        blue_cone_obj = blue_cone(float(row['X_left']), float(row['Y_left']))
        blue_cones.append(blue_cone_obj)
        yellow_cone_obj = yellow_cone(float(row['X_right']), float(row['Y_right']))
        yellow_cones.append(yellow_cone_obj)

left_boundary = np.array([[cone.x for cone in blue_cones], [cone.y for cone in blue_cones]])
right_boundary = np.array([[cone.x for cone in yellow_cones], [cone.y for cone in yellow_cones]])

midpoints = []

# Traverse the left and right cones to calculate midpoints and add the midpoint to the list of midpoints
for i in range(len(left_boundary[0])):
    x_left = left_boundary[0][i]
    y_left = left_boundary[1][i]
    x_right = right_boundary[0][i]
    y_right = right_boundary[1][i]
    
    midpoint_x = (x_left + x_right) / 2
    midpoint_y = (y_left + y_right) / 2
    
    midpoints.append([midpoint_x, midpoint_y])

# Convert the list of midpoints into a numpy array
intermediate_trace = np.array(midpoints)

# Number of intermediate points to add between each pair of points
num_intermediate_points = 60

# Initialize a new array to store points with interpolation
new_intermediate_trace = []

# Traverse the original trace to add intermediate points
for i in range(len(intermediate_trace) - 1):
    x1, y1 = intermediate_trace[i]
    x2, y2 = intermediate_trace[i + 1]
    
    # Calculate the distance between the two points
    distance_between_points = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Interpolate the intermediate points only if the distance is greater than a threshold
    if distance_between_points > 0.01:  # 0.01 is an arbitrary threshold
        interp_x = np.linspace(x1, x2, num_intermediate_points + 2)[1:-1]
        interp_y = np.linspace(y1, y2, num_intermediate_points + 2)[1:-1]
        new_intermediate_trace.extend(list(zip(interp_x, interp_y)))
    else:
        new_intermediate_trace.append([x1, y1])

# Add the last point of the original trace
new_intermediate_trace.append(intermediate_trace[-1])

# Convert the list of points into a numpy array
intermediate_trace = np.array(new_intermediate_trace)

plt.figure(figsize=(10, 6))
plt.imshow(background_image)

for i in range(len(right_boundary[0])):
    plt.scatter(right_boundary[0][i], right_boundary[1][i], c="yellow")

for i in range(len(left_boundary[0])):
    plt.scatter(left_boundary[0][i], left_boundary[1][i], c="blue")

# Initialize the red point at the first position
red_point = plt.scatter(intermediate_trace[0, 0], intermediate_trace[0, 1], c="red")

plt.plot(intermediate_trace[:, 0], intermediate_trace[:, 1], 'g-', label='Intermediate Trace')

plt.title('2D Representation of the Nürburgring Circuit')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()

plt.grid(True)

# Update the position of the red point in a loop
for i in range(1, len(intermediate_trace)):
    x, y = intermediate_trace[i]
    red_point.set_offsets([x, y])
    plt.pause(0.001)  # Add a 0.01-second delay between updates

plt.show()
