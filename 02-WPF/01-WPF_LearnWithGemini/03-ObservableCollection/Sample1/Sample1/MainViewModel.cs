using System.Collections.ObjectModel; // 必须引用，这是动态列表的关键
using System.Windows.Input;

namespace Sample1
{
    public class MainViewModel
    {
        // ObservableCollection 会自动向 UI 发送增删通知
        public ObservableCollection<TodoItem> TodoList { get; } = new ObservableCollection<TodoItem>();

        public ICommand AddTaskCommand { get; }
        public ICommand DeleteTaskCommand { get; }

        public MainViewModel()
        {
            // 初始化数据
            TodoList.Add(new TodoItem { Title = "学习 WPF 动态列表" });

            // 添加逻辑：直接操作集合
            AddTaskCommand = new RelayCommand(obj =>
                TodoList.Add(new TodoItem { Title = $"新任务 {TodoList.Count + 1}" }));

            // 删除逻辑：接收参数（即要删除的那一项对象）
            DeleteTaskCommand = new RelayCommand(obj =>
            {
                if (obj is TodoItem item)
                    TodoList.Remove(item);
            });
        }
    }
}