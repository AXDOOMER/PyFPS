#module.exports = function (point, vs) {
#    // ray-casting algorithm based on
#    // http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
#    
#    var x = point[0], y = point[1];
#    
#    var inside = false;
#    for (var i = 0, j = vs.length - 1; i < vs.length; j = i++) {
#        var xi = vs[i][0], yi = vs[i][1];
#        var xj = vs[j][0], yj = vs[j][1];
#        
#        var intersect = ((yi > y) != (yj > y))
#            && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
#        if (intersect) inside = !inside;
#    }
#    
#    return inside;
#};

#https://github.com/substack/point-in-polygon/blob/master/index.js
def pointInPoly(point, vertices) {
	# ray-casting algorithm based on
	# http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html

	x = point[0]
	y = point[1]

	inside = False
	for(i = 0, j = vertices.length - 1; i < vertices.length; j = i++) {
		xi = vertices[i][0]
		yi = vertices[i][1]
		xj = vertices[j][0]
		yj = vertices[j][1]
        
		intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
		if intersect:
			inside = !inside
	}

	return inside
}
