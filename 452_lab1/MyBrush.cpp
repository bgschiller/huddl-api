#include "cse452.h"
#include "MyBrush.h"
#include "BrushInterface.h"
#include <cmath>
#include <iostream>

using namespace std;

void MyBrush::changedBrush() {
    // this is called anytime the brush type or brush radius changes
    // it should recompute the brush mask appropriately
    const int radius = brushUI->getRadius();
	const int brushType = brushUI->getBrushType();

//	int** pixelArray = maskCalc(radius);

}

// int** MyBrush::maskCalc (int r) {
// 	int	x = 0, y = r;
// 	int deltaE = 2 * x + 3;
// 	int deltaSE = 2 * (x - y) + 5;
// 	float decision = (x + 1)*(x + 1) + (y - 0.5)*(y - 0.5) - r*r;
// 	WritePixel(x, y);
// 	while (y	>	x) {
// 		if (decision	<	0) {	//	Move	East	
// 			x++; WritePixel(x, y);
// 			decision += deltaE;
// 			deltaE += 2; deltaSE += 2; //	Update	deltas
// 		}
// 		else {	//	Move	SouthEast
// 			y--;	x++; WritePixel(x, y);
// 			decision += deltaSE;
// 			deltaE += 2; deltaSE += 4; //	Update	deltas
// 		}
// 	}
// }

void MyBrush::drawBrush() {
    // apply the current brush mask to image location (x,y)
    // the mouse location is in mouseDrag
    const int radius = brushUI->getRadius();
    const float pixelFlow = brushUI->getFlow();
    const Color colBrush = brushUI->getColor();
	this->putPixel(mouseDrag[0], mouseDrag[1], colBrush);
}

void MyBrush::drawLine( ) {
    // draw a thick line from mouseDown to mouseDrag
    // the width of the line is given by the current brush radius
    const int radius = brushUI->getRadius();
    const Color colBrush = brushUI->getColor();


	int dx = (mouseDrag[0] - mouseDown[0]), dy = (mouseDrag[1] - mouseDown[1]);
	int	d = 2 *	dy - dx;
	int	incrE = 2 *	dy;
	int	incrNE = 2 * (dy - dx);
	int	x =	mouseDown[0], y = mouseDown[1];
	this->putPixel(x, y, colBrush);
	while (x < mouseDrag[0]) {
		if (d <= 0)	d += incrE;
		else {d += incrNE; ++y;}
		++x;
		this->putPixel(x, y, colBrush);
	}
	while (x > mouseDrag[0]) {
		if (d <= 0)	d -= incrE;
		else {d -= incrNE; --y;}
		--x;
		this->putPixel(x, y, colBrush);
	}
}

void MyBrush::drawCircle() {
    // draw a thick circle at mouseDown with radius r
    // the width of the circle is given by the current brush radius
}


void MyBrush::drawPolygon() {
    // draw a polygon with numVertices whos coordinates are stored in the
    // polygon array: {x0, y0, x1, y1, ...., xn-1, yn-1}
}

void MyBrush::filterRegion( ) {
    // apply the filter indicated by filterType to the square
    // defined by the two corner points mouseDown and mouseDrag
    // these corners are not guarenteed to be in any order
    // The filter width is given by the brush radius
}