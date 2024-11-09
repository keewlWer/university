using System;

class Program
{
    static double MyPow(double x, int n)
    {
        if (n == 0)
            return 1;

        if (n < 0)
            return 1 / MyPow(x, -n);

        double half = MyPow(x, n / 2);

        if (n % 2 == 0)
            return half * half;
        else
            return half * half * x;
    }

    static void Main()
    {
        double x = 2.0;
        int n = -2;
        Console.WriteLine(MyPow(x, n));
    }
}
