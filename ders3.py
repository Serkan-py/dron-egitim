from pymavlink import mavutil
import sys
master = mavutil.mavlink_connection('127.0.0.1:14550')

master.wait_heartbeat()

print("baglandi")


mode = 'GUIDED'

#degistirilecek olan modun uygun olup olmadigini kontrol ediyor.
if mode not in master.mode_mapping():
    print('Unknown mode : {}'.format(mode))
    print('Try:', list(master.mode_mapping().keys()))
    sys.exit(1)

#mod ID sini aliyor
mode_id = master.mode_mapping()[mode]

#modu degistiren komut
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id)

#modun degisip degismedigini kontrol eden komut
while True:
    # Wait for ACK command
    # Would be good to add mechanism to avoid endlessly blocking
    # if the autopilot sends a NACK or never receives the message
    ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
    ack_msg = ack_msg.to_dict()

    # Continue waiting if the acknowledged command is not `set_mode`
    if ack_msg['command'] != mavutil.mavlink.MAV_CMD_DO_SET_MODE:
        continue

    # Print the ACK result !
    print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
    break