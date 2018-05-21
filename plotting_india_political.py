import matplotlib.pyplot as plt

INDIA_SVG_SIZE = [425,480]#size of the svg image want to convert into
Patna_POS = [230, 205]#position of the required place

def draw_India_map(map_name):
	"""will locate India's capital and required place"""
	
	#opening the file
	with open(map_name, 'rb') as map_file:
		#reading the file through imread function of matplotlib
		map_img = plt.imread(map_file)
	
	#storing the dimmensions using shape function of numpy
	ypixels, xpixels, bands = map_img.shape
	print(ypixels, xpixels, bands)

	#plotting the map image
	implot = plt.imshow(map_img)
	
	#plot the nation's capital using coordinates of the image provided in green colour
	plt.scatter(x = xpixels/3, y = ypixels/3, s = 100, c = "Green")

	#will plot the required place using red colour and relative position to image given
	plt.scatter(x = Patna_POS[0] * xpixels/ INDIA_SVG_SIZE[0], y = Patna_POS[1] * ypixels / INDIA_SVG_SIZE[1], s =100, c ="RED")

	#showing the image
	plt.show()
	
#calling the function	
draw_India_map("india.png")
	
