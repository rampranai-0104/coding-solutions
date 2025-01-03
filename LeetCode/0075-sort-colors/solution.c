void sortColors(int* a, int numsSize) {
    for(int gap=numsSize/2;gap>=1;gap=gap/2) {
        for(int j=gap;j<numsSize;j++) {
            for (int i=j-gap;i>=0;i=i-gap) {
                if(a[i+gap]>a[i]) {
                    break;
                }
                else {
                    int t=a[i];
                    a[i]=a[i+gap];
                    a[i+gap]=t;
                }
            }
        }
    }
}
