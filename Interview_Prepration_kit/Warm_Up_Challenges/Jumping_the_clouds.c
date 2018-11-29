
// Complete the jumpingOnClouds function below.
int jumpingOnClouds(int c_count, int* c) {
    int count; 
    for(int i=0;i<(c_count-1);i){
        if(c[i+2]==0){
            i=i+2;
            count++;
        }
        else{
            i=i+1;
            count++;
        }
    }
    return count;


}
