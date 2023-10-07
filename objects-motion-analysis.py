initial_params = {
    "x0" : int(input("Enter the initial position (m): ")),
    "v0" : int(input("Enter the initial velocity (m/s): ")),
    "a" : int(input("Enter the acceleration (m/s^2): ")),
    "t" : int(input("Enter the time (s): ")), 
}

final_position = int(initial_params["x0"] + initial_params["v0"]* initial_params["t"] + 0.5*initial_params["a"]*initial_params["t"]**2)
final_velocity = int(initial_params["v0"] + initial_params["a"]*initial_params["t"])

print(f"Final Position (x): {final_position}")
print(f"Final Velocity (m/s): {final_velocity}")