

using System;
using System.Globalization;
using System.Windows.Data;
using System.Windows.Media;

namespace Sample3
{
    public abstract class BaseValueConverter : IValueConverter
    {
        // 强制子类必须实现
        public abstract object Convert(object value, Type targetType, object parameter, CultureInfo culture);

        // 默认不实现 ConvertBack，如果不需要可以抛出异常，但这里不要抛出 NotImplementedException 给 UI 线程，除非你确实需要
        public virtual object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
            => throw new NotImplementedException("该转换器不支持反向转换");
    }

    public class CompletedToOpacityConverter : BaseValueConverter
    {
        public override object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            return (bool)value ? 0.5 : 1.0;
        }
    }

    public class PriorityToColorConverter : BaseValueConverter
    {
        public override object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            int priority = (int)value;
            return priority switch
            {
                0 => Brushes.Green,
                1 => Brushes.Orange,
                _ => Brushes.Red,
            };
        }
    }

}
