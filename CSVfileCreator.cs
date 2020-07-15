using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Reflection;


namespace CSVWriter
{

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
            if (max>min){
                return random.Next(min, max);
            }
            return min;
        }
    }

    public class Data
    {
        public override string ToString()
        {
            var props = this.GetType().GetProperties();
            var sb = new StringBuilder();
            String prefix = "";
            foreach (var p in props)
            {
                sb.Append(prefix);
                prefix = ",";
                sb.Append(p.GetValue(this, null));
            }
            sb.Append("\n");
            return sb.ToString();
        }
    }
    namespace data
    {
        public class BasicUser : Data
        {
            public int basic_user_id { get; set; }
            public string email { get; set; }
            public string password { get; set; }
            public int age { get; set; }

            public BasicUser(int number)
            {
                basic_user_id = number;
                email = RandomValues.RandomString(10);
                password = RandomValues.RandomString(10);
                age = RandomValues.RandomInt(100);
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
        }
        public class BasicUserSong : Data
        {
            public int id { get; set; }
            public int basic_user_id { get; set; }
            public int song_id { get; set; }
            public int session_id { get; set; }
            public BasicUserSong(int number)
            {   
                basic_user_id = RandomValues.RandomInt(1, number);
                song_id = RandomValues.RandomInt(1, number);
                session_id = RandomValues.RandomInt(1, number);

            }
        }
    }

    public class Script
    {
        const string FILE_PATH = "data.csv";
        const int ROW_NUMBER = 250;

        private static List<Type> GetTypesInNamespace(Assembly assembly, string nameSpace)
        {
            var resultList = assembly.GetTypes()
                      .Where(t => String.Equals(t.Namespace, nameSpace, StringComparison.Ordinal))
                      .ToArray();
            return resultList.OfType<Type>().ToList();
        }

        private static StringBuilder PopulateObjectData(StringBuilder csv, int rowNumber, Type className)
        {
            List<Object> data = new List<Object>();
            var i = 0;
            Console.Write(className);
            csv.AppendLine("className:"+className.Name.ToString());
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
            foreach (var type in classList)
            {
                Console.Write(type);
                csv = PopulateObjectData(csv, ROW_NUMBER, type);
            }
            return csv;
        }

        private static void CreateCSVFile()
        {
            var csv = new StringBuilder();
            List<Type> typeList = GetTypesInNamespace(Assembly.GetExecutingAssembly(), "CSVWriter.data");
            csv = PopulateData(csv, typeList);
            File.WriteAllText(FILE_PATH, csv.ToString());
        }
        static void Main(string[] args)
        {
            CreateCSVFile();

        }
    }

}