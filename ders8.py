from pymavlink import mavutil
import sys
master = mavutil.mavlink_connection('127.0.0.1:14550')

master.wait_heartbeat()

print("baglandi")


x = 5
y = 10
alt = -10


master.mav.set_position_target_local_ned_send(
    0, master.target_system, master.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b110111111000,
    x,
    y,
    alt,
    0, 0, 0, 0, 0, 0, 0, 0
)

