using System;

class Program
{
    static void ReverseString(string str)
    {
        if (str.Length == 0)
            return;

        ReverseString(str.Substring(1));
        Console.Write(str[0]);
    }

    static void Main()
    {
        string input = "tiger";
        ReverseString(input);
    }
}

