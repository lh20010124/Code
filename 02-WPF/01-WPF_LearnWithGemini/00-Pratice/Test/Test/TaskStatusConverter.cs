using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Data;

namespace Test
{
    public class TaskStatusConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            // value 是绑定的 IsDone (bool)
            bool isDone = (bool)value;
            return isDone ? 0.4 : 1.0; // 完成则 40% 透明度，未完成则不透明
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException(); // 通常不需要反向转换
        }
    }
}
