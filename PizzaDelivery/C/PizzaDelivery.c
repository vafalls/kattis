#include<stdio.h>
#include<stdlib.h>

int nrOfColumns, nrOfRows;

void printTown(int rows, int col, int town[col][rows]) {
  printf("[");
  for(int x=0; x<rows; x++){
    for(int y=0; y<col; y++){
      printf("%d", town[x][y]);
    }
    printf(" ");
  }
  printf("]\n");
}


int nrOfBlocksFromPos(int _x, int _y, int town[_x][_y]){
  int dist = 0;
  
  for(int x=0; x<nrOfRows; x++){
    for(int y=0; y<nrOfColumns; y++){
      printf("town=%d %d,%d ",town[x][y], x, y);
      if(town[x][y] > 0){
        dist += (town[x][y]*((abs(_x-x))+(abs(_y-y))));
      }
    }
  }
  return dist;
}


void testCaseExecution() {
  scanf("%d %d", &nrOfColumns, &nrOfRows);

  int town[nrOfRows][nrOfColumns];

  for(int x=0; x<nrOfRows; x++){
    for(int y=0; y<nrOfColumns; y++){
      scanf("%d", &town[x][y]);
    }
  }

  printTown(nrOfRows, nrOfColumns, town);

  int shortWay = 9999999;
  int currWay=0;

  for(int x=0; x<nrOfRows; x++){
    for(int y=0; y<nrOfColumns; y++){
      currWay = nrOfBlocksFromPos(x, y, town);
      printf("currway: %d\n",currWay);
      if(currWay < shortWay){
        shortWay = currWay;
      }
    }
  }

  printTown(nrOfRows, nrOfColumns, town);
  printf("%d blocks\n", shortWay);
}


int main() {
  int nrOfTestCases;
  scanf("%u", &nrOfTestCases);
  for(int i=0; i<nrOfTestCases; i++){
    testCaseExecution();
  }
}
