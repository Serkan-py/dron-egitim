"""
Arkadaslar merhaba, bu python dosyasi insansiz bir araci kuzey(ileri), guney(geri), saga(dogu), sola(bati), yukari ve asagi yonlu 
haraket ettirmeniz icin hazirlandi. master.mav.set_position_target_local_ned_send komutundaki bazi parametreleri degistirerek gidilecek yonun merkezini,
gidilecek hizi veya sureyi ayarlayabilirsiniz.
iste yararlanacaginiz kaynaklarin linkleri:

https://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html#copter-commands-in-guided-mode-set-position-target-local-ned

https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_LOCAL_NED

bu iki sitede bu komutun nasil kullanilacagina yonelik detayli anlatim yapilmis zaten videoda anlatirken de bu kaynaklardan yararlaniyorum. hangi 
parametrenin ne ise yaradigini tek tek gorup anlayabilirsiniz. yine anlamadiginiz veya yapamadiginiz bir sey olursa bana mail veya linkedin 
uzerinden ulasabilirsiniz. Iletisim bilgilerim readme dosyasinda bulunmakta, iyi calismalar dilerim.

"""

from pymavlink import mavutil

master = mavutil.mavlink_connection('127.0.0.1:14550')

master.wait_heartbeat()

print("baglandi")


x = 10 #m/s
y = -5 #m/s
alt = 0 # yukari yon icin (-) asagi yon icin (+) deger verilmeli.


master.mav.set_position_target_local_ned_send(
    0, master.target_system, master.target_component,
    mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
    0b110111111000, 
    x,
    y,
    alt,
    0, 0, 0, 0, 0, 0, 0, 0
)

