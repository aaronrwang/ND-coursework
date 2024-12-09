//Aaron Wang - Fund Comp - Lab 10 - fractals.c
//Program makes graphics for severl different fractals

#include "gfx.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define PI 3.14
void sierpinski( int x1, int y1, int x2, int y2, int x3, int y3 );
void drawTriangle( int x1, int y1, int x2, int y2, int x3, int y3 );
void shrinkingSquares(int x, int y, int r, int mrgn);
void spiralSquares(int centerx, int centery, double r, double d, double angle);
void drawSquare(int x1, int y1, int x2, int y2);
void circularLace(int x, int y, int size);
void snowFlake(int x, int y, int r, double angle);
void tree(double x, double y, double l, double angle);
void fern(double x, double y, double l, double angle);
void spirals(int centerx, int centery, double d, double angle);

int main()
{
  int width = 800, height = 800, mrgn = 20;
  char c;
  gfx_open(width, height, "Fractals");
  while (1) {
    c = gfx_wait();
    gfx_clear();

    if (c == '1') {  
      sierpinski(mrgn, mrgn, width-mrgn, mrgn, width/2, height-mrgn);
    } else if (c == '2') { 
      shrinkingSquares(width/2,height/2, width/4, mrgn);
    } else if (c == '3') {
      spiralSquares(width/2,height/2,width/10,width/2,0);
    } else if (c == '4') {
      circularLace(width/2,height/2,width/3);
    } else if (c == '5') {
      snowFlake(width/2,height/2,width/3, PI/2);
    } else if (c == '6') {
      tree(width/2,height-mrgn,height/3,PI/2);
    } else if (c == '7') {
      fern(width/2,height-mrgn,2*height/3,PI/2);
    } else if (c == '8') {   // Spiral of Spirals 
      spirals(width/2,height/2,width/2,0);
    } else if (c == 'q') { 
        break;
    }
  }
}

void sierpinski(int x1, int y1, int x2, int y2, int x3, int y3){
  // Base case. 
  if( abs(x2-x1) < 5 ) return;

  // Draw a triangle
  drawTriangle( x1, y1, x2, y2, x3, y3 );

  // Recursive calls
  sierpinski( x1, y1, (x1+x2)/2, (y1+y2)/2, (x1+x3)/2, (y1+y3)/2 );
  sierpinski( (x1+x2)/2, (y1+y2)/2, x2, y2, (x2+x3)/2, (y2+y3)/2 );
  sierpinski( (x1+x3)/2, (y1+y3)/2, (x2+x3)/2, (y2+y3)/2, x3, y3 );
}

void drawTriangle(int x1, int y1, int x2, int y2, int x3, int y3){
  gfx_line(x1,y1,x2,y2);
  gfx_line(x2,y2,x3,y3);
  gfx_line(x3,y3,x1,y1);
}

void shrinkingSquares(int x, int y, int r, int mrgn){
  if (r<2) return;

  drawSquare(x+r,y+r,x-r,y-r);

  shrinkingSquares(x+r,y+r,r/2-mrgn/2,mrgn/2);
  shrinkingSquares(x+r,y-r,r/2-mrgn/2,mrgn/2);
  shrinkingSquares(x-r,y+r,r/2-mrgn/2,mrgn/2);
  shrinkingSquares(x-r,y-r,r/2-mrgn/2,mrgn/2);
}
void spiralSquares(int centerx, int centery, double r,double d, double angle){
  if(r<0.5) return;
  int x = (int) centerx+d*cos(angle);
  int y = (int) centery+d*sin(angle);
  drawSquare(x+r,y+r,x-r,y-r);

  spiralSquares(centerx,centery,r*.9,d*.9,angle+PI/5);
}
void drawSquare(int x1, int y1, int x2, int y2){
  gfx_line(x1,y1,x1,y2);
  gfx_line(x2,y1,x2,y2);
  gfx_line(x1,y1,x2,y1);
  gfx_line(x1,y2,x2,y2);
}

void circularLace(int x, int y, int r){
  if (r<2) return;
  gfx_circle(x,y,r);
  
  for(int i = 0; i < 6;i++){
    circularLace(x+r*cos(i*PI/3),y+r*sin(i*PI/3),r/3);
  }
}

void snowFlake(int x, int y, int r, double angle){
  if (r<1) return;
  
  
  for(int i = 0; i < 5;i++){
    gfx_line(x,y,x+r*cos(2*i*PI/5+angle),y+r*sin(2*i*PI/5+angle));
    snowFlake(x+r*cos(2*i*PI/5+angle),y+r*sin(2*i*PI/5+angle),r/3,2*i*PI/5+angle);
  }
}

void tree(double x, double y, double l, double angle){
  if(l<1) return;
  gfx_line(x,y,x-l*cos(angle),y-l*sin(angle));
  x=x-l*cos(angle);
  y=y-l*sin(angle);
  tree(x,y,2*l/3,angle+35*PI/180);
  tree(x,y,2*l/3,angle-35*PI/180);
}

void fern(double x, double y, double l, double angle){
  if(l<5) return;
  gfx_line(x,y,x-l*cos(angle),y-l*sin(angle));
  double intervalX = l*cos(angle)/4;
  double intervalY = l*sin(angle)/4;
  //printf("%g, %g\n",intervalX,intervalY);

  for(int i = 0; i < 4; i++){
    x-=intervalX;
    y-=intervalY;
    fern(x,y,l/3,angle+35*PI/180);
    fern(x,y,l/3,angle-35*PI/180);
  }
}

void spirals(int centerx, int centery, double r, double angle){
  if (r<1) return;
  int x = (int) centerx+r*cos(angle);
  int y = (int) centery+r*sin(angle);
  gfx_point(x,y);
  double newAngle = angle+PI/5;
  spirals(centerx,centery,r*.85,newAngle);
  spirals(x,y,r*.375,newAngle);
}