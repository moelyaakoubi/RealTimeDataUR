Overview
This project is a Python-based platform designed for real-time data extraction, logging, and control of a Universal Robot (UR3) using the RTDE (Real-Time Data Exchange) protocol. The platform enables efficient monitoring of robot states and motion parameters while providing capabilities for real-time control.

Features
Real-time data extraction for joint positions, velocities, TCP pose, forces, and more.
Customizable sampling rate and data fields through an XML configuration file.
Logging to CSV or binary files for analysis and integration.
Real-time robot control by sending commands such as target joint positions or speeds.
Compatibility with existing URScript programs running on the teach pendant.


Prerequisites
Universal Robot (UR3) with RTDE enabled.
Python 3.x.
Universal Robots RTDE Python library (rtde).
A configured robot program running on the teach pendant (if needed for motion).


Installation
1. Clone this repository:
   git clone https://github.com/moelyaakoubi/RealTimeDataUR.git
2. Configure the record_configuration.xml file to specify the data fields you want to log.

Usage
Start a Robot Program (if needed):
Load and run a robot program from the teach pendant to move the robot to predefined waypoints.

Run the Data Logger:
Use the following command to start the data logging process:
python record.py --host 192.168.0.1 --samples 1000 --frequency 125 --output robot_data.csv

Log Data:
The selected data fields (configured in record_configuration.xml) will be recorded in the specified output file.

Control the Robot (Optional):
Modify the script to send control commands (e.g., target joint positions) via RTDE using input registers.

Configuration
XML File (record_configuration.xml):
Define the data fields for extraction and their types (e.g., joint positions, TCP pose).

Command-Line Arguments:

--host: IP address of the robot.
--port: RTDE port (default is 30004).
--samples: Number of samples to log (use 0 for continuous logging).
--frequency: Sampling rate in Hz.
--output: Output file name for the logged data.


Example Workflow
1. Define the robot motion program (8 waypoints) on the teach pendant.
2. Start the program to move the robot through the waypoints.
3. Run the Python script to log joint positions and other parameters during motion.
4. Analyze the recorded data to extract insights or validate performance.


