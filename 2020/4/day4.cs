using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Solution
{
    class Passport {
        private List<string> RequiredFields;
        private List<string> RequiredFieldsPart2;

        private static Dictionary<string, string> keyRegexVerifiers = new Dictionary<string, string>() {
            {"byr", @"19[2-9]\d|200[0-2]"},
            {"iyr", @"20(1\d|20)"},
            {"eyr", @"20(2\d|30)"},
            {"hgt", @"(1([5-8]\d|9[0-3])cm)|((59|6\d|7[0-6])in)"},
            {"hcl", @"#[\da-f]{6}"},
            {"ecl", @"amb|blu|brn|gry|grn|hzl|oth"},
            {"pid", @"\d{9}"},
        };

        public Passport() {
            RequiredFields = new List<string>{
                "byr",
                "iyr",
                "eyr",
                "hgt",
                "hcl",
                "ecl",
                "pid",
            };
            RequiredFieldsPart2 = new List<string>{
                "byr",
                "iyr",
                "eyr",
                "hgt",
                "hcl",
                "ecl",
                "pid",
            };
        }

        /// <summary>Determines if a passport is valid or not by checking if 
        /// all of the required fields exists.</summary>
        public bool IsValid() {
            return RequiredFields.Count == 0;
        }

        public bool IsValidPart2() {
            return RequiredFieldsPart2.Count == 0;
        }

        /// <summary>Updates the passport by marking the key as existing if the
        /// required criteria for the provided field are met.</summary>
        public void Update(string key, string val) {
            RequiredFields.Remove(key);

            if (RequiredFieldsPart2.Contains(key)) {
                // Verifiy if the fields are valid using some regex rules.
                Regex reg = new Regex(keyRegexVerifiers[key]);
                Match m = reg.Match(val);
                
                if (m.Value.Equals(val)) {
                    RequiredFieldsPart2.Remove(key);
                }
            }
        }
    }

    class Day4
    {
        /// <summary>Parses the line into the corresponding key:value pairs and
        /// updates the passport with these values.</summary>
        static void parseLineAndUpdatePassport(string line, Passport passport) {
            string[] kvPairs = line.Split(' ');
            foreach (string kvPair in kvPairs)
            {
                string[] kv = kvPair.Split(':');
                string key = kv[0];
                string val = kv[1];

                passport.Update(key, val);
            }
        }

        static void Main(string[] args) {

            int validPassports = 0;
            int validPassportsPart2 = 0;

            using (StreamReader file = new StreamReader("input")) {
                string line;

                while ((line = file.ReadLine()) != null) {
                    Passport passport = new Passport();

                    parseLineAndUpdatePassport(line, passport);

                    while ((line = file.ReadLine()) != null && line != "") {
                        parseLineAndUpdatePassport(line, passport);
                    }

                    if (passport.IsValid()) {
                        validPassports++;
                    }

                    if (passport.IsValidPart2()) {
                        validPassportsPart2++;
                    }
                }
            }

            Console.WriteLine($"{validPassports} passports are valid.");
            Console.WriteLine($"{validPassportsPart2} passports are valid with stricter rules.");
        }
    }
}