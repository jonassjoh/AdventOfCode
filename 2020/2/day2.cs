using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

namespace Solution
{
    class Day2
    {
        /// <summary>Checks is a password is valid by counting if it contains
        /// the required amount of a certain charcter.</summary>
        static bool passwordIsValidPart1(char requiredChar, int minOccurances, int maxOccurances, string password) {
            int requiredCharOccurances = password.Count(c => c == requiredChar);
        
            return (requiredCharOccurances >= minOccurances &&
                    requiredCharOccurances <= maxOccurances);
        }

        /// <summary>Checks is a password is valid by checking if one, and only
        /// one, of the provided indices of the password contains the required
        /// provided character.</summary>
        static bool passwordIsValidPart2(char requiredChar, int i1, int i2, string password) {
            bool firstIndex = password[i1 - 1] == requiredChar;
            bool secondIndex = password[i2 - 1] == requiredChar;
        
            return (firstIndex != secondIndex);
        }

        static void Main(string[] args) {
            StreamReader file = new StreamReader("input");
            int validPart1PasswordsCount = 0;
            int validPart2PasswordsCount = 0;
            char[] separators = {'-', ':', ' '};
            string line;

            while ((line = file.ReadLine()) != null) {
                var splitLine = line.Split(separators, StringSplitOptions.RemoveEmptyEntries);
                
                int minOccurances = int.Parse(splitLine[0]);
                int maxOccurances = int.Parse(splitLine[1]);
                char requiredChar = char.Parse(splitLine[2]);
                string password = splitLine[3];

                if (passwordIsValidPart1(requiredChar, minOccurances, maxOccurances, password)) {
                    validPart1PasswordsCount++;
                }
                if (passwordIsValidPart2(requiredChar, minOccurances, maxOccurances, password)) {
                    validPart2PasswordsCount++;
                }
            }

            Console.WriteLine($"There are {validPart1PasswordsCount} valid passwords in the database using the wrong policy.");
            Console.WriteLine($"There are {validPart2PasswordsCount} valid passwords in the database using the corrected policy.");
        }
    }
}