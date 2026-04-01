using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Sample1
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            List<Color> test = new List<Color>();
            test.Add(new Color() { Code = "#ADFF2F", Name = "黄绿色" });
            test.Add(new Color() { Code = "#00FF7F", Name = "春绿色" });
            test.Add(new Color() { Code = "#90EE90", Name = "浅绿色" });
            test.Add(new Color() { Code = "#8FBC8F", Name = "深海绿色" });
            test.Add(new Color() { Code = "#3CB371", Name = "中海绿色" });
            test.Add(new Color() { Code = "#2E8B57 ", Name = "海绿色" });
            list.ItemsSource = test;
        }
    }

    //黄绿色	＃ADFF2F rgb（173,255,47）
    //春绿色	＃00FF7F rgb（0,255,127）
    //浅绿色	＃90EE90 RGB（144,238,144）
    //深海绿色	＃8FBC8F rgb（143,188,143）
    //中海绿色	＃3CB371 rgb（60,179,113）
    //海绿色	＃2E8B57 rgb（46,139,87）

    public class Color
    {
        public string Code { get; set; }
        public string Name { get; set; }
    }
}
