using System;

class Program
{
    static int ClimbStairs(int n)
    {
        if (n <= 1) return 1;
        return ClimbStairs(n - 1) + ClimbStairs(n - 2);
    }

    static void Main()
    {
        int n = 3;
        Console.WriteLine(ClimbStairs(n));
    }
}
