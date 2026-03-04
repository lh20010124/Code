using System;
using System.Globalization;
using System.Windows.Data;
using System.Windows.Media;

namespace Sample1
{
    public class CompletedToColorConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            // 如果任务已完成(true)，返回灰色，否则返回黑色
            return (bool)value ? Brushes.Gray : Brushes.Black;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
            => throw new NotImplementedException();
    }
}