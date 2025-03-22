bool digitCount(char * num)
{
    int l = strlen(num);
    for(int i=0;i<l;i++)
    {
        int count = 0;
        for(int j = 0;j<l;j++)
        {
            if(i==num[j]-'0')
            count++;
        }
        if(count != num[i]-'0')
        return false;
    }
    return true;
}
