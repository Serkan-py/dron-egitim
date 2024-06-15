from pymavlink import mavutil

master = mavutil.mavlink_connection('127.0.0.1:14550')

master.wait_heartbeat()

print("baglandi")