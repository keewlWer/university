using System;

public class Solution
{
    public int FindMaxConsecutiveOnes(int[] nums)
    {
        int maxCount = 0;  // Змінна для збереження максимальної кількості одиничних елементів
        int currentCount = 0;  // Поточний лічильник одиничних елементів

        foreach (var num in nums)
        {
            if (num == 1)
            {
                currentCount++;  // Якщо елемент 1, збільшуємо поточний лічильник
            }
            else
            {
                maxCount = Math.Max(maxCount, currentCount);  // Оновлюємо максимальну кількість
                currentCount = 0;  // Обнуляємо поточний лічильник
            }
        }

        // Після проходу через весь масив, перевіряємо ще раз на випадок, коли масив закінчується одиницею
        return Math.Max(maxCount, currentCount);
    }
}

class Program
{
    static void Main()
    {
        var solution = new Solution();
        
        // Приклад 1
        int[] nums1 = { 1, 1, 0, 1, 1, 1 };
        Console.WriteLine(solution.FindMaxConsecutiveOnes(nums1));
        
        // Приклад 2
        int[] nums2 = { 1, 0, 1, 1, 0, 1 };
        Console.WriteLine(solution.FindMaxConsecutiveOnes(nums2));
    }
}
