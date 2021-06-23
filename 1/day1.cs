using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

namespace Solution
{
    class Day1
    {
        /// <summary>Finds the two values in the provided array that sum to the
        /// provided target.</summary>
        static (int, int) FindValuePairsThatSumTo(List<int> values, int target) {
            // Holds complementary values to those we've seen (target - value).
            HashSet<int> complementaryValues = new HashSet<int>();

            foreach (int value in values)
            {
                // Check if we've already encountered the complementary value
                // that would sum to the target.
                if (complementaryValues.Contains(value)) {
                    return (value, target - value);
                }

                complementaryValues.Add(target - value);
            }

            throw new ArgumentException("Array does not contain a solution.");
        }
    
        /// <summary>Finds the three values in the provided array that sum to
        /// the provided target.</summary>
        static (int, int, int) FindValueTriplesThatSumTo(List<int> values, int target) {
            while (values.Count > 2)
            {
                // Pop the first value and try to create the sum using that.
                int v1 = values[0];
                values.RemoveAt(0);

                try {
                    var (v2, v3) = FindValuePairsThatSumTo(values, target - v1);
                    return (v1, v2, v3);
                } catch (ArgumentException) {
                    // No solution existed using the first value.
                }
            }

            throw new ArgumentException("Array does not contain a solution.");
        }

        static void Main(string[] args) {
            string[] lines = File.ReadAllLines("input");
            int target = 2020;
            List<int> values = lines.Select(line => int.Parse(line)).ToList();
            int v1, v2, v3;

            (v1, v2) = FindValuePairsThatSumTo(values, target);
            Console.WriteLine($"{v1} and {v2} sum to {target}. Their product is {v1 * v2}.");

            (v1, v2, v3) = FindValueTriplesThatSumTo(values, target);
            Console.WriteLine($"{v1}, {v2} and {v3} sum to {target}. Their product is {v1 * v2 * v3}.");
        }
    }
}