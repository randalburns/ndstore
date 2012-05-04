import urllib2
import zlib
import StringIO
import numpy as np
import argparse
import cStringIO
import sys


def main():

  parser = argparse.ArgumentParser(description='Cutout a portion of the database.')
  parser.add_argument('token', action="store")
  parser.add_argument('xlow', action="store", type=int )
  parser.add_argument('xhigh', action="store", type=int)
  parser.add_argument('ylow', action="store", type=int)
  parser.add_argument('yhigh', action="store", type=int)
  parser.add_argument('zlow', action="store", type=int)
  parser.add_argument('zhigh', action="store", type=int)

  result = parser.parse_args()

#  url = 'http://127.0.0.1:8000/cutout/hayworth5nm/npz/3/' +\
  url = 'http://127.0.0.1/EM/cutout/hayworth5nm/npz/3/' +\
            str(result.xlow) + "," + str(result.xhigh) + "/" +\
            str(result.ylow) + "," + str(result.yhigh) + "/" +\
            str(result.zlow) + "," + str(result.zhigh) + "/"\

  print url

  #  Grab the bottom corner of the cutout
  xoffset = result.xlow
  yoffset = result.ylow
  zoffset = result.zlow

  # Get cube in question
  f = urllib2.urlopen ( url )

  zdata = f.read ()

  # get the data out of the compressed blob
  pagestr = zlib.decompress ( zdata[:] )
  pagefobj = StringIO.StringIO ( pagestr )
  cube = np.load ( pagefobj )

  voxlist= []

  # Again, should the interface be all zyx
  it = np.nditer ( cube, flags=['multi_index'])
  while not it.finished:
    if it[0] < 25:
      voxlist.append ( [ it.multi_index[2]+xoffset,\
                         it.multi_index[1]+yoffset,\
                         it.multi_index[0]+zoffset ] )
    it.iternext()

#  url = 'http://127.0.0.1:8000/annotate/%s/npvoxels/new/' % result.token
  url = 'http://127.0.0.1/EM/annotate/%s/npvoxels/new/' % result.token

  # Encode the voxelist an pickle
  fileobj = cStringIO.StringIO ()
  np.save ( fileobj, voxlist )

  # Build the post request
  req = urllib2.Request(url, fileobj.getvalue())
  response = urllib2.urlopen(req)
  the_page = response.read()

  print the_page


if __name__ == "__main__":
      main()


