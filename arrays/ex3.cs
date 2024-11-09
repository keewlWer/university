using System;

public class Solution
{
    public int[] SortedSquares(int[] nums)
    {
        int n = nums.Length;
        int[] result = new int[n];
        int left = 0, right = n - 1, index = n - 1;
        
        // Пройдемо по масиву з двома вказівниками
        while (left <= right)
        {
            int leftSquare = nums[left] * nums[left];
            int rightSquare = nums[right] * nums[right];
            
            if (leftSquare > rightSquare)
            {
                result[index--] = leftSquare;
                left++;
            }
            else
            {
                result[index--] = rightSquare;
                right--;
            }
        }
        
        return result;
    }
}

class Program
{
    static void Main()
    {
        var solution = new Solution();
        
        // Приклад 1
        int[] nums1 = { -4, -1, 0, 3, 10 };
        int[] result1 = solution.SortedSquares(nums1);
        Console.WriteLine(string.Join(", ", result1));  // Виведе: 0, 1, 9, 16, 100

        // Приклад 2
        int[] nums2 = { -7, -3, 2, 3, 11 };
        int[] result2 = solution.SortedSquares(nums2);
        Console.WriteLine(string.Join(", ", result2));  // Виведе: 4, 9, 9, 49, 121
    }
}
