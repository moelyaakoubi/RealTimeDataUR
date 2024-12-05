import rtde.rtde as rtde
import rtde.rtde_config as rtde_config
import csv
import time

# Robot connection details
ROBOT_HOST = "192.168.0.1"  # Replace with your robot's IP
ROBOT_PORT = 30004          # RTDE port

# CSV file path
CSV_FILE = "robot_joint_data.csv"

# Load RTDE configuration
config_filename = "control_configuration.xml"  # Provided in RTDE examples
config = rtde_config.ConfigFile(config_filename)
output_names, output_types = config.get_output_configuration()

# Connect to the robot
con = rtde.RTDE(ROBOT_HOST, ROBOT_PORT)
if not con.connect():
    print("Unable to connect to the robot")
    exit()

# Setup outputs
if not con.send_output_setup(output_names, output_types):
    print("Unable to configure output setup")
    exit()

# Start RTDE communication
if not con.send_start():
    print("Unable to start RTDE")
    exit()

# Open CSV file for logging
with open(CSV_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write CSV header
    writer.writerow(["Timestamp", "Joint1_Pos", "Joint2_Pos", "Joint3_Pos", "Joint4_Pos", "Joint5_Pos", "Joint6_Pos",
                     "Joint1_Cur", "Joint2_Cur", "Joint3_Cur", "Joint4_Cur", "Joint5_Cur", "Joint6_Cur"])

    # Move the robot to an initial position
    # (Assumes the robot is in freedrive mode or a separate program handles movement)
    print("Logging data. Press Ctrl+C to stop.")

    try:
        while True:
            # Receive data from the robot
            state = con.receive()
            if state is None:
                break

            # Get joint positions and currents
            joint_positions = state.actual_q           # Joint positions
            joint_currents = state.actual_current      # Joint currents
            timestamp = time.time()                   # Current timestamp

            # Write data to the CSV file
            writer.writerow([timestamp] + joint_positions + joint_currents)

            # Add a small delay for data logging frequency (e.g., 10 Hz)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Data logging stopped.")

# Close RTDE connection
con.send_pause()
con.disconnect()

print(f"Data has been saved to {CSV_FILE}")
