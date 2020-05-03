using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;

namespace CSVWriter {

    public class RandomValues
    {
        private static Random random = new Random();
        public static string RandomString(int length)
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            return new string(Enumerable.Repeat(chars, length)
              .Select(s => s[random.Next(s.Length)]).ToArray());
        }

        public static int RandomInt(int max)
        {
            return random.Next(max);
        }

        public static int RandomInt(int min, int max)
        {
            return random.Next(min, max);
        }
    }

    public class Data
    {
        public static Data getRandomObj(int number)
        {
            return new Data();
        }
    }
    public class User:Data
    {
        public int basic_user_id { get; set; }
        public string email { get; set; }
        public string password { get; set; }
        public int age { get; set; }

        public User(int number)
        {
            basic_user_id = number;
            email = RandomValues.RandomString(10);
            password = RandomValues.RandomString(10);
            age = RandomValues.RandomInt(100);
        }
        public override string ToString()   
        {
            return "User:" + basic_user_id + "," + email + ","+ password + ","+ age + "\n";
        }
    }

    public class Song : Data
    {
        public int song_id { get; set; }
        public string name { get; set; }
        public int length { get; set; }
        public int rating { get; set; }
        public Song(int number)
        {
            song_id = number;
            name = RandomValues.RandomString(10);
            length = RandomValues.RandomInt(10);
            rating = RandomValues.RandomInt(100);
        }
        public override string ToString()
        {
            return "Song:" + song_id + "," + name + "," + length + "," + rating + "\n";
        }
    }

    public class Session : Data
    {
        public int session_id { get; set; }
        public int day { get; set; }
        public int month { get; set; }
        public int year { get; set; }
        public int duration { get; set; }
        public string device { get; set; }
        public Session(int number)
        {
            session_id = number;
            day = RandomValues.RandomInt(30);
            month = RandomValues.RandomInt(12);
            year = RandomValues.RandomInt(2019, 2020);
            duration = RandomValues.RandomInt(2019, 2020);
        }
        public override string ToString()
        {
            return "Session:" + session_id+","+day + "," + month + "," + year + "," + duration + "\n";
        }
    }
    public class BasicUserSong : Data
    {
        public int basic_user_id { get; set; }
        public int song_id { get; set; }
        public int session_id { get; set; }
        public int feedback_id { get; set; }
        public BasicUserSong(int number)
        {
            basic_user_id = RandomValues.RandomInt(number);
            song_id = RandomValues.RandomInt(number);
            session_id = RandomValues.RandomInt(number);

        }
        public override string ToString()
        {
            return "BasicUserSong:" + basic_user_id + "," + song_id + "," + session_id + "," + feedback_id + "\n";
        }
    }


    public class Script
    {
        const string FILE_PATH = "D:\\university\\templating\\SpotifyServerPart\\SpotifyServerPart\\data.txt";
        const int ROW_NUMBER = 250;
        private static StringBuilder PopulateObjectData(StringBuilder csv, int rowNumber, Type className)
        {
            List<Object> data = new List<Object>();
            var i = 0;
            Console.Write(className);
            while (i < rowNumber)
            {
                var dataObject = Activator.CreateInstance(className, i);
                               
                if (!data.Contains(dataObject))
                {
                    data.Add(dataObject);
                }
                Console.Write(dataObject.ToString());
                csv.AppendLine(dataObject.ToString());
                i++;
            }
            return csv;
        }

        private static StringBuilder PopulateData(StringBuilder csv, List<Type> classList)
        {
            foreach (Type type in classList) {
                Console.Write(type);
                csv = PopulateObjectData(csv, ROW_NUMBER, type);
            }
            return csv;
        }
        static void Main(string[] args)
        {

            var csv = new StringBuilder();
            List<Type> classList = new List<Type> {
                typeof(User),
                typeof(Song),
                typeof(Session),
                typeof(BasicUserSong)
            };
            csv = PopulateData(csv, classList);
        
            File.WriteAllText(FILE_PATH, csv.ToString());
        }
    }

}