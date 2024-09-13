int addDigits(int num) {
    int sum = 0;
    while(num>0)
    {
        
        int r  = num%10;
        sum+=r;
        num = (num/10);
    }
    if (sum>9)
    return addDigits(sum);
    else 
    return sum;
}
