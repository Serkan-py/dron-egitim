"""
Haritada rastgele bir koordinata gitmesi saglanacak.
"""

from pymavlink import mavutil

master = mavutil.mavlink_connection('127.0.0.1:14550')

master.wait_heartbeat()

print("baglandi")


lat = -35.36321282 
lon = 149.16531987
alt = 14


master.mav.set_position_target_global_int_send(
    0, master.target_system, master.target_component,
    mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
    0b110111111000,
    int(lat * 1e7),
    int(lon * 1e7),
    alt,
    0, 0, 0, 0, 0, 0, 0, 0
)

