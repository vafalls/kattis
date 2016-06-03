private void printTown(){
        //System.out.println("nrOfColumns:"+nrOfColumns+" nrOfRows:"+nrOfRows);
        for(int x=0; x<nrOfRows; x++){
        System.out.print("[");
        for(int y=0; y<nrOfColumns; y++){
        System.out.print(town[x][y]+" ");
        }
        System.out.print("]");
        }
        System.out.println();
        }