using System;
using System.ComponentModel; // 提供 INotifyPropertyChanged 接口
using System.Runtime.CompilerServices; // 提供 CallerMemberName 特性
using System.Windows.Input; // 提供 ICommand 接口

namespace Sample1
{
    /// <summary>
    /// MainViewModel：作为 UI 的逻辑中枢。
    /// 它实现了 INotifyPropertyChanged，使得任何绑定到此 ViewModel 的 UI 
    /// 都能在数据变化时自动感知并更新。
    /// </summary>
    public class MainViewModel : INotifyPropertyChanged
    {
        // 1. 私有字段：存储实际数据，UI 不直接访问此字段
        private string _userName = "Gemini";

        // 2. 属性更改事件：这是 MVVM 的“广播天线”
        // WPF 绑定系统会订阅此事件，一旦触发，UI 就会去重新读取对应的属性值
        public event PropertyChangedEventHandler PropertyChanged;

        /// <summary>
        /// UserName 属性：View 将绑定到此属性
        /// </summary>
        public string UserName
        {
            get => _userName;
            set
            {
                // 性能优化：只有值真正改变时才触发通知，避免冗余刷新
                if (_userName != value)
                {
                    _userName = value;
                    // OnPropertyChanged() 不传参时，[CallerMemberName] 会自动获取属性名 "UserName"
                    OnPropertyChanged();
                }
            }
        }

        // 3. 命令定义：公开 ICommand 供 XAML 绑定
        // 它们替代了后台代码中的 Button_Click 事件
        public ICommand ChangeNameCommand { get; }
        public ICommand ClearNameCommand { get; }

        /// <summary>
        /// 构造函数：初始化命令并绑定业务逻辑
        /// </summary>
        public MainViewModel()
        {
            // 使用 Lambda 表达式定义命令的具体行为
            // 这里 obj 表示传递过来的参数，此处我们暂未使用参数，直接修改 UserName
            ChangeNameCommand = new RelayCommand(obj => UserName = "数据已更新！");
            ClearNameCommand = new RelayCommand(obj => UserName = "");
        }

        /// <summary>
        /// 触发通知的方法
        /// [CallerMemberName] 是一个神奇的特性，它能自动捕获调用该方法的属性名。
        /// 这样你就不需要手动写 OnPropertyChanged("UserName") 了。
        /// </summary>
        protected void OnPropertyChanged([CallerMemberName] string name = null)
            => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}