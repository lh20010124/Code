using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Data;
using System.Windows.Media;

namespace Test
{
    public class PriorityColorConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            int priority = (int)value;
            return priority switch
            {
                2 => Brushes.Red,    // 高优先级
                1 => Brushes.Orange, // 中优先级
                _ => Brushes.Gray    // 低优先级或默认
            };
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
