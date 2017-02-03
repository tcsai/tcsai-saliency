import sys
sys.path.append("../PyGazeAnalyser")
from pygazeanalyser import eyetribereader, gazeplotter
import os

IMGDIR = os.path.join('/home/akos/Documents/tcsai-saliency/mod_imgs')
IMGNAMES = os.listdir(IMGDIR)
outdir = os.path.join('/home/akos/Documents/tcsai-saliency/gazeviz')
RESOLUTION = (1024, 768)
DATAFILE = 'testdata/subject-5-1.tsv'
# ,stop="stop_trial"
gazedata = eyetribereader.read_eyetribe(DATAFILE,
									    "start_trial",
										stop_time=2995,  # first 3 seconds
										missing=0.0)

imgs = open("imgorder.txt").read().split('\n')
for i in range(len(gazedata)):
	if i < 4:
		pass
		# print gazedata[i]['events']['msg']
		# imgname = gazedata[i]['events']['msg'][69][1].split()[-1]
		# imgname = imgname.split('.')[0] + '.jpg'
	else:
		print i+4
		print gazedata[i]['events']['msg']
		# imgname = gazedata[i]['events']['msg'][71][1].split()[-1]
		imgname = imgs[i+4]
		imgname = imgname.split('.')[0] + '.jpg'
		imgfile = os.path.join(IMGDIR, imgname)
		print imgname, imgfile
		# get the fixations
		fixations = gazedata[i]['events']['Efix']
		# get the saccades
		saccades = gazedata[i]['events']['Esac']
		# plot a heatmap
		gazeplotter.draw_heatmap(fixations, RESOLUTION, imagefile=imgfile,
					alpha=0.5, invert_x=True, invert_y=False,
					savefilename=os.path.join(outdir, '%s_fix.png' % imgname))

		gazeplotter.draw_fixations(fixations, RESOLUTION, imagefile=imgfile,
				alpha=0.5, invert_x=True, invert_y=False,
				savefilename=os.path.join(outdir,'%s_heatmap.png' % imgname))


		# gazeplotter.draw_scanpath(fixations, saccades, RESOLUTION, imagefile=imgfile,
		#		alpha=0.5, invert_x=True, invert_y=False,
		#		savefilename=os.path.join(outdir ,'%s_scan.png' % imgname))

		print "YEEEEEEEEEEEE"
