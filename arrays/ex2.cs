using System;

public class Solution
{
    public int FindNumbers(int[] nums)
    {
        int count = 0;  // Лічильник чисел з парною кількістю цифр

        foreach (var num in nums)
        {
            // Перетворюємо число в рядок і перевіряємо, чи кількість цифр парна
            if (num.ToString().Length % 2 == 0)
            {
                count++;  // Якщо парна кількість цифр, збільшуємо лічильник
            }
        }

        return count;
    }
}

class Program
{
    static void Main()
    {
        var solution = new Solution();
        
        // Приклад 1
        int[] nums1 = { 12, 345, 2, 6, 7896 };
        Console.WriteLine(solution.FindNumbers(nums1));

        // Приклад 2
        int[] nums2 = { 555, 901, 482, 1771 };
        Console.WriteLine(solution.FindNumbers(nums2));
    }
}
