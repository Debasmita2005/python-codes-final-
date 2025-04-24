def create_array(dim1, dim2, dim3, init_value):
    # Create a 3D array with the given dimensions
    # and initialize each element to init_value
    array_3d = [[[init_value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
    return array_3d

# Test the function
dimensions = (2, 3, 4)  # 2x3x4 array
init_val = 7

result_array = create_array(*dimensions, init_val)

print(f"Created a {dimensions[0]}x{dimensions[1]}x{dimensions[2]} array initialized with {init_val}:")
for i in range(dimensions[0]):
    print(f"Layer {i+1}:")
    for j in range(dimensions[1]):
        print(result_array[i][j])
