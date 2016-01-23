import base64
import wave

with open(r'C:\pc19.txt', 'rb') as f:
    data = f.read()

with open(r'pc19.wav', 'wb') as f:
    f.write(base64.decodebytes(data))

wi = wave.open('pc19.wav', 'rb')
wo = wave.open('pc19-x.wav', 'wb')
wo.setparams(wi.getparams())
for i in range(wi.getnframes()):
    wo.writeframes(wi.readframes(1)[::-1])
wi.close()
wo.close()
