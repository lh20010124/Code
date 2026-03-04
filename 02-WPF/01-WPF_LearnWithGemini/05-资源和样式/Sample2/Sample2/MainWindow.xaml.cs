
using System.Windows;
using System.Windows.Media;

namespace Sample2
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.DataContext = new MainViewModel();
        }

        private void ToggleTheme_Click(object sender, RoutedEventArgs e)
        {
            // 获取全局资源字典
            var res = Application.Current.Resources;

            // 如果当前是白色，就切换成深灰色
            if (((SolidColorBrush)res["BgColor"]).Color == Colors.White)
            {
                res["BgColor"] = new SolidColorBrush(Colors.LightBlue);
                res["TextColor"] = new SolidColorBrush(Colors.Red);
            }
            else
            {
                res["BgColor"] = new SolidColorBrush(Colors.White);
                res["TextColor"] = new SolidColorBrush(Colors.Black);
            }
        }
    }
}
