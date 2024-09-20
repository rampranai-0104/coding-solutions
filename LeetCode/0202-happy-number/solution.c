bool isHappy(int n) {
    int sum=0,digit;
    if(n==1)
      return true;
      while(n>4)
      {
        while(n!=0)
        {
            digit=n%10;
            n/=10;
            sum+=digit*digit;
        }
        if(sum==1)
        return true;
        n=sum;
        sum=0;
      }
      return false;
    }

