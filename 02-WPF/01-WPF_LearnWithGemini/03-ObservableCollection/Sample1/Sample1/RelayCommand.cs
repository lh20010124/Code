using System;
using System.Windows.Input; // 必须引用，包含 ICommand 接口定义

namespace Sample1
{
    /// <summary>
    /// RelayCommand：中继命令类。
    /// 它的作用是把 UI 的“点击动作”转换成 ViewModel 里的“方法调用”。
    /// 它是连接 View 和 ViewModel 的桥梁，彻底摆脱了 Code-behind 事件处理。
    /// </summary>
    public class RelayCommand : ICommand
    {
        // 1. 核心委托：存储执行逻辑和判断逻辑
        // Action<object> 是一个没有返回值的委托，存放要执行的方法
        private readonly Action<object> _execute;
        // Predicate<object> 是一个返回 bool 的委托，存放“是否可执行”的逻辑
        private readonly Predicate<object> _canExecute;

        /// <summary>
        /// 构造函数
        /// </summary>
        /// <param name="execute">必填：当命令执行时要运行的方法</param>
        /// <param name="canExecute">可选：决定命令是否可用的判断方法</param>
        public RelayCommand(Action<object> execute, Predicate<object> canExecute = null)
        {
            // 防御性编程：如果 execute 为空，直接抛出异常，防止程序在运行时崩溃
            _execute = execute ?? throw new ArgumentNullException(nameof(execute));
            _canExecute = canExecute;
        }

        // 2. CanExecute：WPF 会自动调用此方法来判断绑定了该命令的按钮是否变灰
        // 如果没有传入 _canExecute 逻辑，则默认认为命令始终可用 (true)
        public bool CanExecute(object parameter) => _canExecute == null || _canExecute(parameter);

        // 3. Execute：执行实际的业务逻辑
        // 这里的 parameter 是通过 XAML 中 CommandParameter 传递过来的参数
        public void Execute(object parameter) => _execute(parameter);

        // 4. CanExecuteChanged：这是命令的核心触发器
        // 为什么用 CommandManager.RequerySuggested？
        // 当用户在 UI 上有任何操作（如鼠标移动、输入字符），WPF 的全局命令管理器
        // 就会发出 RequerySuggested 信号，这会触发 WPF 自动重新调用所有的 CanExecute 方法，
        // 从而实时刷新按钮的启用/禁用状态。
        public event EventHandler CanExecuteChanged
        {
            add => CommandManager.RequerySuggested += value;
            remove => CommandManager.RequerySuggested -= value;
        }
    }
}