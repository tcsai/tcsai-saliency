from pygazeanalyser import eyetribereader, gazeplotter
import os

IMGDIR = os.path.join('/home/akos/Documents/tcsai-saliency/imgs')
IMGNAMES = os.listdir(IMGDIR)
outdir = os.path.join('/home/akos/Documents/tcsai-saliency/gazeviz')
RESOLUTION = (1024, 768)


gazedata = eyetribereader.read_eyetribe('testdata/subject-0-1.tsv', 
											     "start_trial", stop="stop_trial", 
											      missing=0.0)

for i in range(len(gazedata)):
	# Warm up cases
	if i < 4:
		imgname = gazedata[i]['events']['msg'][69][1].split()[-1]
		imgname = imgname.split('.')[0] + '.jpg'
	else:
		imgname = gazedata[i]['events']['msg'][71][1].split()[-1]
		imgname = imgname.split('.')[0] + '.jpg'
		imgfile = os.path.join(IMGDIR,imgname)
		print imgname, imgfile
		# get the fixations
		fixations = gazedata[i]['events']['Efix']
			# plot a heatmap
		gazeplotter.draw_heatmap(fixations, RESOLUTION, imagefile=imgfile, durationweight=True,
					alpha=0.5, savefilename=os.path.join(outdir,'%s_heatmap.png' % imgname))
		print "YEEEEEEEEEEEE"

	