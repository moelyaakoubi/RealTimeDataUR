import rtde.rtde as rtde
import rtde.rtde_config as rtde_config

ROBOT_IP = '192.168.0.1'  # Replace with your robot's IP address
RTDE_PORT = 30004  # RTDE data port

# Load RTDE configuration file


config = rtde_config.ConfigFile("record_configuration.xml")
output_names, output_types = config.get_recipe("out")

# Attempt to connect to the robot's RTDE interface
try:
    rtde_con = rtde.RTDE(ROBOT_IP, RTDE_PORT)
    rtde_con.connect()
    print("RTDE connection successful!")

    # Get controller version to confirm connection
    if rtde_con.get_controller_version():
        print("Robot controller version retrieved successfully.")

    # Setup output recipe
    rtde_con.send_output_setup(output_names, output_types)
    rtde_con.send_start()

    # Try to receive one data packet to test
    state = rtde_con.receive()

    if state:
        # Access and print joint positions and currents
        print(f"voltage: {state.actual_joint_voltage}")
        print(f"target_current: {state.target_current}")


    else:
        print("No data received, but RTDE connection is established.")

    # Clean up connection
    rtde_con.send_pause()
    rtde_con.disconnect()
    print("RTDE connection closed.")

except Exception as e:
    print(f"Failed to connect to RTDE: {e}")
