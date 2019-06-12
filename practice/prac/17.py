#encoding: utf-8


src = '/tmp/kk.iso'
dst = '/tmp/kk2.iso'

src_handler = open(src,'rb')
dst_handler = open(dst,'wb')

BUFFER_SIZE = 1024 * 1024

while True:
    btxt = src_handler.read(BUFFER_SIZE)
    if b'' == btxt:
        break
    dst_handler.write(btxt)
    dst_handler.flush()

dst_handler.close()
src_handler.close()
