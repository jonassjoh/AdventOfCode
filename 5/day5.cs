using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

namespace Solution
{
    class Day5
    {
        /// <summary>Parses the binary string consisting of [FB]* to the
        /// corresponding value in the range determined by 2^n - 1 where n is the
        /// length of the provided string.
        /// 
        /// For example: consider FBFBBFFRLR: 
        ///     Start by considering the whole range, 0 through 127.
        ///     F means to take the lower half, keeping 0 through 63.
        ///     B means to take the upper half, keeping 32 through 63.
        ///     F keeps 32 through 47.
        ///     B keeps 40 through 47.
        ///     B keeps 44 through 47.
        ///     F keeps 44 through 45.
        ///     The final F keeps the lower of the two, 44.</summary>
        static int parseBinaryValue(string str) {
            int maxValue = (int) Math.Pow(2, str.Length) - 1;
            int minValue = 0;

            foreach (char value in str)
            {
                int diff = maxValue - minValue;

                if (value == 'F') {
                    // Round down.
                    maxValue = minValue + diff / 2;
                }
                else {
                    // Round up.
                    minValue += (int) Math.Ceiling((double) diff / (double) 2);
                }
            }

            // minValue and maxValue have the same value.
            return minValue;
        }

        /// <summary>Finds the lowest available seat ID.</summary>
        static int findAvailableSeat(List<int> seats) {
            seats.Sort();

            int lastSeat = seats[0] - 1;
            foreach (var seat in seats)
            {
                if (lastSeat + 1 != seat) {
                    return lastSeat + 1;
                }
                lastSeat = seat;
            }

            // There are no available seats, so let's just return a
            // non-existing seat... maybe the floor (not that of the plane)?
            return -1;
        }

        static void Main(string[] args) {

            int highestId = -1;

            List<int> takenSeats = new List<int>();

            using (StreamReader file = new StreamReader("input")) {
                string line;

                while ((line = file.ReadLine()) != null) {
                    line = line.Replace('L', 'F').Replace('R', 'B');

                    string rowString = line.Substring(0, 7);
                    string colString = line.Substring(7, 3);

                    int row = parseBinaryValue(rowString);
                    int col = parseBinaryValue(colString);

                    int seatId = row * 8 + col;

                    highestId = Math.Max(highestId, seatId);

                    takenSeats.Add(seatId);
                }
            }

            int mySeat = findAvailableSeat(takenSeats);

            Console.WriteLine($"The highest seat ID is {highestId}.");
            Console.WriteLine($"My seat ID is {mySeat}.");
        }
    }
}