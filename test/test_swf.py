from __future__ import absolute_import
from swf.movie import SWF
from swf.tag import Tag

import colorama as clrm

def test_header():

  if True and False:
    fn = './test/data/test.swf'
    hdrFrmCnt = 1
  else:
    fn = '../BDL/Games/Evony/.com.evony.download1.EvonyClient1922.swf'
    hdrFrmCnt = 2

  f = open(fn, 'rb')
  swf = SWF(f)

  Tag._colourOffsetLen = clrm.Back.GREEN
  Tag._colourName = clrm.Back.BLUE
  Tag._colourOff = clrm.Style.RESET_ALL
  print(swf)

  print(f'BTW swf.header.frame_count = {swf.header.frame_count}')
  assert swf.header.frame_count == hdrFrmCnt

test_header()
print('done')
