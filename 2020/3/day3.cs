using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

namespace Solution
{
    class Point {
        public int X { get; set; }
        public int Y { get; set; }

        public Point(int x, int y) {
            this.X = x;
            this.Y = y;
        }

        public override string ToString()
        {
            return $"({X}, {Y})";
        }

        public static Point operator +(Point p1, Point p2) {
            return new Point(p1.X + p2.X, p1.Y + p2.Y);
        }
    }

    class Day3
    {
        /// <summary>Traverses the map from (0, 0) using the provided slope
        /// until it exists the bottom of the map.</summary>
        /// <returns>Returns the amount of trees encountered during the
        /// traversal of the map.</returns>
        static int TraverseMapAndCountTrees(Point slope) {
            int trees = 0;

            using(StreamReader file = new StreamReader("input")) {
                string mapLine;
                // Starting position.
                Point pos = new Point(0, 0);

                while ((mapLine = file.ReadLine()) != null) {
                    int mapWidth = mapLine.Length;

                    if (mapWidth != 31) {
                        Console.WriteLine("hmm");
                    }

                    // Check if we are in a tree. Repeat the map as needed.
                    if (mapLine[pos.X % mapWidth] == '#') {
                        trees++;
                    }

                    // Traverse the map.
                    pos += slope;

                    // Move the map down to account for our new position.
                    for (int i = 0; i < slope.Y - 1; i++)
                    {
                        file.ReadLine();
                    }
                }
            }
            return trees;
        }

        static void Main(string[] args) {
            Point[] slopes = {
                new Point(1, 1),
                new Point(3, 1),
                new Point(5, 1),
                new Point(7, 1),
                new Point(1, 2),
            };
            // For this example the product will exceed the max int value.
            long treeProduct = 1;
            
            foreach (var slope in slopes)
            {
                int trees = TraverseMapAndCountTrees(slope);
                treeProduct *= trees;
                Console.WriteLine($"Using slope {slope} we will encounter {trees} trees.");                
            }

            Console.WriteLine($"Multiplying the encountered trees for each slope produce {treeProduct}.");
        }
    }
}