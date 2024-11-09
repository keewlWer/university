using System;

public class Solution
{
    public void DuplicateZeros(int[] arr)
    {
        int n = arr.Length;
        int zeros = 0;

        // Підраховуємо кількість нулів
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == 0)
            {
                zeros++;
            }
        }

        // Починаємо з кінця масиву
        for (int i = n - 1; i >= 0; i--)
        {
            // Якщо поточний елемент — нуль, потрібно подвоїти його
            if (arr[i] == 0)
            {
                if (i + zeros < n) arr[i + zeros] = 0;  // Подвоюємо нуль
                zeros--;
                
                if (i + zeros < n) arr[i + zeros] = 0;  // Другий нуль на нову позицію
            }
            else
            {
                if (i + zeros < n) arr[i + zeros] = arr[i];  // Переміщаємо елемент
            }
        }
    }
}

class Program
{
    static void Main()
    {
        var solution = new Solution();
        
        // Приклад 1
        int[] arr1 = { 1, 0, 2, 3, 0, 4, 5, 0 };
        solution.DuplicateZeros(arr1);
        Console.WriteLine(string.Join(", ", arr1));  // Виведе: 1, 0, 0, 2, 3, 0, 0, 4

        // Приклад 2
        int[] arr2 = { 1, 2, 3 };
        solution.DuplicateZeros(arr2);
        Console.WriteLine(string.Join(", ", arr2));  // Виведе: 1, 2, 3
    }
}
