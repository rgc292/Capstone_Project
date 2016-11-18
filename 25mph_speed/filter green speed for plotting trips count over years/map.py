#!/usr/bin/python

import sys
import csv
import StringIO

class Point:
        def __init__(self,x,y):
                self.x = x
                self.y = y
                
class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)

		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in xrange(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)

		self.bound = (minx,miny,maxx,maxy)


	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]
			
			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)

			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c

	def bounds(self):
		return self.bound

def simplePolygonTest_lga(lat,lon):
    # Create a simple polygon
    #poly1 = Polygon([Point(40.713674, -74.011846), Point(40.713601, -74.011642), Point(40.715508, -74.011017), Point(40.718135, -74.010341), Point(40.718163, -74.010540), Point(40.715703, -74.011170), Point(40.714988, -74.011428), Point(40.713674, -74.011846)])
    #poly2 = Polygon([Point(40.702548, -74.012991), Point(40.702272, -74.012970), Point(40.703118, -74.010202), Point(40.706631, -74.004902), Point(40.709429, -74.001554), Point(40.709592, -74.001812), Point(40.707689, -74.004151), Point(40.704322, -74.009193), Point(40.703459, -74.010438), Point(40.702548, -74.012991)])
    #poly3 = Polygon([Point(40.715548, -74.009429), Point(40.715401, -74.009150), Point(40.719906, -74.005567), Point(40.720053, -74.005824), Point(40.715548, -74.009429)])
    #poly4 = Polygon([Point(40.712612, -74.004858), Point(40.712352, -74.004419), Point(40.717816, -73.999741), Point(40.718060, -74.000213), Point(40.712612, -74.004858)])
    #poly5 = Polygon([Point(40.721045, -74.003989),Point(40.720882, -74.003786),Point(40.726354, -73.999086),Point(40.726468, -73.999312),Point(40.721045, -74.003989)])
    poly7 = Polygon([Point(40.872923, -73.910287), Point(40.879802, -73.928140), Point(40.747153, -74.020151), Point(40.698757, -74.018434), Point(40.710599, -73.974145), Point(40.746243, -73.968309), Point(40.778748, -73.938096), Point(40.785377, -73.938268), Point(40.796684, -73.927968), Point(40.803831, -73.929513), Point(40.809678, -73.933633), Point(40.824488, -73.933462), Point(40.835139, -73.934320), Point(40.856436, -73.921445), Point(40.870716, -73.909772), Point(40.872923, -73.910287)])
    #poly7 = Polygon([Point(40.729782, -74.009265), Point(40.729766, -74.009136), Point(40.730392, -74.009039), Point(40.730481, -74.009018), Point(40.731116, -74.008900), Point(40.731124, -74.009029), Point(40.730498, -74.009136), Point(40.730392, -74.009157), Point(40.729782, -74.009265)])
    #poly8 = Polygon([Point(40.727660, -73.985366), Point(40.727587, -73.985184), Point(40.728091, -73.984808), Point(40.728181, -73.984744), Point(40.728701, -73.984379), Point(40.728782, -73.984540), Point(40.728254, -73.984926), Point(40.728172, -73.984980), Point(40.727660, -73.985366)])
    #poly9 = Polygon([Point(40.745885, -74.005598), Point(40.745828, -74.005426), Point(40.746332, -74.005062), Point(40.746413, -74.005008), Point(40.746941, -74.004611), Point(40.747015, -74.004772), Point(40.746478, -74.005180), Point(40.746405, -74.005244), Point(40.745885, -74.005598)])
    #poly10 = Polygon([Point(40.746633, -73.997600), Point(40.746576, -73.997449), Point(40.747128, -73.997052), Point(40.747210, -73.996999), Point(40.748356, -73.996151), Point(40.748429, -73.996323), Point(40.747283, -73.997160), Point(40.747202, -73.997224), Point(40.746633, -73.997600)])
    #poly11 = Polygon([Point(40.742235, -73.987101), Point(40.742162, -73.986930), Point(40.742698, -73.986533), Point(40.742788, -73.986490), Point(40.743308, -73.986093), Point(40.743381, -73.986265), Point(40.742837, -73.986651), Point(40.742755, -73.986726), Point(40.742235, -73.987101)])
    #poly12 = Polygon([Point(40.756516, -74.001580), Point(40.756443, -74.001398), Point(40.756979, -74.000990), Point(40.757060, -74.000947), Point(40.757605, -74.000539), Point(40.757686, -74.000711), Point(40.756841, -74.001344), Point(40.756516, -74.001580)])
    #poly13 = Polygon([Point(40.752956, -73.989282), Point(40.752913, -73.989180), Point(40.752913, -73.989180), Point(40.753531, -73.988719), Point(40.754080, -73.988306), Point(40.754124, -73.988410), Point(40.753574, -73.988815), Point(40.753511, -73.988864), Point(40.752956, -73.989282)])
    #poly14 = Polygon([Point(40.747988, -73.973643), Point(40.747939, -73.973536), Point(40.748496, -73.973123), Point(40.748565, -73.973059), Point(40.749106, -73.972672), Point(40.749146, -73.972774), Point(40.748618, -73.973182), Point(40.748545, -73.973236), Point(40.747988, -73.973643)])
    #poly15 = Polygon([Point(40.765420, -73.987620), Point(40.765372, -73.987502), Point(40.765924, -73.987084), Point(40.765997, -73.987030), Point(40.766554, -73.986628), Point(40.766603, -73.986741), Point(40.766042, -73.987143), Point(40.765973, -73.987197), Point(40.765420, -73.987620)])
    #poly16 = Polygon([Point(40.758082, -73.981840), Point(40.758037, -73.981728), Point(40.758586, -73.981325), Point(40.758655, -73.981272), Point(40.759208, -73.980859), Point(40.759257, -73.980966), Point(40.758708, -73.981390), Point(40.758631, -73.981438), Point(40.758082, -73.981840)])
    #poly17 = Polygon([Point(40.753547, -73.980920), Point(40.753482, -73.980765), Point(40.754108, -73.980368), Point(40.754181, -73.980319), Point(40.754734, -73.979906), Point(40.754779, -73.980019), Point(40.754218, -73.980432), Point(40.754149, -73.980480), Point(40.753547, -73.980920)])
    #poly18 = Polygon([Point(40.762251, -73.966149), Point(40.762198, -73.966042), Point(40.762739, -73.965645), Point(40.762812, -73.965597), Point(40.763377, -73.965178), Point(40.763429, -73.965291), Point(40.762861, -73.965699), Point(40.762792, -73.965752), Point(40.762251, -73.966149)])
    #poly19 = Polygon([Point(40.776796, -73.979332), Point(40.776747, -73.979225), Point(40.777356, -73.978785), Point(40.777437, -73.978726), Point(40.778051, -73.978281), Point(40.778100, -73.978383), Point(40.777482, -73.978839), Point(40.777401, -73.978893), Point(40.776796, -73.979332)])
    #poly20 = Polygon([Point(40.770458, -73.954122), Point(40.770409, -73.954015), Point(40.770958, -73.953613), Point(40.771035, -73.953559), Point(40.771600, -73.953157), Point(40.771644, -73.953259), Point(40.771080, -73.953672), Point(40.771011, -73.953720), Point(40.770458, -73.954122)])
    #poly21 = Polygon([Point(40.784615, -73.973652), Point(40.784546, -73.973491), Point(40.785086, -73.973061), Point(40.785155, -73.973013), Point(40.785724, -73.972600), Point(40.785793, -73.972788), Point(40.785228, -73.973196), Point(40.785155, -73.973244), Point(40.784615, -73.973652)])
    #poly22 = Polygon([Point(40.774679, -73.948114), Point(40.774630, -73.948012), Point(40.775199, -73.947599), Point(40.775268, -73.947551), Point(40.775873, -73.947100), Point(40.775922, -73.947197), Point(40.775321, -73.947647), Point(40.775240, -73.947706), Point(40.774679, -73.948114)])
    #poly23 = Polygon([Point(40.791288, -73.979445), Point(40.791252, -73.979322), Point(40.791706, -73.978683), Point(40.791747, -73.978576), Point(40.792113, -73.977669), Point(40.792206, -73.977766), Point(40.791824, -73.978683), Point(40.791637, -73.979080), Point(40.791288, -73.979445)])
    #poly24 = Polygon([Point(40.780864, -73.956644), Point(40.780827, -73.956547), Point(40.781392, -73.956115), Point(40.781449, -73.956070), Point(40.782011, -73.955665), Point(40.782054, -73.955756), Point(40.781493, -73.956169), Point(40.781432, -73.956212), Point(40.780864, -73.956644)])
    #poly25 = Polygon([Point(40.802316, -73.970086), Point(40.802289, -73.970000), Point(40.802919, -73.969544), Point(40.802982, -73.969501), Point(40.803522, -73.969120), Point(40.803562, -73.969200), Point(40.803006, -73.969584), Point(40.802316, -73.970086)])
    #poly26 = Polygon([Point(40.792312, -73.946306), Point(40.792263, -73.946210), Point(40.792878, -73.945767), Point(40.792933, -73.945722), Point(40.793514, -73.945306), Point(40.793550, -73.945402), Point(40.792978, -73.945824), Point(40.792917, -73.945869), Point(40.792312, -73.946306)])
    #poly27 = Polygon([Point(40.808916, -73.954062), Point(40.809446, -73.953560), Point(40.809503, -73.953515), Point(40.810065, -73.953027), Point(), Point(40.810118, -73.953201), Point(40.809541, -73.953595), Point(40.809477, -73.953657), Point(40.808916, -73.954062)])
    #poly28 = Polygon([Point(40.804551, -73.951518), Point(40.804509, -73.951419), Point(40.805087, -73.951003), Point(40.805148, -73.950957), Point(40.805708, -73.950552), Point(40.805753, -73.950646), Point(40.805191, -73.951057), Point(40.805126, -73.951102), Point(40.804551, -73.951518)])
    #poly29 = Polygon([Point(40.803132, -73.938414), Point(40.803087, -73.938307), Point(40.803648, -73.937888), Point(40.803721, -73.937845), Point(40.804322, -73.937405), Point(40.804371, -73.937507), Point(40.803757, -73.937947), Point(40.803696, -73.937993), Point(40.803132, -73.938414)])
    #poly30 = Polygon([Point(40.827108, -73.940164), Point(40.827067, -73.940062), Point(40.827627, -73.939660), Point(40.827701, -73.939606), Point(40.828249, -73.939231), Point(40.828293, -73.939317), Point(40.827701, -73.939740), Point(40.827108, -73.940164)])
    #poly31 = Polygon([Point(40.817869, -73.941787), Point(40.817816, -73.941680), Point(40.818376, -73.941277), Point(40.818445, -73.941224), Point(40.818993, -73.940827), Point(40.819038, -73.940923), Point(40.818530, -73.941304), Point(40.818425, -73.941385), Point(40.817869, -73.941787)])
    #poly32 = Polygon([Point(40.808332, -73.938823), Point(40.808283, -73.938710), Point(40.808847, -73.938308), Point(40.808912, -73.938249), Point(40.809472, -73.937857), Point(40.809509, -73.937954), Point(40.808957, -73.938362), Point(40.808892, -73.938415), Point(40.808332, -73.938823)])
    #poly33 = Polygon([Point(40.843619, -73.936170), Point(40.843570, -73.936068), Point(40.844154, -73.935645), Point(40.844219, -73.935596), Point(40.844799, -73.935167), Point(40.844836, -73.935253), Point(40.844256, -73.935682), Point(40.844183, -73.935747), Point(40.843619, -73.936170)])
    #poly34 = Polygon([Point(40.834787, -73.940706), Point(40.834739, -73.940599), Point(40.835770, -73.939853), Point(40.835835, -73.939799), Point(40.836504, -73.939333), Point(40.836545, -73.939445), Point(40.835904, -73.939907), Point(40.835360, -73.940288), Point(40.834787, -73.940706)])
    #poly35 = Polygon([Point(40.849783, -73.940867), Point(40.849750, -73.940722), Point(40.850355, -73.940561), Point(40.850440, -73.940534), Point(40.851304, -73.940207), Point(40.851304, -73.940357), Point(40.850408, -73.940668), Point(40.849783, -73.940867)])
    #poly36 = Polygon([Point(40.851674, -73.933713), Point(40.851629, -73.933622), Point(40.852165, -73.933220), Point(40.852238, -73.933172), Point(40.852846, -73.932732), Point(40.852899, -73.932834), Point(40.852274, -73.933260), Point(40.852205, -73.933319), Point(40.851674, -73.933713)])
    # Create point
    pt = Point(lat,lon)

    # Test if the polygon contains the point (This polygon is the whole Manhattan)
    if (poly7.contains(pt)): #or poly2.contains(pt) or poly3.contains(pt) or poly4.contains(pt) or poly5.contains(pt) or poly6.contains(pt) or poly7.contains(pt) or poly8.contains(pt) or poly9.contains(pt) or poly10.contains(pt) or poly11.contains(pt) or poly12.contains(pt) or poly13.contains(pt) or poly14.contains(pt) or poly15.contains(pt) or poly16.contains(pt) or poly17.contains(pt) or poly18.contains(pt) or poly19.contains(pt) or poly20.contains(pt) or poly21.contains(pt) or poly22.contains(pt) or poly23.contains(pt) or poly24.contains(pt) or poly25.contains(pt) or poly26.contains(pt) or poly27.contains(pt) or poly28.contains(pt) or poly29.contains(pt) or poly30.contains(pt) or poly31.contains(pt) or poly32.contains(pt) or poly33.contains(pt) or poly34.contains(pt) or poly35.contains(pt) or poly36.contains(pt)):
        return True
    else:
        return False

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    try:
    #Fill in your map code here. To write to output file, use "print"
    # remove leading and trailing whitespace
        csv_file = StringIO.StringIO(line) 
        csv_reader = csv.reader(csv_file)
        
    except:
        pass
         
    for l in csv_reader:

		try:
			if (l[0].upper() == 'VENDOR_ID' or l[1] == '' or l[2] == '' or l[5] == '' or l[6] == '' or l[7] == '' or l[8] == '' or  l[5] == '0' or l[6] == '0' or l[7] == '0' or l[8] == '0' or float(l[10]) > 15.0 or float(l[10]) < .1):
					pass

			else:
				try:
						pick = simplePolygonTest_lga(float(l[6]), float(l[5]))
						drop = simplePolygonTest_lga(float(l[8]), float(l[7]))

						if not(pick and drop):
								pass

						else:

								dateTime_p = l[1].split(' ')
								date_p = dateTime_p[0]
								time_p = float(dateTime_p[1].split(':')[0]) + float(dateTime_p[1].split(':')[1])/float(60) + float(dateTime_p[1].split(':')[2])/float(3600)
								dateTime_d = l[2].split(' ')
								date_d = dateTime_d[0]
								time_d = float(dateTime_d[1].split(':')[0]) + float(dateTime_d[1].split(':')[1])/float(60) + float(dateTime_d[1].split(':')[2])/float(3600)
								duration = time_d-time_p

								if duration < 0:
										duration = 24 + duration

								speed = float(l[10])/float(duration)
								
								if (speed > 70.0 or speed <= 0.):
								    pass
								else:
								    print "%s\t%d" %(date_p[:7],1)
				except:
					pass

		except:
			pass
