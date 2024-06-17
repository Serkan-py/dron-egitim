from pymavlink import mavutil
import sys
import time

master = mavutil.mavlink_connection('127.0.0.1:14550')
master.wait_heartbeat()
print("baglandi")


while True:
    msg = master.recv_match()
    if not msg:
        continue
    if msg.get_type() == 'HEARTBEAT':
        #print("\n\n*****Got message: %s*****" % msg.get_type())
        #print("Message: %s" % msg)
        #print("\nAs dictionary: %s" % msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
        #print("\nSystem status: %s" % msg.system_status)
        msg1 = master.recv_match(type="GLOBAL_POSITION_INT",blocking=True)
        print(msg1)
        altitude = msg1.relative_alt/1000
        print(altitude)